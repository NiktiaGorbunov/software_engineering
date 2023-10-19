import cv2
import face_recognition
from PIL import Image, ImageDraw
import pickle

import training_models
def create_user():
    # name = input("Name user: -> ")
    # password = input("Password:  -> ")

    #training_models.take_screenshot('nikita')

    #training_models.train_model_py_img('nikita')
    pass

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
            print(f"Match found! {match}")
        else:
            print("ACHTUNG")



def main():
    #create_user()

    while True:
        answer = int(input("Есть сигнал? (1/0)"))
        if answer == 1:
            user_verification()







if __name__ == '__main__':
    main()
