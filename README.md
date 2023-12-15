# DistilBERT Sentiment Analysis

This repository contains a DistilBERT model fine-tuned using the Hugging Face Transformers library on the IMDb movie review dataset. The model is designed for sentiment analysis, enabling the determination of sentiment polarity (positive or negative) within text reviews.

The model is based on the paper [DistilBERT: a distilled version of BERT: smaller, faster, cheaper and lighter](https://arxiv.org/abs/1910.01108).[![arXiv](https://img.shields.io/badge/Arxiv-1910.01108-b31b1b.svg?logo=arXiv)](https://arxiv.org/abs/1910.01108)

## 📝 Contents

- `dataset/`: Contains scripts or code related to dataset handling and processing.
- `pretrained/`: **(Please manually download and place the `pytorch_model.bin` file from the link below)**
- `predict.ipynb`: Notebook demonstrating the prediction process using the fine-tuned DistilBERT model.
  

## 🤗 Pretrained Model

Please download the pre-trained model `pytorch_model.bin` from the following link and move it to the `pretrained/` folder: [Download Model](https://huggingface.co/distilbert-base-uncased/resolve/main/pytorch_model.bin?download=true)

## 🔨 Preparation

To get started, clone the repository and navigate to the project directory:

```bash
git clone https://github.com/zyh040521/distilbert-base-uncased-finetuning
cd distilbert-base-uncased-finetuning
```

## 💡 Building the Environment

To set up the required environment, install the dependencies listed in the `requirements.txt` file using pip:

```bash
pip install -r requirements.txt
```

## 🌟 Usage

Run main.ipynb

## 😊 Predict

Run predict.ipynb

## 🔥 TODO
- Use the `evaluate` library to assess model accuracy
