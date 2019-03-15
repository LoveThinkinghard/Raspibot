# Raspibot

A robot dased on raspiberry pi who can see, listen, speak, chat, face recognition, remember face and send email

## 这是什么？

一个用树莓派做的会聊天，能人脸识别（支持云台追踪）和发送邮件的小玩具，我称之为小派  

## 它怎么工作？

1.程序运行后，首先进入睡眠模式，可以使用关键词或人脸唤醒它；  
2.唤醒后它，如果它认识你会叫出你的名字，并向你问好（如果不认识你，会询问你的名字，然后记住（或许可以吧:），并给指定邮箱发送附有照片的邮件），然后就可以跟它聊天了（支持VAD，也就是没有固定录音时间）；  
3.当它看不见人脸并且有一定时间没有声音，它会再次进入睡眠模式（想停止只能强行关闭进程）。

## 背后的技术(python)

视频获取：opencv（也可以使用picamera，见[人脸识别](https://blog.csdn.net/yonglisikao/article/details/82288757)）  
人脸识别：python库——face_recognition（离线）  
语音识别与语音合成：百度云语音（在线）  
聊天对话：图灵机器人（在线）  
云台控制：自己设计的土方法  
关键词检测：snowboy  
语音端点检测（VAD）:webrtcvad + github上找的代码  
邮件发送：python自带支持，代码主要参考廖雪峰老师的  

## 实现

### 硬件

树莓派，USB带麦摄像头(webcam)，音箱（3.5mm）

### 需要安装的python库

（建议你[虚拟环境](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001432712108300322c61f256c74803b43bfd65c6f8d0d0000)里安装，方便包的管理）  
opencv, numpy, dlib, face_recognition, webrtc, baidu-aip等（实际运行如果还需要什么，可以根据`报错提示`和各种`搜索引擎`安装相应的包）

### 具体实现

人脸识别：https://blog.csdn.net/yonglisikao/article/details/82288757  
聊天：https://blog.csdn.net/yonglisikao/article/details/82314512  
云台控制：https://blog.csdn.net/yonglisikao/article/details/82318626  
其他：我感觉主要是snowboy配置的时候有点麻烦，反正我不能直接用官方编译的库（so文件），非得自己再编译一下，不过官方也有[教程](http://docs.kitt.ai/snowboy/)

### （代码）文件解释

（顾名思义就好，个人感觉名字起的都挺直观的）  

总体结构：  
1.together.py是主程序，其他都是库  
2.说实话，multiProcess.py才是真正的主程序（我也不知道together.py存在的价值是什么:( 对，我使用了多进程）  
3.其他py文件都是库，除了snowboydecoder.py（snowboy官方提供的），其他文件都像它们的名字一样好理解  
4.temp.wav是暂时存放的语音文件，每次都会换  

## 其他注意事项

代码里的密钥，密码什么的我都改了一下，可以到相应的官网申请，都是免费的。  

时间：2018年8月

