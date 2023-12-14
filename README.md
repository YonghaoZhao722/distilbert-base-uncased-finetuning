# DistilBERT Sentiment Analysis

This repository contains a DistilBERT model fine-tuned using the Hugging Face Transformers library on the IMDb movie review dataset. The model is designed for sentiment analysis, enabling the determination of sentiment polarity (positive or negative) within text reviews.

The model is based on the paper [DistilBERT: a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108).

## Contents

- `dataset/`: Contains scripts or code related to dataset handling and processing.
- `pretrained/`: **(Please manually download and place the `pytorch_model.bin` file from the link below)**
- `predict.ipynb`: Notebook demonstrating the prediction process using the fine-tuned DistilBERT model.
- 
## Pretrained Model

Please download the pre-trained model `pytorch_model.bin` from the following link and place it inside the `pretrained/` folder: [Download Model](https://huggingface.co/distilbert-base-uncased/resolve/main/pytorch_model.bin?download=true)

## Usage

Run main.ipynb

## Predict

Run predict.ipynb
