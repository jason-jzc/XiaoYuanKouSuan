# 文档说明：
  本教程用于介绍如何为手机/模拟器安装mitmproxy的CA证书<br>

# 安装教程：
## 0.写在前面：
  接下来的操作如果是MIUI/HayperOS等基于AOSP的国产魔改系统，可能会失败，建议使用原生系统或者类原生系统（作者使用的是类原生的LineageOS-Android13）<br>
  接下来的操作可能会破坏你的系统，请谨慎操作！<br>
  该教程参考了[mitmproxy官方文档](https://docs.mitmproxy.org/stable/concepts-certificates/)<br>

## 1.下载安卓根证书并hash转码：
### 1.0.写在前面：
  我的[附件](/annex/README.md)中存放了已经通过hash转码的证书文件，如果你不是为了学习一些技能，可以直接下载，跳过‘下载安卓根证书并安装’这一步骤，直接进入下一步[‘获取并hash转码mitmproxy证书’](#get_mitmproxy_ca)<br>
  接下来的操作需要openssl，如果电脑中没有openssl，请自行搜索如何安装openssl（通常GNU/Linux和MacOS自带）
### 1.1.下载安卓根证书：
  <a name="download_ca"></a>

  前往[证书网站](https://www.cacert.org/index.php?id=3)，你将会看见如下图所示的界面：<br>
  ![image](/pic/CA_mainpage.png)<br><br>
  下载Class1和Class3的PEM格式的证书（下载DER格式的也可以，就是接下来的步骤会有一定的不同）<br>
  你将会得到如下的两个文件：<br>
  ![image](/pic/rootCA1.png) ![image](/pic/rootCA2.png)<br>
  如果无法打开证书的网站，可以前往我的[附件](/annex/README.md)中下载<br>
### 1.2.将证书转为hash格式：
  在终端中进入下载根证书的目录，并执行如下命令：
  ```bash
  openssl x509 -inform PEM -subject_hash_old -in root_X0F.crt | head -1
  ```
  你将会获得一串hash值，如下图<br>
  ![image](/pic/openssl_hash1.png)<br>
  请复制该hash值，如果不出意外，你的hash值应该与我相同。<br><br>
  >[!NOTE]
  >该命令中‘PEM’参数代表证书格式，正如我在[1.1章节](#download_ca)中提到的，如果你下载的是DER格式的证书，请将该参数修改为‘DER’。<br>
  >其中'root_X0F.crt'为证书的名称，下文中出现类似'证书名称'的文字，均修改该文件名。
  <br><br>

  然后在当前目录下创建一个以上述hash值加‘.0’（点零），的文本文档（如下图）。<br>
  ![image](/pic/openssl_hash2.png)<br>
  然后以文本文档打开’root_X0F.crt‘，复制其中的所有内容到hash值加‘.0’（点零）的文本文件中。<br>
  >[!TIP]
  >GNU/Linux系统用户可以直接使用命令：<br>
  >cat root_X0F.crt > 5ed36f99.0
  <br>

  上述操作完成后，在命令行中输入：<br>
  ```bash
  openssl x509 -inform PEM -text -in root_X0F.crt -noout >> 5ed36f99.0
  ```
  >[!NOTE]
  >该命令中‘PEM’参数代表证书格式，正如我在[1.1章节](#download_ca)中提到的，如果你下载的是DER格式的证书，请将该参数修改为‘DER’。<br>

  然后请对另一个根文件重复执行如上步骤，并将证书名称改为另一个证书的名称。<br>
  如果不出意外，你将会获得类似如下的文件，并且hash值与我相同<br>
  ![image](/pic/openssl_hash3.png)<br>
  将这两个转码后的文件保留备用<br>

## 2.获取并hash转码mitmproxy证书：
<a name="get_mitmproxy_ca"></a>

### 2.1.获取证书
  在命令行中输入以下命令，用于获取证书：<br>
  ```bash
  mitdump
  ```
  此时你可能还是找不到证书，因为mitmproxy将证书放到了你的用户目录下，它有可能是一个隐藏文件夹。<br>
  如果是GNU/Linux或MacOS系统，隐藏目录通常在 ~/ 目录下，名为 .mitmproxy 的文件夹。<br>
  在Windows系统中，可以通过文件管理器搜索 .mitmproxy 来查找该文件夹。<br>

  >[!TIP]
  >如果真的找不到，可以设置电脑的代理为127.0.0.1端口8080（如何设置请自行搜索），然后打开浏览器输入mitm.it，你将会看见证书的下载界面，下载安卓的证书文件。（作者未尝试，无法确认是否可行，详细教程请参考[官方文档](https://docs.mitmproxy.org/stable/concepts-certificates/)）
  <br><br>

  打开文件夹你将看见如下文件：<br>
  ![image](/pic/mitmproxy_ca_list.png)<br>
  那么恭喜你，可以距成功又近一步了<br>

### 2.2.hash转码证书：
  终端打开 .mitmproxy 文件夹，输入如下命令：<br>
  ```bash
  openssl x509 -inform PEM -subject_hash_old -in mitmproxy-ca.pem | head -1
  ```
  <br>

  >[!TIP]
  >如果通过浏览器下载的证书，请将文件名称改为浏览器下载的文件名
  <br>

  命令执行后将会获得一串hash值，请复制该hash值，并在当前目录下创建一个以 hash值+‘.0’（点零） 的文件，例如：‘c8750f0d.0’ 并以文本形式打开，将 mitmproxy-ca.pem 文件中的内容复制进去，保存。<br>

  >[!TIP]
  >GNU/Linux系统用户可以直接使用命令：<br>
  >cat mitmproxy-ca.pem > hash值+‘.0’（点零）
  <br>

  然后在终端中输入：<br>
  ```bash
  openssl x509 -inform PEM -text -in mitmproxy-ca.pem -noout >> hash值+‘.0’（点零）
  ```
  <br>

  将得到的转码后的文件与根证书的两个文件放到一起，留着备用<br>
  如果没有报错，那么恭喜你，你距离成功更近了！<br>


## 3.安装证书：
### 3.0.写在最前面：
  你已经坚持到了这里，说明你真的很想要尝试，那么就继续吧！<br>
  这一步结束，你就完成了所有困难的部分了，胜利就在眼前！<br>
  接下来的操作很多都要在手机/模拟器上完成<br>
### 3.1.解锁System分区：
  这部分的内容，如果是经常玩刷机的，应该不陌生，毕竟解锁了 /system 分区才算真正的root手机了<br>

  >[!NOTE]
  >本教程中的解锁分区教程并不能适用于所有版本的安卓系统，仅供参考
  <br>

  还记得当时root的时候安装的Magisk吗？<br>
  没错，我们还要继续用它，只不过这次是利用它的平台，去安装一些工具<br>

  前往[magisk-overlayfs](https://github.com/HuskyDG/magic_overlayfs/releases)的下载界面，下载最新版的overlayfs的压缩包<br>

  >[!TIP]
  >如果无法打开网站，可以前往我的[附件](/annex/README.md)中下载压缩包
  <br>

  将下载好的压缩包传到手机上（使用如下命令）：<br>
  ```bash
  adb push ./magisk-overlayfs-release.zip /sdcard
  ```
  <br>

  将‘./magisk-overlayfs-release.zip’替换成你下载的压缩包的文件名<br>

  打开手机的Magisk软件，可以看到右下角有个‘模块’按键<br>
  选择‘从本地安装’，然后找到刚才传到手机上的压缩包<br>
  在弹出来的窗口选择‘确认安装’<br>
  你将看到输出的很多日志，当看到最后一行出现‘Done’字样的时候，证明安装成功了（如下图）<br>
  ![image](/pic/overlayfs_ok.png)<br>

  此时点击重启按键，手机将重启<br>
  如果正常重启了，那么恭喜你，已经成功解锁了 /system 分区<br>
### 3.2.安装证书到系统：
  重启的过程中，没有必要一直等着，这时候可以准备下一步<br>
  前往[MT管理器的官网](https://mt2.cn/)下载MT管理器的安装包，并使用如下命令安装到手机上<br>
  如果无法下载，可以前往我的[附件](/annex/README.md)下载<br>
  ```bash
  adb install mt2.apk
  ```
  其中 ‘mt2.apk’ 替换成你的文件名，部分系统需要手机确认<br>
  安装成功后，打开MT管理器，此时可能会弹出一个root权限授权窗口，点击允许，然后将会看见如下图的界面<br>
  ![image](/pic/MT_mainpage.png)<br>

  此时，将准备好的三个转码的证书文件通过如下命令传入手机：<br>

  ```bash
  adb push ./5ed36f99.0 /sdcard # 根证书1
  adb push ./e5662767.0 /sdcard # 根证书2
  adb push ./hash值+‘.0’ /sdcard # 转码后的mitmproxy证书文件
  ```
  <br>

  然后在MT管理器中，轻滑左侧目录，点击上面的路径，输入‘/sdcard’，即可进入手机的/sdcard目录<br>
  然后轻滑右侧目录，点击上面的路径，输入‘/system/etc/security/cacerts’，即可进入手机的/system/etc/security/cacerts目录<br>
  然后长按左侧目录中转码后的证书文件，在弹出的菜单中（如下图），选择 ‘复制->’：<br>
  ![image](/pic/copy_ca.png)<br>
  此时右侧刚刚复制过去的证书文件将会是绿色的字体，长按复制过去的文件，在弹出的菜单中选择‘属性’，此时你将看到该文件的属性细节（如下图）<br>
  ![image](/pic/detail_ca.png)<br>
  如果权限、所有者和用户组图像中不同，则改为与图示相同<br>
  然后对剩余两个证书文件重复上述操作<br>
  都完成后，重启手机<br>

### 3.3 验证证书安装是否成功：
  打开手机设置，找到“安全”，找到“更多安全设置”，选择“加密与凭据”，进入“信任的凭据”，选择“系统”，向下滑动，找到“mitmproxy”，检查是否开启（如下图），如果未开启，请手动开启<br>
  ![image](/pic/check_installed.png)<br>

<br>
<br>

恭喜你，你已经完成了所有的配置，可以准备香槟了！

<br>
<br>

  


[最后一步，准备使用](/tutorial/GET_READY.md)
  

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)