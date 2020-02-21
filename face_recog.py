import pickle
import cv2
import argparse
import face_recognition
import imutils
from imutils.video import VideoStream
from imutils import paths
import os


def train_face_recog_model(dataset, method="cnn"):
    # parser=argparse.ArgumentParser()
    # parser.add_argument("-i", "--dataset", required=False)
    # parser.add_argument("-e","--encoding", required=False)
    # parser.add_argument("-m", "--method", required=False, default="cnn")
    # args=vars(parser.parse_args())

    imagepaths=list(paths.list_images(dataset))
    known_name=[]
    known_encoding=[]

    for i, image in enumerate(imagepaths):
    #    print(os.path.sep) [-2])
        name=image.split("/")[-2]
        gambar=cv2.imread(image)
        rgb=cv2.cvtColor(gambar, cv2.COLOR_BGR2RGB)
  
        boxes=face_recognition.face_locations(rgb, model=method)
        #    print(boxes)
        encodings=face_recognition.face_encodings(rgb,boxes)
        #    print(encodings)

        for encoding in encodings:
            known_encoding.append(encoding)
            known_name.append(name)
        print(known_name)
    
    data = {"encodings": known_encoding, "names": known_name}

    with open("tukulsa_admin.pickle", "wb") as c:
        pickle.dump(data,c)

    return "PROSES SELESAI"

print(train_face_recog_model("dataset"))

