# 免责声明：
  本项目仅供学习交流，不得用于商业用途，请遵守国家相应法规，不得用于非法用途！  
  如使用本项目出现任何问题，与项目作者无关！  
  本项目中如出现侵权内容，请联系作者删除！（E-MAIL:hello2022_jzc@yeah.net，TEL:13103166175）  

# 项目介绍：
  本项目基于python3.10+，使用mitmproxy拦包改包，修改答案，配合adb连续点击，以实现自动答题。  
  该项目致力于让所有人轻松使用该项目，并欢迎能力出众的人提交自己的想法，如果喜欢该项目，请给个star支持一下～  

# 目录结构：
    XiaoYuanKouSuan  
    |  
    |--README.md // 项目说明  
    |  
    |--adbManager.py // adb操作类  
    |  
    |--LICENSE // 许可证  
    |  
    |--main.py // 主程序  
    |  
    |--result.js // 数据提交中的js文件（该文件为抓包获得，可自行抓包查看）  
    |  
    |--bao  // 小猿口算数据包（该文件夹内的文件为小猿口算的html和js文件，可自行抓包）  
        |--english-words_.*\.js // 英语单词pk的js文件  
        |  
        |--english-word.html // 英语单词pk的html文件（可通过修改其中的js文件名称实现每次重新从服务端获取js文件）  
        |  
        |--exercise.js // 口算的js文件，该项目中修改的是该文件  
        |  
        |--exercise.html // 口算的html文件，与英语的html文件相同，可通过修改，从而重新获取js文件  
        |  
        |--pk_.*\.js // pk页面的js文件，其中包含英语pk和口算pk的控件，也可修改  
        |  
        |--pk.html // pk页面的html文件，与英语的html文件相同，可通过修改，从而重新获取js文件  
        |  
        |--css // 口算部分的样式文件目录  
            |--english-words\..*\.css // 英语单词pk的样式文件  
            |  
            |--exercise\..*\.css // 口算pk的样式文件  
            |  
            |--pk\..*\.css // pk页面的样式文件  
    |--pic // 介绍图片的目录
    |
    |--tutorial // 教程目录
    |
    |--annex // 附录，其中包含了项目所需的安装包等依赖文件，如有侵权，请联系作者删除！

# 项目要求：
  1.拥有一台可以安装adb命令和python3.10+的电脑（作者使用的是Ubuntu24测试）  
  2.已通过pip安装mitmproxy模块  
  3.已经root的手机或模拟器，并且已经解锁了system分区（作者使用的是安装LineageOS20的小米8se）  

# 使用教程：
#### 1.下载该项目压缩包并解压缩
#### 2.为root的手机或模拟器安装mitmproxy证书（将证书通过hash转码以后安装到手机的/system/etc/security/cacerts 目录下）
#### 3.清除手机或模拟器中小猿口算的缓存
#### 4.启动mitmproxy，进入XiaoYuanKouSuan目录，在终端中输入命令：
    mitmdump -s ./main.py  
  [详细教程](/tutorial/README.md)

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理  
  ## E-MAIL:
  hello2022_jzc@yeah.net  