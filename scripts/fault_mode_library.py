import os
import re
import time
import json
import qianfan
import requests
import pandas as pd
from openai import OpenAI
from typing import Text, Dict
from tqdm import trange

# baidu qianfan
os.environ["QIANFAN_ACCESS_KEY"] = ""
os.environ["QIANFAN_SECRET_KEY"] = ""

# moonshot kimi
os.environ["MOONSHOT_API_KEY"] = ""


class ChatBot:

    def ask(self, prompt: Text, llm: Text = "kimi", debug=False):
        """
        调用模型进行对话
        :param prompt: 提示语
        :param llm: 选择模型
        :param debug: 是否打印调试信息
        """
        return {
            "qianfan": self.ask_baidu_qianfan,
            "kimi": self.ask_moonshot_kimi
        }[llm](prompt, debug)

    def ask_baidu_qianfan(self, prompt: Text, debug=False):
        """
        调用 百度云 千帆
        :param prompt: 提示语 (注意请强调返回json格式)
        """
        # 发送请求
        chat_comp = qianfan.ChatCompletion()
        resp = chat_comp.do(model="ERNIE-4.0-8K", messages=[{
            "role": "user",
            "content": prompt,
        }])
        # 解析返回结果
        extracted_obj = None
        try:
            resp_obj = resp["body"]
            # 打印调试信息
            if debug:
                print("*" * 50)
                print(f"本轮对话ID: {resp_obj['id']}")
                print(f"回包类型: {resp_obj['object']}")
                print(f"时间戳: {resp_obj['created']}")
                print(f"当前生成的结果是否被截断: {resp_obj['is_truncated']}")
                print(f"是否关闭当前会话，清理历史会话信息: {resp_obj['need_clear_history']}")
                print(f"输出内容标识: {resp_obj['finish_reason']}")
                print(f"token统计信息: {resp_obj['usage']}")
            # 提取json格式的回答
            pattern = r'```json(.*?)```'
            pattern_compiled = re.compile(pattern, re.DOTALL)
            result = resp_obj["result"]
            match_obj = pattern_compiled.search(result)  
            if match_obj:
                extracted_content = match_obj.group(1).strip()
                extracted_obj = json.loads(extracted_content)
            else:  
                print("内容提取失败\n", result)
        except:
            print("响应解析异常\n", resp_obj)
        return extracted_obj
    
    def ask_moonshot_kimi(self, prompt: Text, debug=False):
        """
        调用 月之暗面 Kimi
        :param prompt: 提示语 (注意请强调返回json格式)
        """
        # 计时开始
        start_time = time.perf_counter()
        # 创建一个OpenAI客户端
        client = OpenAI(
            api_key = os.getenv("MOONSHOT_API_KEY"),
            base_url = "https://api.moonshot.cn/v1",
        )
        # 调用对话接口
        completion = client.chat.completions.create(
            model = "moonshot-v1-8k",
            messages = [{
                "role": "user",
                "content": prompt,
            }],
            temperature = 0.3,
        )
        # 解析返回结果
        extracted_obj = None
        try:
            # 打印调试信息
            if debug:
                print("*" * 50)
                print(f"id: {completion.id}")
                print(f"created: {completion.created}")
                print(f"model: {completion.model}")
                print(f"completion_tokens: {completion.usage.completion_tokens}")
                print(f"prompt_tokens: {completion.usage.prompt_tokens}")
                print(f"total_tokens: {completion.usage.total_tokens}")
            # 提取json格式的回答
            pattern = r'```json(.*?)```'
            pattern_compiled = re.compile(pattern, re.DOTALL)
            result = completion.choices[0].message.content
            match_obj = pattern_compiled.search(result)  
            if match_obj:
                extracted_content = match_obj.group(1).strip()
                extracted_obj = json.loads(extracted_content)
            else:
                try:
                    extracted_obj = json.loads(result)
                except (json.JSONDecodeError, TypeError):
                    print("内容提取失败\n", result)
        except:
            print("响应解析异常\n", completion)
        # 计时结束
        end_time = time.perf_counter()
        # 等待到x秒 免费版有速率限制
        wait_for_x_seconds(start_time, end_time)
        return extracted_obj


def wait_for_x_seconds(start_time, end_time, target_time=30):
    # 计算执行时间
    elapsed_time = int(end_time - start_time)
    # 如果执行时间小于x秒，等待到x秒
    if elapsed_time < target_time:
        for i in trange(target_time - elapsed_time, desc='等待中', unit='秒'):
            time.sleep(1)


def wps_webhook(data: Dict, doc_id: Text, username: Text, password: Text, debug=False):
    """
    调用WPS ChatFlow的Webhook接口
    :param data: 请求数据
    :param doc_id: 文档ID
    :param username: 用户名
    :param password: 密码
    """
    # 要发送POST请求的URL
    url = f'https://365.kdocs.cn/chatflow/api/v2/func/webhook/{doc_id}'
    # 设置请求头（这里指定了内容类型为JSON）
    headers = {
        'Content-Type': 'application/json',
        'origin': 'www.kdocs.cn'
    }
    # 尝试从环境变量中获取用户名和密码
    if not username:
        username = os.getenv("WPS_CHATFLOW_USERNAME")
    if not password: 
        password = os.getenv("WPS_CHATFLOW_PASSWORD")
    # 发送POST请求
    response = requests.post(url, data=json.dumps(data), headers=headers, auth=(username, password))
    # 检查请求是否成功
    if response.status_code == 200:
        # 解析并打印响应内容（假设服务器返回了JSON格式的响应）
        response_data = response.json()
        if debug:
            print('响应数据:', response_data)
    else:
        # 打印错误信息
        print('请求失败，状态码:', response.status_code, '响应内容:', response.text)


def read_from_txt(txt: Text, keys: Dict):
    """
    从txt文件中读取数据
    :param txt: 文件
    :param keys: 字段名
    """
    with open(txt, "r", encoding='utf-8') as f:
        for line in f:
            splits = line.strip().split('\t')
            yield {k: v for k, v in zip(keys, splits)}


def read_from_excel(xlsx: Text, keys: Dict):
    """
    从excel文件中读取数据
    :param xlsx: 文件
    :param keys: 字段名
    """   
    df = pd.read_excel(xlsx)
    for _, row in df.iterrows():
        yield {k: row[k] for k in keys}


def task_field_optimization():
    """ 字段优化 """
    # 提示词
    prompt = f"任务：给定一个故障模式的描述，给出对应的故障演练方法。" \
              "要求：" \
              "1.严格以json格式输出，描述要简洁明确，返回字段包括准备阶段、操作方法、验证内容、恢复阶段；" \
              "2.演练方法要可执行，操作步骤要清晰，涉及到描述程度时应给出经验数值；" \
              "以下是json格式的描述内容：\n"
    # 实例化一个ChatBot对象
    bot = ChatBot()
    # 读取数据
    keys = ["所属层级", "对象/资源", "故障模式", "触发步骤"]
    for row in read_from_excel("./bd_qianfan/data.xlsx", keys):
        # 打印日志
        print("-" * 100)
        print(">" * 50)
        print(json.dumps(row, ensure_ascii=False, indent=4))
        # 调用模型咨询
        ans = bot.ask(prompt + json.dumps(row), debug=False)
        # 处理返回结果中的列表
        for k, v in ans.items():
            if isinstance(v, list):
                ans[k] = "\n".join(f"{i+1}. {item}" for i, item in enumerate(v))
        # 打印日志
        print("<" * 50)
        print(json.dumps(ans, ensure_ascii=False, indent=4))
        ans.update(row)
        ans.pop("触发步骤")
        wps_webhook(ans, "", username="", password="")


def task_gen_content():
    """ 故障演练方案生成 """
    # 提示词
    prompt = "任务：给定一个故障模式的标题，生成故障演练方法等相关信息。\n" \
             "要求：\n" \
             "1.严格以json格式输出，描述简洁明确。如果返回字段的值，是一个带序号的列表形式，请处理好换行。\n" \
             "2.如果存在多种原因可能导致此故障发生，请选择最准确、最合适的故障演练方法。\n" \
             "3.返回字段包括演练方法标题，用于简要描述故障演练的执行方法，最好是一个短语或一句话。\n" \
             "4.返回字段包括准备阶段、执行阶段、验证阶段、恢复阶段，用于描述实施故障演练的四个阶段。演练方法要可执行，操作步骤要清晰，涉及到描述程度时应给出经验数值。\n" \
             "5.返回字段包括监控、告警、日志，用于描述故障发生时，应当记录或感知到哪些信息。\n" \
             "6.返回字段包括影响面评估，用于描述实际生产环境中故障发生时，可能影响到哪些点。\n" \
             "7.返回字段包括恢复和应对手段，用于指导实际生产环境中故障发生后，应该如何快速科学的止损恢复。\n" \
             "8.返回字段包括实验名称、实验描述，用于映射到ChaosBlade或ChaosMesh的混沌工程实验；如果不存在，请自行撰写。\n" \
             "以下是json格式的输入：\n"
    # 实例化一个ChatBot对象
    bot = ChatBot()
    # 读取数据
    keys = ["所属层级", "对象/资源", "故障模式"]
    for row in read_from_excel("./bd_qianfan/data.xlsx", keys):
        # 打印日志
        print("-" * 100)
        print(">" * 50)
        print(json.dumps(row, ensure_ascii=False, indent=4))
        # 调用模型咨询
        ans = bot.ask(prompt + json.dumps(row), llm="kimi", debug=False)
        # 打印日志
        print("<" * 50)
        print(json.dumps(ans, ensure_ascii=False, indent=4))
        # 处理返回结果中的列表
        for k, v in ans.items():
            if isinstance(v, list):
                if any(isinstance(item, str) and item.startswith("1. ") for item in v):
                    ans[k] = "\n".join(v)
                else:
                    ans[k] = "\n".join(f"{i+1}. {item}" for i, item in enumerate(v))
        row.update(ans)
        wps_webhook(row, "", username="", password="")


if __name__ == '__main__':
    task_gen_content()
