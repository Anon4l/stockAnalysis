from distutils.log import debug
import torch
from transformers import pipeline,AutoTokenizer, AutoModelForSequenceClassification



def get_sentiment(query):
    output = []
    tokenizer = AutoTokenizer.from_pretrained("ProsusAI/finbert")
    model = AutoModelForSequenceClassification.from_pretrained("ProsusAI/finbert")
    classifier = pipeline("sentiment-analysis",model = model,tokenizer = tokenizer)
    for(i,n) in enumerate(query):
        res = classifier(n)
        output.append({"news":n,"sentiment":res})
    
    return output;
