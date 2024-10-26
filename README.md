# XiaoYuanKouSuan
&lt;算法也是算> 小猿口算快速答题外挂

# 免责声明：
    本项目仅供学习交流，不得用于商业用途，请遵守国家相应法规，不得用于非法用途！  
    如使用本项目出现任何问题，与项目作者无关！  
    本项目中如出现侵权内容，请联系作者删除！（E-MAIL:hello2022_jzc@yeah.net，TEL:13103166175）  

# 项目介绍：
  本项目基于python3.10+，使用mitmproxy拦包改包，修改答案，配合adb连续点击，以实现自动答题。

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

# 项目要求：
  1.拥有一台可以安装adb命令和python3.10+的电脑（作者使用的是Ubuntu24测试）  
  2.已通过pip安装mitmproxy模块  
  3.已经root的手机或模拟器，并且已经解锁了system分区（作者使用的是安装LineageOS20的小米8se）  



