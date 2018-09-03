# coding = utf-8
import face_recognition
import numpy as np
import cv2
import multiProcess
import time
import sys
import RPi.GPIO as GPIO
import sendEmail

ecodinglist = list(np.load('resources/ecodinglist.npy'))
namelist = list(np.load('resources/namelist.npy'))
x0, y0 = 80, 30

def setServoAngle(servo, angle):
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(servo, GPIO.OUT)
    pwm = GPIO.PWM(servo, 50)
    pwm.start(8)
    dutyCycle = angle / 18. + 3.
    pwm.ChangeDutyCycle(dutyCycle)
    time.sleep(0.3)
    pwm.stop()
    GPIO.cleanup()

def face_recog():
    # print("Capturing image.")
    sys.stdout.write('.')
    sys.stdout.flush()
    video_capture = cv2.VideoCapture(0)
    ret, pframe = video_capture.read()
    video_capture.release()
    frame = cv2.resize(pframe, (0, 0), fx=0.25, fy=0.25)

    output = frame[:, :, ::-1]
    # Find all the faces and face encodings in the current frame of video
    face_locations = face_recognition.face_locations(output)
    if face_locations:
        x = (face_locations[0][1] + face_locations[0][3])/2
        y = (face_locations[0][0] + face_locations[0][2])/2
        print(x, y)
    else:
        x, y = 80, 60
    dx = (80 - x) * 0.3125
    dy = -(60 - y) * 0.3125
    global x0, y0
    if abs(dx) >= 3:
        x0 += dx
        if x0 > 180:
            x0 = 180
        elif x0 < 0:
            x0 = 0
        setServoAngle(27, x0) # x
    if abs(dy) >= 3:
        y0 += dy
        if y0 > 180:
            y0 = 180
        elif y0 < 0:
            y0 = 0
        setServoAngle(17, y0)  # y
    face_encodings = face_recognition.face_encodings(output, face_locations)
    results = ['']*len(face_encodings)
    # Loop over each face found in the frame to see if it's someone we know.
    for i in range(len(face_encodings)):
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(ecodinglist, face_encodings[i], tolerance=0.38)

        if True in matches:
            first_match_index = matches.index(True)
            name = namelist[first_match_index]
            results[i] = name
        else:
            cv2.imwrite('New friends/emmmm.jpg', pframe)
    return results


def watch(event):
    """
    one of the main process: watching
    :return: None
    """
    while True:
        face = face_recog()
        if face:
            event.set()
            break
    return


def face_quit(event, times=3):
    # decide when to quit
    time.sleep(4.21)
    no_times = 0
    while True:
        if not face_recog():
            no_times += 1
        else:
            no_times = 0
            event.clear()
        if no_times >= times:
            event.set()

def new_friend(name):
    image = face_recognition.load_image_file('New friends/emmmm.jpg')
    face_locations = face_recognition.face_locations(image)
    face_encodings = face_recognition.face_encodings(image, face_locations)
    global ecodinglist, namelist
    ecodinglist.append(face_encodings[0])
    namelist.append(name)
    np.save('resources/ecodinglist.npy', ecodinglist)
    np.save('resources/namelist.npy', namelist)
    sendEmail.send_email(name)
    return
# face_recog()
