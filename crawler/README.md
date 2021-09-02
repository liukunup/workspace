# 顶会论文爬虫

## THE COMPUTER VISION FOUNDATION

官方链接 [openaccess.thecvf.com](https://openaccess.thecvf.com)

### 爬取思路

* 从menu.json文件读取待爬信息
* 依次爬取历年论文信息，如标题、作者、链接等，并写入到日志文件中
* 从日志文件中取得单篇论文信息，逐篇论文爬取

### Tips

* 已经为您配置好2013年至2021年的历年链接
* 已经爬取好论文信息，并保存到日志文件，仅需执行以下代码下载即可
* 下载较慢，且需要极大的磁盘存储空间，请做好准备

``` python
menu_list = list()
with open("menu.json", "r") as f:
    menu_list = json.load(f)
for item in menu_list:
    paper_path = item["path"]
    paper_jsonl = item["logfile"]
    with open(f"{paper_path}/{paper_jsonl}", "r") as f:
        lines = f.readlines()
        for l in lines:
            obj = json.loads(l)
            downloader(obj["pdf_url"], paper_path)
```

## 问题反馈
* 邮件 (liukunwlb#163.com, 把#换成@)
* 微信 liukun250596945

## 关于作者

``` javascript
var liukunup = {
  nickname  : "我的代码温柔如风",
  site : "http://liukunup.com"
}
```
