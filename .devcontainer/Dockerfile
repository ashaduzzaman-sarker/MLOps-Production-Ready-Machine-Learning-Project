# Use a base image with Python 3.9 or higher
FROM mcr.microsoft.com/vscode/devcontainers/python:3.9

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    cmake \
    libopencv-dev \
    python3-opencv \
    git \
    wget \
    curl \
    vim

# Install Python dependencies for NLP and Computer Vision
RUN pip install --upgrade pip
RUN pip install numpy pandas matplotlib seaborn \
    tensorflow pytorch torchvision torchaudio \
    transformers datasets spacy nltk \
    opencv-python scikit-learn

# Install Jupyter for interactive notebooks
RUN pip install jupyterlab

# Install other useful tools like DVC, MLflow for MLOps
RUN pip install dvc[azure] mlflow

# Set the working directory in the container
WORKDIR /workspace
