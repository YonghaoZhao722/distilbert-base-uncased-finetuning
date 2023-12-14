# DistilBERT Sentiment Analysis

This repository contains a DistilBERT model fine-tuned using the Hugging Face Transformers library on the IMDb movie review dataset. The model is designed for sentiment analysis, enabling the determination of sentiment polarity (positive or negative) within text reviews.

## Contents

- `dataset/`: Contains scripts or code related to dataset handling and processing.
- `pretrained/`: **(Please manually download and place the `pytorch_model.bin` file here from [this link](https://huggingface.co/distilbert-base-uncased/resolve/main/pytorch_model.bin?download=true)**)
- `training/`: Includes scripts used for fine-tuning and training the DistilBERT model.
- `examples/`: Demonstrates how to utilize the trained model for sentiment analysis.

## Pretrained Model

Please download the pre-trained model `pytorch_model.bin` from the following link and place it inside the `pretrained/` folder: [Download Model](https://huggingface.co/distilbert-base-uncased/resolve/main/pytorch_model.bin?download=true)

## Usage

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd distilbert-sentiment-analysis
