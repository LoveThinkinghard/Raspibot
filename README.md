# Raspibot
A robot dased on raspiberry pi who can see, listen, speak, chat, face recognition, remember face and send email
## 这是什么？
一个用树莓派做的会聊天，能人脸识别（支持云台追踪）和发送邮件的小玩具，如果非得有个名字，我会叫它小派  
## 它怎么工作？
1.程序运行后，首先进入睡眠模式，可以使用关键词或人脸唤醒它；  
2.唤醒后它，如果它认识你会叫出你的名字，并向你问好（如果不认识你，会询问你的名字，然后记住（或许可以吧:），并给指定邮箱发送附有照片的邮件），然后就可以跟它聊天了（支持VAD，也就是没有固定录音时间）；  
3.当它看不见人脸并且有一定时间没有声音，它会再次进入睡眠模式（想停止只能强行关闭进程）。
## 背后的技术(python)
视频获取：opencv（我知道picamera跟轻巧，但出于某种原因我没用）  
人脸识别：python库——face_recognition（离线）  
语音识别与语音合成：百度云语音（在线）  
聊天对话：图灵机器人（在线）  
云台控制：自己设计的土方法  
关键词检测：snowboy  
语音端点检测（VAD）:webrtcvad + github上找的代码  
邮件发送：python自带支持，代码主要参考廖雪峰老师的  
## 感觉还不错，想自己做一个？
Good, let me tell you how!
### 硬件
树莓派，USB带麦摄像头(webcam)，音箱（3.5mm）
### 需要安装的python库
（当然，建议你在虚拟环境里面安装）  
opencv, numpy, dlib, face_recognition, webrtc, baidu-aip...（emmm 时间久远有点记不得了，具体的去代码里找吧:)，问题不大）  
### 具体实现
人脸识别：https://blog.csdn.net/yonglisikao/article/details/82288757  
聊天：https://blog.csdn.net/yonglisikao/article/details/82314512  
云台控制：https://blog.csdn.net/yonglisikao/article/details/82318626  
其他：我感觉主要是snowboy配置的时候有点麻烦，反正我不能直接用官方编译的库（so文件），非得自己再编译一下，不过官方也有教程，我就不说了啊
## 其他注意事项
代码里的密钥，密码什么的我都改了一下（第一次上传的时候，把自己邮箱密码都传上去了，唉，搞了半天），要用你自己的哦，反正都是免费的。
## 最后
祝你好运，制作之路肯定困难重重，但是不要轻易放弃，当你最后成功的时候，你会发现：you are so great！  

