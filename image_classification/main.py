import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model('keras_model.h5')

with open('labels.txt', 'r') as f:
    class_names = f.read().splitlines()

image = Image.open('paper.jpg').resize((224, 224))
image_array = np.asarray(image) / 255.0
image_array = np.expand_dims(image_array, axis=0)

prediction = model.predict(image_array)
index = np.argmax(prediction)

print("You played:" , class_names[index])
print("Confidence:" ,round(prediction[0][index]*100, 2), "%")
