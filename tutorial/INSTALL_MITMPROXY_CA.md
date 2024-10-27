# 文档说明：
  本教程用于介绍如何为手机/模拟器安装mitmproxy的CA证书<br>

# 安装教程：
## 0.写在前面：
  接下来的操作如果是MIUI/HayperOS等基于AOSP的国产魔改系统，可能会失败，建议使用原生系统或者类原生系统（作者使用的是类原生的LineageOS-Android13）<br>
  接下来的操作可能会破坏你的系统，请谨慎操作！<br>
  该教程参考了[mitmproxy官方文档](https://docs.mitmproxy.org/stable/concepts-certificates/)，并参考了网上的教程<br>
## 1.下载安卓根证书并hash转码：
### 1.0.写在前面：
  我的[附件](/annex/README.md)中存放了已经通过hash转码的证书文件，如果你不是为了学习一些技能，可以直接下载，跳过‘下载安卓根证书并安装’这一步骤，直接进入下一步[‘获取并安装mitmproxy证书’](##2.获取并安装mitmproxy证书)<br>
  接下来的操作需要openssl，如果电脑中没有openssl，请自行搜索如何安装openssl（通常GNU/Linux和MacOS自带）
### 1.1.下载安卓根证书：
  前往[证书网站](https://www.cacert.org/index.php?id=3)，你将会看见如下图所示的界面：<br>
  ![image](/pic/CA_mainpage.png)<br><br>
  下载Class1和Class3的PEM格式的证书（下载DER格式的也可以，就是接下来的步骤会有一定的不同）<br>
  你将会得到如下的两个文件：
  ![image](/pic/rootCA1.png) ![image](/pic/rootCA2.png)<br>
### 1.2.将证书转为hash格式：
  在终端中进入下载根证书的目录，并执行如下命令：
  ```bash
  openssl x509 -inform PEM -subject_hash_old -in root_X0F.crt | head -1
  ```
  你将会获得一串hash值，如下图<br>
  ![image](/pic/openssl_hash1.png)<br>
  请复制该hash值，如果不出意外，你的hash值应该与我相同。<br><br>
  >[!NOTE]
  >该命令中‘PEM’参数代表证书格式，正如我在[1.1章节](###1.1.下载安卓根证书：)中提到的，如果你下载的是DER格式的证书，请将该参数修改为‘DER’。<br>
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
  >该命令中‘PEM’参数代表证书格式，正如我在[1.1章节](###1.1.下载安卓根证书：)中提到的，如果你下载的是DER格式的证书，请将该参数修改为‘DER’。<br>

  然后请对另一个根文件重复执行如上步骤，并将证书名称改为另一个证书的名称。<br>
  如果不出意外，你将会获得类似如下的文件，并且hash值与我相同<br>
  ![image](/pic/openssl_hash3.png)<br>
  将这两个转码后的文件保留备用<br>



## 2.获取并hash转码mitmproxy证书：
## 3.安装证书：




[下一步](/tutorial/INSTALL_ADB.md)
  

# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)