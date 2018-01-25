# BingPhoto
不能上Google的日子里，都是bing陪伴我，一直觉得，每天早上打开bing的主页是，美如画的背景图片能带来一天的好心情，于是决定把bing的每日一图给爬下来，用作备用图库。

## 思路
使用chrome监听工具，发现bing的图片都是从[新浪App网站](https://area.sinaapp.com/bingImg/)上来的，用`urllib`的get请求，直接就获取了当日的图片。接下来的保存过程就轻而易举了。

## 用法
由于我加入了`Fire`CLI，可以直接在终端使用Fire语法获取图片：
```shell
python bing_photo.py --dirname 'your_dir_name'
```
默认为我的工作栈的当前路径。
**Have fun!**