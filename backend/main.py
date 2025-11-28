from flask import Flask, send_file
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api 
from flask_cors import CORS
from flask import jsonify, request, make_response
from werkzeug.exceptions import HTTPException
import json
from ultralytics import YOLO
from PIL import Image
from io import BytesIO
from werkzeug.utils import secure_filename
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import torch
import os
from roboflow import Roboflow
# Setting up componenets.............................................................................
# main app
app = Flask(__name__)
CORS(app)
# basic database overview
# # database
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+"backend\database_file"+"\my_app.db"
# db = SQLAlchemy(app)
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     email = db.Column(db.String(30), unqiue=True)
#     user_name = db.Column(db.String(50), unqiue=True)
#     password = db.Column(db.String(20))
# class DiscussionForum(db.Model):
#     user_id = db.Column(db.Integer, db.ForeingKey(User.id))
#     discussion_id = db.Column(db.Integer, primary_key=True, autoinrement=True)

# Validations
class NotFoundError(HTTPException):
    def __init__(self, status_code):
        self.response = make_response("", status_code)

class PostValidationErorr(HTTPException):
    def __init__(self, status_code, erorr_code, error_message):
        message = {"eror_code": erorr_code, "error_message": error_message}
        self.response = make_response(json.dumps(message), status_code)


# Controllers
@app.route("/", methods=["GET"])
def home():
    return "Hello World!!!"


# @app.route("/upload/<crop_name>", methods=["POST"])
# def upload_crop_image(crop_name):
@app.route("/upload/<crop_name>", methods=["POST"])
def upload_crop_image(crop_name):
    # after dataset is acquired, then use if else to take in    different crop_names
    if 'file' not in request.files:
        raise PostValidationErorr(status_code=404, erorr_code ="BE1003", error_message="Image file is not uploaded")
    img = request.files['file']
    print(img.filename, img.content_type)
    if crop_name.lower() == "bhindi":
        model = YOLO("pretrained_models/bhindi.pt")
    elif crop_name.lower() == "gourd":
        model = YOLO("pretrained_models/gourd.pt")
    else:
        model = YOLO("pretrained_models/best.pt") 
    print(model.__class__.__name__.split(".")[-1])

    img = Image.open(BytesIO(img.read()))
    
    # # res = model.predict(img, save=True, save_crop=True, project="runs/detect", name="predict", exist_ok=True)
    # # res = model.predict(img, save=True, project="runs/detect", name="predict", exist_ok=True)
    # # C:/Users/MENGDE/Desktop/Plant Disease Detection/backend
    # save_path = "C:/Users/MENGDE/Desktop/Plant Disease Detection/backend/runs/detect"
    # res = model.predict(source=img, save=True, project=save_path, name="predict", exist_ok=True)
    res = model.predict(source=img)
    crop = create_annotated_img(res, img)
    # return crop
    if len(res[0].boxes) > 0:
        class_label = res[0].names[res[0].boxes.cls.cpu().numpy()[0]]
        confidence = res[0].boxes.conf.cpu().numpy()[0]
        total_spots = len(res[0].boxes)
        result = {
            "class_label": class_label, 
            "confidence": float(confidence),
            "total_spots": total_spots
        }
    else:
        result = {"error": "No detection found"}

    # Return the result as JSON
    return jsonify(result)
    # return "Model works"

def create_annotated_img(res, img):
    boxes = res[0].boxes
    # image_path = "rust11.jpg"  # Replace with the path to your original image

    # Load the original image
    # original_image = Image.open(img)

    # Convert the image to a NumPy array
    image_np = np.array(img)

    # Create a figure and axes
    fig, ax = plt.subplots(1)

    # remove x and y axis ticks
    ax.set_xticks([])  # Remove X-axis ticks
    ax.set_yticks([])  # Remove Y-axis ticks

    # Display the original image
    ax.imshow(image_np)

    # Accessing attributes from the Boxes object
    xyxy = boxes.xyxy.cpu().numpy()
    conf = boxes.conf.cpu().numpy()
    cls = boxes.cls.cpu().numpy()

    # Iterate through the bounding boxes and plot them on the image
    for i in range(len(xyxy)):
        x, y, x_max, y_max = xyxy[i]
        box_width = x_max - x
        box_height = y_max - y
        confidence = conf[i]
        class_label = cls[i]

        # Create a Rectangle patch
        rect = patches.Rectangle((x, y), box_width, box_height, linewidth=1, edgecolor='r', facecolor='none')

        # Add confidence and class labels as text
        # ax.text(x, y, f'Class: {class_label}, Conf: {confidence:.2f}', color='r')
        ax.text(x, y, f'{res[0].names[class_label]}, {confidence:.2f}', bbox=dict(facecolor='orange', alpha=1, pad=0.7), color='w')

        # Add the patch to the Axes
        ax.add_patch(rect)
    save_path = "C:/Users/MENGDE/Desktop/Plant Disease Detection/backend/images/1.jpg"  # Replace with the desired save path
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)
    # Show the plot
    # plt.show()
    
    return "owKS"

@app.route("/result", methods=["GET"])
def get_result():
    # C:\Users\MENGDE\Desktop\Plant Disease Detection\backend\images
    image_path = "C:/Users/MENGDE/Desktop/Plant Disease Detection/backend/images/1.jpg"  # Replace with the actual path to your image

    # Check if the image file exists
    if os.path.exists(image_path):
        print("yes")
        return send_file(image_path, mimetype='image/jpeg')
    else:
        raise NotFoundError(404)
# # Api
# api = Api(app)
# api.add_resource

@app.route("/upload/new_model/<crop_name>", methods=["POST"])
def upload_new(crop_name):
    if 'file' not in request.files:
        raise PostValidationErorr(status_code=404, erorr_code ="BE1003", error_message="Image file is not uploaded")
    img = request.files['file']
    print(img.filename, img.content_type)
    # model = YOLO("pretrained_models/best.pt") 
    # print(model.__class__.__name__.split(".")[-1])

    img = Image.open(BytesIO(img.read()))

    img.save("uploaded_image.jpg")

    rf = Roboflow(api_key="oV1vcdh3l6saK5uHx664")
    if crop_name.lower() == "eggplant":
        project = rf.workspace().project("egg_plant")
    elif crop_name.lower() == "potato":
        project = rf.workspace().project("potato-disease-cw1hc")
    elif crop_name.lower() == "corn":
        project = rf.workspace().project("corn-and-maize-disease-dataset")
    model = project.version(1).model
    
    # infer on a local image
    print(model.predict("uploaded_image.jpg", confidence=40, overlap=30).json())
    res = model.predict("uploaded_image.jpg", confidence=40, overlap=30)
    # print(res)
    crop = create_annotated_img_roboflow(res, img)
    # print(res)
    
    #model.predict("uploaded_image.jpg", confidence=40, overlap=30).save("prediction.jpg")
    
    # infer on an image hosted elsewhere
    # print(model.predict("URL_OF_YOUR_IMAGE", hosted=True, confidence=40, overlap=30).json())
    
    result = extract_prediction_info(res)

    # Return the result as JSON
    return jsonify(result)

def extract_prediction_info(res):
    if not res or not res.predictions:
        return None

    class_labels = []
    confidences = []

    for prediction in res.predictions:
        class_labels.append(prediction['class'])
        confidences.append(prediction['confidence'])

    total_spots = len(res.predictions)

    # Assuming you want the most confident prediction
    max_confidence_index = np.argmax(confidences)
    class_label = class_labels[max_confidence_index]
    confidence = confidences[max_confidence_index]

    result = {
        "class_label": class_label,
        "confidence": float(confidence),
        "total_spots": total_spots
    }

    return result


def create_annotated_img_roboflow(res, img):
    # Convert the image to a NumPy array
    image_np = np.array(img)

    # Create a figure and axes
    fig, ax = plt.subplots(1)

    # remove x and y axis ticks
    ax.set_xticks([])  # Remove X-axis ticks
    ax.set_yticks([])  # Remove Y-axis ticks

    # Display the original image
    ax.imshow(image_np)

    # Iterate through the PredictionGroup (assuming it behaves like a list)
    for prediction in res:
        x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
        confidence = prediction['confidence']
        class_label = prediction['class']

        # Create a Rectangle patch
        rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')

        # Add confidence and class labels as text
        ax.text(x, y, f'{class_label}, {confidence:.2f}', bbox=dict(facecolor='orange', alpha=1, pad=0.7), color='w')

        # Add the patch to the Axes
        ax.add_patch(rect)

    save_path = "C:/Users/MENGDE/Desktop/Plant Disease Detection/backend/images/1.jpg"  # Replace with the desired save path
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

    return "owKS"

# def create_annotated_img_roboflow(res, img):
#     # Convert the image to a NumPy array
#     image_np = np.array(img)

#     # Create a figure and axes
#     fig, ax = plt.subplots(1)

#     # remove x and y axis ticks
#     ax.set_xticks([])  # Remove X-axis ticks
#     ax.set_yticks([])  # Remove Y-axis ticks

#     # Display the original image
#     ax.imshow(image_np)

#     # Iterate through the PredictionGroup (assuming it behaves like a list)
#     for prediction in res:
#         x, y, width, height = prediction['x'], prediction['y'], prediction['width'], prediction['height']
#         confidence = prediction['confidence']
#         class_label = prediction['class']

#         # Adjust the coordinates based on the image size
#         x *= image_np.shape[1] / float(prediction['image']['width'])
#         y *= image_np.shape[0] / float(prediction['image']['height'])
#         width *= image_np.shape[1] / float(prediction['image']['width'])
#         height *= image_np.shape[0] / float(prediction['image']['height'])

#         # Create a Rectangle patch
#         rect = patches.Rectangle((x, y), width, height, linewidth=1, edgecolor='r', facecolor='none')

#         # Add confidence and class labels as text
#         ax.text(x, y, f'{class_label}, {confidence:.2f}', bbox=dict(facecolor='orange', alpha=1, pad=0.7), color='w')

#         # Add the patch to the Axes
#         ax.add_patch(rect)

#     save_path = "C:/Users/MENGDE/Desktop/Plant Disease Detection/backend/images/1.jpg"  # Replace with the desired save path
#     plt.savefig(save_path, bbox_inches='tight', pad_inches=0)

#     return "owKS"





if __name__ == "__main__":
    # db.create_all()
    app.run(debug=True)