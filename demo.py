# demo

import requests
import json
from PIL import Image
from io import BytesIO
import numpy as np
import hashlib

URL = "http://localhost/predict"


def process_request(data):
    # Ensure headers specify that you're sending JSON data
    headers = {"Content-Type": "application/json"}
    # Convert your data to JSON before sending

    response = requests.post(URL, headers=headers, data=json.dumps(data))
    # Debug: Print the status code and response text

    response_dict = json.loads(response.text)
    print("Response Text:", response_dict["message"], "for image:", data["url"])
    mask = np.array(response_dict["predictions"]).transpose(1, 2, 0)

    response = requests.get(data["url"])
    # create hexcode for image url
    img_url_bytes = data["url"].encode("utf-8")
    # Create a hash object and generate the hex code
    hex_code = hashlib.md5(img_url_bytes).hexdigest()

    original_image = Image.open(BytesIO(response.content)).convert("RGBA")
    # Get the width and height of the original image
    width = original_image.width
    height = original_image.height
    # Start with a transparent image
    colors = [
        (255, 0, 0, 128),  # Red
        (0, 255, 0, 128),  # Lime Green
        (0, 0, 255, 128),  # Blue
        (255, 255, 0, 128),  # Yellow
        (0, 255, 255, 128),  # Cyan
        (255, 0, 255, 128),  # Magenta
        (192, 192, 192, 128),  # Silver
        (128, 0, 128, 128),  # Purple
        (255, 165, 0, 128),  # Orange
        (0, 128, 0, 128),  # Dark Green
    ]
    composite = Image.new("RGBA", (width, height), (0, 0, 0, 0))
    num_classes = mask.shape[2]
    for i in range(num_classes):
        # Create a mask for the current class
        class_mask = mask[:, :, i]

        # Convert the class mask to a PIL image with the same color for all mask pixels
        overlay_color = Image.new("RGBA", (width, height), colors[i])

        # Convert the binary mask to an 8-bit grayscale image and then to 'L' mode
        mask_image = Image.fromarray((class_mask * 255).astype(np.uint8)).convert("L")
        mask_image = mask_image.resize(original_image.size)
        # Create a composite image with the current class's overlay
        composite = Image.composite(overlay_color, composite, mask_image)

    # Overlay the colored mask on the original image
    final_image = Image.alpha_composite(original_image, composite)
    # save th original image
    original_image.save(f"original_image_{hex_code}.png")
    # Save or display the final image
    final_image.save(f"final_image-{hex_code}.png")


if __name__ == "__main__":

    data_list = [
        {
            "url": "http://images.cocodataset.org/val2017/000000039769.jpg",
            "text": "cat, remote, blanket",
        },
        {
            "url": "https://media.wired.com/photos/5932743344db296121d6b359/master/w_1280,c_limit/6714960287_b8f2a8bd8e_b.jpg",
            "text": "person, hat, gloves, eyeglasses",
        },
        # {
        #     "url": "https://i.pinimg.com/564x/30/88/88/3088880ef60a8860d7cbd53c95d95fcd.jpg",
        #     "text": "person, car, road, boots",
        # },
    ]
    # create a multiprocessing pool to concurrently process the requests
    from multiprocessing import Pool

    with Pool(3) as p:
        p.map(process_request, data_list)
