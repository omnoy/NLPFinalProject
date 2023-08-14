from transformers import AutoTokenizer, AutoModel, pipeline
tokenizer = AutoTokenizer.from_pretrained("avichr/heBERT_sentiment_analysis") #same as 'avichr/heBERT' tokenizer
model = AutoModel.from_pretrained("avichr/heBERT_sentiment_analysis")

class sentiment_analyzer:
    def __init__(self):
        self.sentiment_analysis = pipeline(
            "sentiment-analysis",
            model="avichr/heBERT_sentiment_analysis",
            tokenizer="avichr/heBERT_sentiment_analysis"
        )

    def get_analysis(self, text: str):

        return self.sentiment_analysis(text[:511])[0]['label']
