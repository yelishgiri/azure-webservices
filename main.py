import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from azure.ai.vision.imageanalysis import ImageAnalysisClient
from azure.ai.vision.imageanalysis.models import VisualFeatures
from azure.core.credentials import AzureKeyCredential
load_dotenv()


app = Flask(__name__)
CORS(app)


try:
    endpoint = os.getenv("VISION_ENDPOINT")
    key = os.environ["VISION_KEY"]
except KeyError:
    print("Missing environment variable for vision endpoint and key")
    exit()

@app.route("/")
def index():
    return render_template("index.html")



@app.route("/generate_caption", methods=["POST"])
def generate_caption():
    if request.method == "POST":
        image = request.files["image"]
        image.save("images/imgfortest.jpg")

        client = ImageAnalysisClient(endpoint=endpoint, credential=AzureKeyCredential(key))

        with open("images/imgfortest.jpg", "rb") as image_stream:
            image_analysis = client.analyze(image_data=image_stream, visual_features=[VisualFeatures.CAPTION])

        os.remove("images/imgfortest.jpg")
        print("Image analysis results:")
        print("Caption:")
        if image_analysis.caption is not None:
            print(f" '{image_analysis.caption.text}', Confidence {image_analysis.caption.confidence:.4f}")

        return jsonify({"caption": image_analysis.caption.text, "confidence": image_analysis.caption.confidence})
    else:
        return jsonify({"error": "Invalid request method"}), 405



if __name__ == "__main__":
    app.run(debug=True)






