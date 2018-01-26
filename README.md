# BingPhoto
不能上Google的日子里，都是bing陪伴我，一直觉得，每天早上打开bing的主页是，美如画的背景图片能带来一天的好心情，于是决定把bing的每日一图给爬下来，用作备用图库。

## 思路
使用chrome监听工具，审查元素发现bing的图片都是从[Bing子网](https://cn.bing.com/az/hprichbg/rb/)上来的（后面加上当日图片的id），用`urllib`的get请求，直接就获取了当日的图片。接下来的保存过程就轻而易举了。

## 用法
由于我加入了`Fire`CLI，可以直接在终端使用Fire语法获取图片：
```shell
python bing_photo.py --dirname 'your_dir_name'
```
默认为我的工作栈的当前路径。

# 续
突然想到可以将bing的每日一图当作我的gp的背景图片，但是又不可能每天去git add commit push，而python又可以进行系统调用帮我执行这个重复性过程，好主意！

## 思路
1. 爬取bing每日一图的时候顺便保存一份名字为background.jpg的副本到我的Blog/img目录下，替换原来的背景图片。
2. 使用`subprocess`module进行git命令调用。
3. 使用`Apscheduler`module添加work flow定时执行。

## 用法
由于所有的代码都是跨平台的，直接执行`python commit_to_my_gp.py`脚本即可。
如果想要在后台运行（关闭终端窗口也能继续执行），需要使用Linux的`nohup &`命令，即`nouhp python commit_to_my_gp.py &`。

**Have fun!**