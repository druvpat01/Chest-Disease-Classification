import os
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image


class PredictionPipeline:
    def __init__(self, filename):
        self.img_path = filename    # the user loaded image

    def predict(self):
        # loading the trained model
        model = load_model(os.path.join('model', 'model.h5'))
        
        test_img = image.load_img(self.img_path, target_size=(224,224))

        test_img = image.img_to_array(test_img)
        test_img = np.expand_dims(test_img, axis=0)

        result = np.argmax(model.predict(test_img), axis=1)

        # as it is a binary classification
        if result == 1:
            prediction = 'Healthy'
            return[{'image': prediction}]
        else:
            prediction = 'Coccidiosis'
            return[{'image': prediction}]