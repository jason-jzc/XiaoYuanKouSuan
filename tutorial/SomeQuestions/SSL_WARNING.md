# 文档说明：
>## 文档类型：
>> 常见问题处理文档
>## 该文档用于解决：
>> 1.小猿口算提示无法上网<br>
>> 2.脚本运行时提示SSL握手错误<br>
>> 3.脚本运行时偶发404错误代码<br>
> ## 特别鸣谢：
>> pikaqiuKEAI 发现该问题

# 解决方法及步骤：
## 1.准备工作：
> 1. 前往[LSPosed](https://github.com/LSPosed/LSPosed/releases/tag/v1.9.2)官网，或者前往我的[附件](/annex/README.md)中下载类似于“zygisk-release.zip”的文件备用
> 2. 前往[JustTrustMe](https://github.com/Fuzion24/JustTrustMe/releases)官网，或者前往我的[附件](/annex/README.md)中下载“JustTrustMe.apk”的文件备用
## 2.操作步骤：
> 1. 首先将上述两个文件通过adb传入手机/模拟器的固定目录（方法在教程中有所提到，此处不再赘述）
> 2. 打开手机中的Magisk，并点击右上角的设置图标打开设置界面（如下图）
>![image](/pic/magisk_setting.png)<br>
> 3. 向下滑动，找到“Zygisk”开关并打开，然后重启手机/模拟器。
> 4. 重新启动后打开Magisk并进入模块管理界面，安装LSPosed的zip包，安装成功后重启手机/模拟器
> 5. 重启后进入系统，通过MT管理器找到"JustTrustMe.apk"文件并安装，安装成功后并不会出现应用图标，然后重启手机/模拟器
> 6. 重启后进入系统，下拉到通知栏，你将会看见“LSPosed已加载”的提示（如下图）
> ![image](/pic/LSPosedMsg.png)<br>
> 7. 正如信息所提示，点击该信息进入LSPosed的设置界面（如下图）
> ![image](/pic/LSPosedSetting.png)
> 8. 点击下方的拼图选项，你将会看见JustTrustMe模块，点击该模块进入该模块设置界面（如下图），并开启该模块。
> ![image](/pic/JustTrustMeSetting.png)<br>
> 9. 开启该模块后重启手机/模拟器
> 10. 重启后再次回到该模块设置界面，然后找到小猿口算并勾选。
> 11. 或许需要重启手机/模拟器
> ## 3.验证：
> 清除小猿口算缓存，然后启动脚本，再打开小猿口算，此时是否还有错误或警告，如没有，那么恭喜你，你解决了这个问题！

>[!NOTE]
> 如果你在安装JustTrustMe时遇到问题，可以下载并安装[TrustMeAlready](https://github.com/ViRb3/TrustMeAlready/releases/tag/v1.11)（我的[附件](/annex/README.md)中也有该文件）


# 联合开发：
  该项目欢迎大家参与，如果大家有更好的想法，欢迎大家提出贡献，作者会及时合并处理   
  >## E-MAIL:
  >hello2022_jzc@yeah.net  
  >## 贡献者：
  >* [jason-jzc](https://github.com/jason-jzc)