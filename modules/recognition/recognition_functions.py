import cv2
import face_recognition
from PIL import Image, ImageDraw
import pickle
import keyboard
import asyncio
from random import randint
from modules.recognition import training_models

def create_user(name):
    training_models.take_screenshot(name)
    training_models.train_model_py_img(name)


def user_verification():
    data = pickle.loads(open('dataset/users_pickles/nikita_encodings.pickle','rb').read())
    cap = cv2.VideoCapture(0)

    # "Прогреваем" камеру, чтобы снимок не был тёмным
    for i in range(30):
        cap.read()


    ret, image = cap.read()# Делаем снимок
    cap.release() #отключаем камеру

    locations = face_recognition.face_locations(image)
    encodings = face_recognition.face_encodings(image, locations)

    for face_encoding, face_location in zip(encodings, locations):
        result = face_recognition.compare_faces(data["encodings"], face_encoding)
        match = None

        if True in result:
            match = data['name']
            return (True, match)
        else:
            return (False, match)