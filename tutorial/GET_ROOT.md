# 文档说明：
  本教程为手机或模拟器获取root权限的教程，作者使用的是安装了LineageOS的小米8se，安卓版本为13  

<br><br>

# 免责声明（请务必仔细阅读！）：
  接下来的操作可能对手机或模拟器的系统造成不可逆的改变，请确保你已经备份好数据！<br>
  且如果出现了任何损失，作者概不负责！<br>

<br><br>

>[!WARNING]
>接下来的操作将会使系统处于不安全的状态，并且及有可能造成数据不可逆的丢失！<br>
>请确保你已经了解风险，并确定造成的任何损失都是可以接受的！<br>
>请再次确认是否已经了解以上内容，并确定是否继续！<br>

<br><br>

# 操作步骤：
## 0.写在最前面：
  如果使用实体机，请确认手机已经解锁，并确认手机数据已经备份！<br>
  运行如下命令以连接手机/模拟器：
  ```bash
  adb devices
  ```
  如果返回类似如下的信息，则表示连接成功：
  ![image](/pic/adb_devices.png)<br>

## 1.获取boot镜像：
  首先到系统的设置中获取当前系统版本，并找到同版本系统的刷机包，获取boot.img镜像，如下图<br>
  ![image](/pic/boot_img.png)<br>
  将boot.img上传到目标手机/虚拟机（利用如下命令）：<br>
  ```bash
  adb push boot.img /sdcard
  ```
  将boot.img替换成对应的boot镜像路径

## 2.安装Magisk:
  前往[Magisk官网](https://github.com/topjohnwu/Magisk/releases)或从[附件]()中下载Magisk.apk，并在命令行中输入：
  ```bash
  adb install Magisk.apk
  ```
  请将Magisk.apk替换为下载的Magisk安装包的文件名<br>
  部分系统可能需要在手机/虚拟机上确认安装<br>
## 3.修补boot.img:
  打开Magisk（如下图）<br>
  ![image](/pic/Magisk_main_page.png)<br>
  点击“安装”按键（如下图）<br>
  ![image](/pic/Magisk_install_page.png)<br>
  绝大多数系统没有“直接安装”这一选项，如果有，选择“直接安装”即可，如果没有，请选择“选择并修补一个文件”（如下图）<br>
  ![image](/pic/Magisk_chosen_file.png)<br>
  找到boot.img文件，然后点击“开始”即可<br>
  等待修补完成，可以看到如下图<br>
  ![image](/pic/Magisk_patch_done.png)<br>
  记住输出的路径，并在电脑上输入如下命令：
  ```bash
  adb pull /sdcard/Download/patched-boot.img
  ```
  将 /sdcard/Download/patched-boot.img 替换成输出的路径，即可获得修补后的boot.img文件<br>
  然后输入命令（这将使手机/模拟器重启）：
  ```bash
  adb reboot bootloader
  ```
  等待手机/模拟器启动，可能会显示fastboot字样，此时命令行（终端）输入如下命令：
  ```bash
  fastboot flash patched-boot.img
  ```
  将patched-boot.img替换成修补后的boot镜像名称<br>
  替换结束后，终端输入命令（这将使手机/模拟器重启）：
  ```bash
  fastboot reboot
  ```

[下一步](/tutorial/INSTALL_MITMPROXY_CA.md)  

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)