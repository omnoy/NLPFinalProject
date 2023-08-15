
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM, Embedding, SimpleRNN
from tensorflow.keras.callbacks import ReduceLROnPlateau
from tensorflow.keras.utils import to_categorical


class judges_detection_model:

    def __init__(self, judge_df, tokenizer, max_length, y_train, epochs=10, batch_size=256, save=True,path=None):
        self.epochs = epochs
        self.batch_size = batch_size
        self.save = save

        self.model = Sequential()
        self.model.add(Embedding(input_dim=len(tokenizer.word_index) + 1, output_dim=32, input_length=max_length))
        self.model.add(SimpleRNN(32, return_sequences=True))
        self.model.add(SimpleRNN(16))
        self.model.add(Dense(len(judge_df), activation='sigmoid'))

        self.reduce_lr = ReduceLROnPlateau(monitor='loss', factor=0.2, patience=3, min_lr=0.0001)

        self.model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

        self.one_hot_labels = to_categorical(y_train, num_classes=len(judge_df))
        self.y_train = y_train
        self.accuracy = 0

        if path:
            self.model.load_weights(path)

    def fit(self, padded_sequences_train):
        self.model.fit(padded_sequences_train, self.one_hot_labels, epochs=self.epochs, batch_size=self.batch_size,
                       callbacks=[self.reduce_lr])

        if self.save:
            self.model.save_weights("judges_detection_model.h5")

    def test(self,validation, padded_sequences_validation):
        predictions = self.model.predict(padded_sequences_validation)

        accuracy_size = 0
        accuracy = 0

        for idx, (judge, text) in enumerate(validation):
            accuracy_size += 1
            sorted_predictions = sorted(enumerate(predictions[idx]), key=lambda x: x[1], reverse=True)

            if sorted_predictions[0][0] == judge:
                accuracy += 1
        self.accuracy = accuracy / accuracy_size

        print(f"Accouracy: {self.accuracy}")

    def predict(self,texts,padded_sequences,judge_dict):
        predictions = self.model.predict(padded_sequences)

        result = []

        for idx, (text) in enumerate(texts):
            sorted_predictions = sorted(enumerate(predictions[idx]), key=lambda x: x[1], reverse=True)
            result.append({"text":text,"judge":judge_dict[sorted_predictions[0][0]]})

        return result