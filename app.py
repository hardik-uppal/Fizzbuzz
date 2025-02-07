from flask import Flask, request, jsonify
from transformers import AutoProcessor, CLIPSegForImageSegmentation
import requests
from io import BytesIO
import torch
from PIL import Image

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    url = data.get("url")
    prompts = list(data.get("text").split(","))
    if len(prompts) > 10:
        prompt = prompts[:10]
        raise Warning("Too many prompts, only using the first 10")

    # Define the paths to the model and processor
    model_path = "/app/models/model"
    processor_path = "/app/models/processor"

    processor = AutoProcessor.from_pretrained(processor_path)
    model = CLIPSegForImageSegmentation.from_pretrained(model_path)

    # Download the image from the URL
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))

    # Preprocess the image and the text
    inputs = processor(
        text=prompt, images=[image] * len(prompt), padding=True, return_tensors="pt"
    )

    outputs = model(**inputs)

    # Postprocess the outputs
    logits = outputs.logits
    predictions = logits.sigmoid()  # Apply sigmoid to convert logits to probabilities
    thresholded_predictions = (
        predictions > 0.5
    ).int()  # Apply a threshold to get binary mask

    # Convert your processed results into a list or any structure you desire
    results = thresholded_predictions.tolist()

    # Create a response object
    response = {
        "message": "Inference completed",
        "predictions": results,
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
