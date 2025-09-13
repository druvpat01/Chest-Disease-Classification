import os
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from classifier.utils.utils import decodImage
from classifier.pipeline.prediction import PredictionPipeline


# initializing flask
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)
CORS(app)


class ClientApp:
    def __init__(self):
        self.img_path = 'inputImage.jpg'
        self.classifier = PredictionPipeline(self.img_path)


# landing page
@app.route("/", methods=['GET'])
@cross_origin
def home():
    return render_template('index.html')

# training the model 
@app.route("/train", methods=['GET', 'POST'])
@cross_origin
def trainRoute():
    # running the entire pipeline using DVC 
    os.system("dvc repro")
    return "Training Done Successfully! "

# prediction
@app.route("/predict", methods=['POST'])
@cross_origin
def predictRoute():
    image = request.json['image']
    decodImage(image, clapp.img_path)
    result = clapp.classifier.predict()
    return jsonify(result)




if __name__ == '__main__':
    clapp = ClientApp()
    app.run(host='0.0.0.0', port=8080, debug=True)