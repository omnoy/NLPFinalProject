
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense , Embedding, SimpleRNN
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical


class sentiment_analysis_model:
    sentiment_text = ['positive', 'negative', 'neutral']

    def __init__(self, tokenizer, max_length, y_train=[0,1,2], epochs=10, batch_size=256, save=True,path:str=None):
        self.epochs = epochs
        self.batch_size = batch_size
        self.save = save

        self.model = Sequential()
        self.model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=512, input_length=max_length))
        self.model.add(SimpleRNN(32, return_sequences=True))
        self.model.add(SimpleRNN(16))
        self.model.add(Dense(3, activation='sigmoid'))

        self.reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=3, min_lr=0.0001)

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        self.one_hot_labels = to_categorical(y_train, num_classes=3)

        self.accuracy = 0

        if path:
            self.model.load_weights(path)

    def fit(self, padded_sequences_train):
        self.model.fit(padded_sequences_train, self.one_hot_labels, epochs=self.epochs, batch_size=self.batch_size,
                       callbacks=[self.reduce_lr])

        if self.save:
            self.model.save_weights("sentiment_analysis_model_weights.h5")

    def test(self,validation, padded_sequences_validation):
        predictions = self.model.predict(padded_sequences_validation)

        accuracy_size = 0
        accuracy = 0

        for idx, (val, text) in enumerate(validation):
            accuracy_size += 1
            sorted_predictions = sorted(enumerate(predictions[idx]), key=lambda x: x[1], reverse=True)

            if sorted_predictions[0][0] == val:
                accuracy += 1
        self.accuracy = accuracy / accuracy_size

        print(f"Accouracy: {self.accuracy}")

    def predict(self,texts,padded_sequences):
        predictions = self.model.predict(padded_sequences)

        result = []

        for idx, (t) in enumerate(texts):
            sorted_predictions = sorted(enumerate(predictions[idx]), key=lambda x: x[1], reverse=True)
            result.append({"text":t,"sentiment":sorted_predictions[0][0]})

        return result
