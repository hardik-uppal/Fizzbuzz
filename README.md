# CLIPSeg Inference Service Project

## Overview

This project sets up a Docker-based inference service using the [CLIPSegForImageSegmentation: CIDAS/clipseg-rd64-refined](https://huggingface.co/CIDAS/clipseg-rd64-refined) model, aimed at processing image segmentation with a focus on clothing in human images. The setup includes an NGINX server to handle multiple parallel incoming requests efficiently.

## Why CLIPSegForImageSegmentation?

The CLIPSegForImageSegmentation model is chosen for its exceptional ability to understand both textual prompts and visual inputs, making it highly suitable for detailed segmentation tasks like clothing on humans. The use of this model aligns with our project's goal to explore data segmentation in fashion and improve understanding of different clothing types. The model can be found on Hugging Face at the following link: [CLIPSegForImageSegmentation](https://huggingface.co/CIDAS/clipseg-rd64-refined).

## Setup Instructions

### Prerequisites

- Docker installed on your system.
- python
- requirements.txt

### Building the Docker Image

1. Clone the repository and navigate to the project directory.
2. Build the Docker image using the following command:

```shell
docker build -t clipseg_inference_service .
docker run -p 80:80 clipseg_inference_service
```

### Making Requests to the Service
A [Jupyter notebook](https://github.com/hardik-uppal/Fizzbuzz/blob/main/demo_notebook.ipynb) is provided to demonstrate how to send POST requests to the container endpoint and receive responses. The notebook, InferenceRequestsDemo.ipynb, contains examples of interacting with the inference service. Another file [demo.py](https://github.com/hardik-uppal/Fizzbuzz/blob/main/demo.py) for insuring multiple requests work.

```shell
python demo.py
```

### Dataset
This project uses the human parsing dataset available on [Hugging Face: Human Parsing Dataset](https://huggingface.co/datasets/mattmdjaga/human_parsing_dataset). This dataset is crucial for our exploration and improvement efforts on the CLIPSeg model's segmentation capabilities regarding clothing.