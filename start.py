# This is a demo of running face recognition on a Raspberry Pi.
# This program will print out the names of anyone it recognizes 
# to the console and send alert to admin in case of intruder.

# To run this you will need 
# 1) Raspberry Pi
# 2) Pi Camera V2 module


import time
from time import sleep
import cv2
import numpy as np
import glob
import os
import dlib
import time
os.environ['PYGAME_HIDE_SUPPORT_PROMPT']="hide"
import pygame
from gpiozero import MotionSensor

pygame.mixer.init()
pygame.mixer.music.load("Audio.mp3")

pir = MotionSensor(4)
print("Hello Coders!!")
print("Initializing the model in...")
sleep(2)
print("3")
sleep(2)
print("2")
sleep(2)
print("1")
sleep(2)

print("WELCOME TO AI INTELLIGENT CAMERA")

def motion_detected():

    while True:
        pir.wait_for_motion()
        return True

def main(video_capture, saved_face_descriptor, names, detect_faces, predictor, face_rec):
    start_time = time.time()
    while ((time.time() - start_time) < 10.1):
        # Grab a single frame from WebCam
    	ret, frame = video_capture.read()

    	# Find all the faces and face enqcodings in the frame
    	gray = cv2.cvtColor((frame), cv2.COLOR_RGB2GRAY)
    	faces = detect_faces.detectMultiScale(gray, 1.3,5)
    	
    	face_locations = []
    	for (x,y,w,h) in faces:
    		face_locations.append(dlib.rectangle(x, y, x+w, y+h))
    	
        # If there is atleast 1 face then do face recognition 
    	if (len(face_locations) > 0):
            for face_location in face_locations:
                face_encoding = predictor(frame, face_location)
                face_descriptor = face_rec.compute_face_descriptor(frame, face_encoding, 1)

                # See if the face is a match for the known face(s)
                match = list((np.linalg.norm(saved_face_descriptor - (np.array(face_descriptor)), axis=1)))
                val, idx = min((val, idx) for (idx, val) in enumerate(match))

                name = "Unknown"
                if (val < 0.6):
                	name = names[idx]

                print(name)
                # Save image for future use
                if name=="Unknown":
                    cv2.imwrite(os.path.join(os.getcwd(), "unknown", str(int(time.time()))+".png"), frame)
                    pygame.mixer.music.play()
                    os.system('python send_sms.py')
                    sleep(10)
                else:
                    return


if __name__ == '__main__':
    detect_faces = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
    predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
    face_rec = dlib.face_recognition_model_v1('dlib_face_recognition_resnet_model_v1.dat')

    video_capture = cv2.VideoCapture(0)
    video_capture.set(3, 320)
    video_capture.set(4, 240)

    saved_face_descriptor = []
    names = []

    for face in glob.glob(os.path.join(os.getcwd(), "face_encodings", "*.npy")):
    	temp = np.load(face)
    	saved_face_descriptor.append(temp)
    	names.append(os.path.basename(face[:-4]))
    
    while True:
        if (motion_detected()):
            main(video_capture, saved_face_descriptor, names, detect_faces, predictor, face_rec)

    video_capture.release()
