from keras.models import load_model
# from keras.preprocessing.image import load_img
from tensorflow.keras.utils import load_img
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np

from keras.models import load_model

model = load_model('final_model.h5')

image = load_img('j.jpg', target_size=(224, 224))
img = np.array(image)
img = img / 255.0
img = img.reshape(1,224,224,3)
label = model.predict(img)
print("Predicted value: ", label[0][0])
if (label>0.0001):
    print("swettha")
else:
    print("not swettha")


