import os.path
import pickle
import sys
import cv2
import face_recognition

def train_model_py_img(name_user:str):

    if not os.path.exists(f"dataset/users_img/{name_user}"):
        print("[ERROR] three is no directory 'dataset/users_img/{name_user}'")
        sys.exit()

    known_encodings = []
    images = os.listdir(f"dataset/users_img/{name_user}")

    for i, image in enumerate(images):
        print(f"[+] processing img {i+1}/{len(images)}")
        print(image)

        face_img = face_recognition.load_image_file(f"dataset/users_img/{name_user}/{image}")
        face_enc = face_recognition.face_encodings(face_img)[0]

        if len(known_encodings) == 0:
            known_encodings.append(face_enc)
        else:
            for item in range(0, len(known_encodings)):
                result = face_recognition.compare_faces([face_enc], known_encodings[item])
                #print(result)

                if result[0]:
                    known_encodings.append(face_enc)
                    #print("Same person!")
                    break
                else:
                    #print("Another person")
                    break
    # print(known_encodings)
    # print(f"Length {len(known_encodings)} ")

    data = {
        "name": name_user,
        "encodings": known_encodings,
    }

    with open(f"dataset/users_pickles/{name_user}_encodings.pickle", "wb") as file:
        file.write(pickle.dumps(data))

    return f"[INFO] File {name_user}_encoding.pickle successfully created"


def take_screenshot(name_user: str):

    if not os.path.exists(f"dataset/users_img/{name_user}"):
        os.mkdir(f"dataset/users_img/{name_user}")

    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()  # возвращает True, если с кадром все ок
        fps = cap.get(cv2.CAP_PROP_FPS)  # получаем значение фпс и внутренних переменных
        multiplier = fps * 10  # как часто мы будем делать скриншот

        if ret:
            cv2.imshow("frame", frame)
            k = cv2.waitKey(20)  # регулирем скорость воспроизведения видео и что-то про клавиши

            if k == ord("s"):
                cv2.imwrite(f"dataset/users_img/{name_user}/{count}_screen.jpg", frame)  # сохраняем скриншоты
                print(f"Take a screenshot {count}_screen.jpg")
                count += 1
            elif k == ord('q') or count == 20:
                print("Q pressed, clossing the app")
                break

        else:
            break

    cap.release()
    cv2.destroyAllWindows()