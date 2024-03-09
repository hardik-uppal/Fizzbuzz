# CLIPSeg Inference Service Project

## Overview
In this project, we leverage the sophisticated capabilities of CLIP segmentation to innovate within the domain of human clothing datasets, utilizing the comprehensive and well-curated mattmdjaga/human_parsing_dataset for fine-tuning and enhancing model performance. By deploying a Docker service, we establish a robust and consistent environment to evaluate CLIP segmentation's effectiveness accurately. Through meticulous exploratory data analysis, we identify key dataset characteristics, including class distribution and spatial biases, informing our strategy for data augmentation. This analysis empowers us to tailor our augmentation techniques, addressing dataset imbalances and biases effectively. By doing so, we not only refine the dataset for improved model training outcomes but also set the stage for more nuanced and accurate segmentation models. 

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

### Further ideas
Building on our project, we can extend our exploration into the realm of virtual try-on applications, envisioning a sophisticated annotation pipeline that leverages systems akin to CLIP segmentation. By harnessing the power of diffusion models, we can advance towards creating a seamless virtual try-on experience, where users can visualize clothing items on  Gen-AI avatars or themselves in real-time with exceptional accuracy. 
[StableVITON](https://github.com/rlawjdghek/StableVITON)
[OOTDiffusion](https://github.com/levihsu/OOTDiffusion)
