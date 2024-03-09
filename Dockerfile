# Start with the official Python image
FROM python:3.8-slim

# Install NGINX
RUN apt-get update && apt-get install -y nginx \
    gcc \
    libc-dev \
    git \
    # Add any other dependencies required by diffusers or other libraries
    && rm -rf /var/lib/apt/lists/*
# Set the working directory in the container
WORKDIR /app
# Install dependencies
# Ensure pip is up to date
RUN pip install --upgrade pip
# Install the transformers and diffusers library
RUN pip install transformers diffusers
RUN pip install --no-cache-dir torch torchvision torchaudio

RUN mkdir -p /app/models
RUN python -c "from transformers import CLIPSegForImageSegmentation, AutoProcessor; \
    processor = AutoProcessor.from_pretrained('CIDAS/clipseg-rd64-refined'); processor.save_pretrained('/app/models/processor'); \
    model = CLIPSegForImageSegmentation.from_pretrained('CIDAS/clipseg-rd64-refined'); model.save_pretrained('/app/models/model');"

# Copy the current directory contents into the container at /app
COPY . /app
# Make start.sh executable
RUN chmod +x /app/start.sh
# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install psutil
RUN pip install --trusted-host pypi.python.org -r requirements.txt -v

# Remove the default NGINX configuration
RUN rm /etc/nginx/sites-enabled/default

# Copy a new configuration file into the NGINX sites-enabled directory
COPY nginx.conf /etc/nginx/sites-enabled/

# Expose port 80 to the outside world
EXPOSE 80

# Start NGINX and Gunicorn from a shell script
CMD ["./start.sh"]
