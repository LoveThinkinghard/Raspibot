# coding=utf-8
import multiprocessing
import tulingRobot
import faceRecog
import snowBoy
import time

def face_chat():
    # when face over, chat will over
    event = multiprocessing.Event()

    tuling_chat = multiprocessing.Process(target=tulingRobot.chat, args=(event,))
    tuling_chat.daemon = True
    tuling_chat.start()
    print('chat begin...')

    thread_face_recog = multiprocessing.Process(target=faceRecog.face_quit, args=(event,))
    thread_face_recog.daemon = True
    thread_face_recog.start()
    print('face detecting...')

    tuling_chat.join()
    thread_face_recog.terminate()
    print('chat over...')

    return


def watch_listen():
    # watching and listening
    while True:
        event = multiprocessing.Event()

        listen = multiprocessing.Process(target=snowBoy.listen, args=(event,))
        listen.daemon = True
        listen.start()
        print('listening...')

        watch = multiprocessing.Process(target=faceRecog.watch, args=(event,))
        watch.daemon = True
        watch.start()
        print('watching...')

        event.wait()
        print('waited')
        listen.terminate()
        watch.terminate()
        print('terminated')
        time.sleep(1.24)
        face_chat()
        print('chat over here')
        time.sleep(1.24)

# face_chat()
