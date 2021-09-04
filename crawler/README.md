# 顶会论文爬虫

## THE COMPUTER VISION FOUNDATION

官方网站 [openaccess.thecvf.com](https://openaccess.thecvf.com)

### 爬取思路

* 点击官方网站链接👆
* 选择您需要查看的年份, 点击`Main Conference`链接
* 打开的链接中可以看到论文相关信息, 如标题、作者、链接等
* 解析页面元素, 依次将每条信息写入到日志文件中
* 根据日志中的论文信息, 逐篇对论文进行爬取下载

### 操作说明

#### 群晖下载

如果您手上有群晖, 或者其他NAS设备, 可以使用准备好的urls.txt文件方式来批量下载

* 登陆群晖系统, 打开`Download Station`软件
* 点击菜单栏上的`+`号按钮
* 设置`目的地文件夹`和`打开文件`, 选择本仓库中`CVPR20XX`下的txt文件, 点击确认开始下载
* Enjoy >_<

#### 手动下载

* 执行`thecvf.py`或`thecvf.ipynb`文件, 进入命令行交互模式
* 输入`crawler`后点击回车, 实现论文信息爬取
* 输入`download`后点击回车, 开始下载论文

```
输入 help 或者 ? 查看帮助。

thecvf>help

Documented commands (type help <topic>):
========================================
clean  crawler  download  exit  help

thecvf>crawler
thecvf>download
```

### Tips

* 历年论文信息已备好, 请查看年份对应文件夹下jsonl文件或txt文件
* 下载较慢, 且需要极大的磁盘存储空间, 请做好准备；）

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
