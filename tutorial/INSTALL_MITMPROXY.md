# 文档说明：
  本教程用于介绍如何安装mitmproxy

# 安装教程：
## 0.写在最前面：
  有的时候，python安装完不一定会安装pip（作者遇到过，但次数不多），所以，你可以先打开命令行（终端），输入以下命令  
  ```bash
  pip --version
  ```
  如果很幸运，输出了带有pip版本的信息（如下图），那么恭喜你，pip已经自动被安装了，那么你可以进行下一步了，否则这时候你应该前往互联网搜索pip的安装教程，然后再回来看我的教程。
  ![image](/pic/pip_version_out.png)
## 1.通过pip安装mitmproxy：
  #### 安装：
  在命令行（终端）中输入以下命令：  
    pip install mitmproxy  
  如果报错，可以尝试使用以下命令：  
    pip3 install mitmproxy  
  #### 常见问题：
  安装这个，一定要耐心，因为一些众所周知的网络原因，可能会下载失败，如果你会魔法，可以使用魔法上网。  
  或者你可以前往互联网，查询一下修改pip源的方法。   
## 3.尝试运行mitmproxy：
  在命令行（终端）中输入以下命令：  
  ```bash
  mitmproxy
  ``` 
  如果是Windows系统，可能无法运行，但是不用担心，你可以在命令行中输入以下命令：  
  ```bash
  mitmdump
  ```
  如果此时没有报错，看见了如下图的两种界面，那么恭喜你，mitmproxy已经安装成功了，可以开始下一步了。
  ![image](/pic/mitmproxy_out.png)  
  ![image](/pic/mitmdump_out.png)  

[下一步](/tutorial/INSTALL_ADB.md)
  

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)