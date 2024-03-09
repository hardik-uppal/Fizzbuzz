# CLIPSeg Inference Service Project

## Overview

This project sets up a Docker-based inference service using the CLIPSegForImageSegmentation model from CIDAS/clipseg-rd64-refined, aimed at processing image segmentation with a focus on clothing in human images. The setup includes an NGINX server to handle multiple parallel incoming requests efficiently.

## Why CLIPSegForImageSegmentation?

The CLIPSegForImageSegmentation model is chosen for its exceptional ability to understand both textual prompts and visual inputs, making it highly suitable for detailed segmentation tasks like clothing on humans. The use of this model aligns with our project's goal to explore data segmentation in fashion and improve understanding of different clothing types.

## Setup Instructions

### Prerequisites

- Docker installed on your system.

### Building the Docker Image

1. Clone the repository and navigate to the project directory.
2. Build the Docker image using the following command:

```shell
docker build -t clipseg_inference_service .
