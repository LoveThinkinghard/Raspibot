# coding=utf-8
import requests
import json
import BaiduSdk
import vadSound
import faceRecog

def tuling(text='I said nothing'):
    # tuling Robot
    tuling_url = 'http://www.tuling123.com/openapi/api'
    tuling_date = {
        'key': '4527c40***********92cf020847be',
        'info': text
    }  # 当你申请了自己的图灵机器人后，请将key换为你自己的
    r = requests.post(tuling_url, data=tuling_date)
    # print(r.text)
    return json.loads(r.text)['text']


def chat(event):
    # chat with tuling Robot
    no_time = 0
    face = faceRecog.face_recog()
    name = True
    if not face:
        face = [' ']
    if BaiduSdk.text2sound('你好，'+face[0]+'。'):
        vadSound.play_sound()
    print('机器人：你好，'+face[0]+'。')
    if face == ['']:
        if BaiduSdk.text2sound('能告诉我你的名字吗？'):
            vadSound.play_sound()
        print('机器人：能告诉我你的名字吗？')
        name = False
    while True:
        if event.is_set() and no_time >= 4:
            break
        if vadSound.record_sound():
            print('语音识别中。。。')
            ret, content = BaiduSdk.sound2text()
        elif event.is_set():
            break
        else:
            continue

        if not content:
            no_time += 1
            continue
        if ret:
            if not name:
                name = content
                faceRecog.new_friend(name)
            print('你：' + content)
            no_time = 0
        else:
            vadSound.play_sound('resources/fail_STT.wav')
            print('机器人：语音识别出错[{}]'.format(content))
            no_time += 1
            continue

        if event.is_set() and content == '再见':
            if BaiduSdk.text2sound('再见。'):
                vadSound.play_sound()
            print('机器人：再见。')
            break

        tuling_text = tuling(content)
        print('机器人：{}'.format(tuling_text))

        if BaiduSdk.text2sound(tuling_text):
            vadSound.play_sound()
        else:
            vadSound.play_sound('resources/fail_TTS.wav')
            print('语音合成出错。。。')

    return


#the followings are used to debug
# chat()
#result = tuling('hello')
#print(result)
