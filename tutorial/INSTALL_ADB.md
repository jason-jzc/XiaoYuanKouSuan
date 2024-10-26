# 文档说明：
  本教程用于介绍如何为不同平台安装ADB命令  

# 在Ubuntu中安装ADB命令
## 1.更新软件源：
  ```bash
  sudo apt update
  ```
## 2.安装ADB和fastboot：
  ```bash
  sudo apt install android-tools-adb android-tools-fastboot -y
  ```
## 3.启动adb服务：
  ```bash
  sudo adb start-server
  ```  
  当看见如下信息时，说明adb安装成功  
  ![image](/pic/adb_startserver.png)  

# 适用于所有GNU/Linux中的ADB安装方法：
## 1.下载Google提供的ADB包：
  [官方下载地址（需要魔法）](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)  
  选择对应平台包下载，如果不出意外下载的为一个zip包，解压缩后，打开文件目录，会看到名为platform-tools的文件夹，将该文件夹放到一个固定的目录下，例如：/opt/ 中
## 2.添加环境变量
  在命令行（终端）中输入：  
  ```bash
  echo 'export PATH=$PATH:/opt/platform-tools' >> ~/.bashrc
  ```  
  其中的/opt/platform-tools为存放platform-tools文件夹的路径，如果为其他路径，请自行修改。  
  执行完成后，输入命令：  
  ```bash
  source ~/.bashrc
  ```  
  命令执行完成后，即可在命令行中直接使用adb命令。  
## 3.启动ADB服务
  在命令行中输入：  
  ```bash
  adb start-server
  ```

# 在windows中安装ADB命令：
## 1.下载Google提供的ADB包：
  [官方下载地址（需要魔法）](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)  
  选择对应平台包下载，如果不出意外下载的为一个zip包，解压缩后，打开文件目录，会看到名为platform-tools的文件夹，将该文件夹放到一个固定的目录下，例如：C:\Users\ 中
## 2.添加环境变量
  请自行搜索，此处不再赘述
## 3.启动ADB服务
  在命令行中输入：  
  ```bash
  adb start-server
  ```
# 在MacOS中安装ADB命令：
## 方法一（推荐）：
### 1.更新源：
  在终端中输入：
  ```bash
  brew update
  ```
### 2.安装：
  在终端中输入：
  ```bash
  brew install android-platform-tools
  ```
### 3.启动ADB服务：
  在终端中输入：
  ```bash
  adb start-server
  ```

## 方法二：
### 1.下载Google提供的ADB包：
  [官方下载地址（需要魔法）](https://developer.android.com/tools/releases/platform-tools?hl=zh-cn)  
  选择对应平台包下载，如果不出意外下载的为一个zip包，解压缩后，打开文件目录，会看到名为platform-tools的文件夹，将该文件夹放到一个固定的目录下，例如：/opt/ 中
### 2.添加环境变量
  请自行搜索，此处不再赘述
### 3.启动ADB服务
  在命令行中输入：  
  ```bash
  adb start-server
  ```

# 下载资源：
  如果上述下载地址无法访问，请前往[附件](/annex/README.md)下载所需文件


[下一步](/tutorial/GET_ROOT.md)  

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)