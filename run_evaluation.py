import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import glob
import pandas as pd
import os
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('./keras_model4.h5')

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
pred_answer=[]

# Replace this with the path to your image
for i, pic_name in enumerate(sorted(glob.glob('./test/*.*'))):
    print (pic_name + ' testing\n')
    image = Image.open(pic_name)

#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
    image_array = np.asarray(image)


    # display the resized image
    #image.show()

# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

# Load the image into the array
    data[0] = normalized_image_array

# run the inference
    pred_matrix=[]
    prediction = model.predict(data)
    pred_matrix = prediction[0]
    max = -1
    max_i = -1
    for i,a in enumerate(pred_matrix):
        if pred_matrix[i] > max:
            max = pred_matrix[i]
            max_i = i
    print('answer_label : ',max_i)
    pred_answer.append(max_i)

#answer_check_accuracy
pred_test = pd.read_csv("./test_solution.csv", names =['answer'])
sol_frame=pred_test['answer']
sol_list = []
for i in sol_frame:
    sol_list.append(i)

count = 0
for i,label_num in enumerate(sol_list):
    if label_num == pred_answer[i]:
        count += 1

print('test_accuracy :', round(count/75*100,5))

# batchsize 16 epochs : 50 learning rate 0.001 78.666
# batchsize 32 epochs : 50 learning rate 0.001 78.666
# batchsize 32 epochs : 50 learning rate 0.01  66.666
# batchsize 32 epochs : 100 learning rate 0.001 73.333
# batchsize 16 epochs : 100 learing rate 0.0005 73.333