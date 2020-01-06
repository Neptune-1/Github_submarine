from keras.models import model_from_json
from keras import optimizers
import cv2
import numpy as np
import PIL
import keras
from keras.applications.resnet50 import ResNet50,preprocess_input

from keras.preprocessing.image import load_img,img_to_array
from keras.applications.imagenet_utils import decode_predictions
import matplotlib.pyplot as plt

json_file = open("reset_imagenet_model_v2.json", "r")
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("reset_imagenet_model_v2.h5")




fish_n=['puffer','baracouta','goldfish', 'Carassius auratus',
'electric ray', 'crampfish', 'numbfish', 'torpedo',
'jellyfish',
'spiny lobster', 'langouste', 'rock lobster', 'crawfish', 'crayfish', 'sea crawfish',
'crayfish', 'crawfish', 'crawdad', 'crawdaddy'
'grey whale', 'gray whale', 'devilfish', 'Eschrichtius gibbosus', 'Eschrichtius robustus',
'eel',
'coho', 'cohoe', 'coho salmon', 'blue jack', 'silver salmon', 'Oncorhynchus kisutch',
'anemone','fish',
'sturgeon',
'gar', 'garfish', 'garpike', 'billfish', 'Lepisosteus osseus',
'lionfish',
'puffer', 'pufferfish', 'blowfish', 'globefish']

fish=0
cap = cv2.VideoCapture(0)
fish=0
font = cv2.FONT_HERSHEY_SIMPLEX

for i in range(1000):
    ret, im1 = cap.read()
    im = PIL.Image.fromarray(im1)
    
    
    im = im.resize((224,224) ,PIL.Image.ANTIALIAS)
    im = np.array(im)
    processed_image = preprocess_input(im.reshape(-1,224,224,3))
    predictions = loaded_model.predict(processed_image)
    label = decode_predictions(predictions)
    for name in fish_n:
        if name in str(label):
            fish=1
    if fish ==1:
        img = cv2.putText(im1,'Fish detected',(290,60), font, 2,(0,255,0),2,cv2.LINE_AA)
    else:
        img = cv2.putText(im1,'NOT',(290,60), font, 2,(0,0,255),2,cv2.LINE_AA)

    
    #img = cv2.circle(im,(112,112),50*fish,(0,0,0))
    cv2.imshow('b',img)
    cv2.waitKey(1)
    fish=0

