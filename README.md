# Python-getting-started

一个简单的使用 Flask 的 Python 应用。
可以运行在 LeanEngine Python 运行时环境。

## 使用命令行工具创建项目

请参考 [LeanCloud 命令行工具](https://leancloud.cn/docs/leanengine_cli.html) 文档。
目前 LeanCloud 命令行工具暂不支持 python 3.5 项目的创建。


## 手动创建项目

首先确认本机已经安装 [Python](http://python.org/)3.5 运行环境。然后执行下列指令：

```
$ git clone git@github.com:leancloud/python-getting-started.git
$ cd python-getting-started
```

准备启动文件:

```
$ touch start.sh
$ chmod +x start.sh
```

将 app id 等信息输入到 `start.sh` 文件中：

```
export LC_APP_ID=<your app id>
export LC_APP_KEY=<your app key>
export LC_APP_MASTER_KEY=<your master key>
export LC_APP_PORT=3000

python3 wsgi.py
```

启动项目：

```
$ ./start.sh
```

应用即可启动运行：[localhost:3000](http://localhost:3000)

## 部署到 LeanEngine


部署到测试环境：
```
$ lean deploy
```

部署到生产环境：
```
$ lean publish
```

## 相关文档

* [LeanEngine 指南](https://leancloud.cn/docs/leanengine_overview.html)
* [Python SDK 指南](https://leancloud.cn/docs/leanstorage_guide-python.html)
* [Python SDK API](https://leancloud.readthedocs.io/zh_CN/latest/)
* [命令行工具详解](https://leancloud.cn/docs/leanengine_cli.html)
* [LeanEngine FAQ](https://leancloud.cn/docs/faq_list.html)


