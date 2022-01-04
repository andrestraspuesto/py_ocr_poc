FROM python:3.9.9-slim-buster
RUN apt-get update && apt-get install -y --no-install-recommends \
    poppler-utils \
    tesseract-ocr \
    python3-opencv

RUN pip install --upgrade pip
RUN pip install \
    pandas \
    numpy\ 
    scikit-learn \
    pdf2image \
    pytesseract \
    opencv-python 

WORKDIR /usr/src/app
