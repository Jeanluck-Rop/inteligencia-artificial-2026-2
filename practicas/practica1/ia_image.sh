#!/bin/bash

# Nombre de la imagen
IMAGE_NAME="ia-python"

#!/bin/bash
if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
    echo "Building Docker Image..."
    docker build -t $IMAGE_NAME .
else
    echo "Docker Image already exist..."
    read -p "Do you want to rebuild it? (y/n): " choice
    if [[ "$choice" == "y" || "$choice" == "Y" ]]; then
        echo "Removing old image..."
        docker rmi -f $IMAGE_NAME
        echo "Rebuilding Docker Image..."
        docker build -t $IMAGE_NAME .
    else
        echo "Using existing image."
    fi
fi

echo "Running Container..."
docker run -it --rm -v "$(pwd)":/app $IMAGE_NAME bash --rcfile <(echo 'PS1="[\u@\h \W (Python-Docker)] > "')
