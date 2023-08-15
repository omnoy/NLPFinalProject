
import pandas as pd
from random import shuffle
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from judges_detection_model import judges_detection_model

JUDGES_PATH = "court_dataset/judges.xlsx"
FULLSET_PATH = "court_dataset/judges_jedgments_links.xlsx"

judge_df = pd.read_excel(JUDGES_PATH)
judge_numbers = {key:inx for inx, (key) in enumerate(judge_df["השופטים"])}
print(judge_df)

df = pd.read_excel(FULLSET_PATH)
df = df.dropna()
df.head()

alldata = [(judge_numbers[judge],judgment) for judge,judgment in zip(df["השופט"],df["פסק-דין"])]
shuffle(alldata)

text_list = [text for _,(_,text) in enumerate(alldata)]

size = len(alldata)
train = alldata[:int(size*0.8)]
validation = alldata[len(train):]

print(f"DB Size: {size}")
print(f"Train Size: {len(train)}")
print(f"Vali Size: {len(validation)}")

x_train = []
y_train =[]
x_validation = []
y_validation =[]

for inx,(ty,tx) in enumerate(train):
    y_train.append(ty)
    x_train.append(tx)

for inx,(ty,tx) in enumerate(validation):
    y_validation.append(ty)
    x_validation.append(tx)


tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_list)


sequences_train = tokenizer.texts_to_sequences(x_train)
sequences_validation = tokenizer.texts_to_sequences(x_validation)


max_length = max([len(seq) for seq in sequences_train + sequences_validation])

padded_sequences_train = pad_sequences(sequences_train, maxlen=max_length, padding='post')
padded_sequences_validation = pad_sequences(sequences_validation, maxlen=max_length, padding='post')

model = judges_detection_model(judge_df=judge_df["השופטים"],tokenizer=tokenizer,
                               max_length=max_length,y_train=y_train)

model.fit(padded_sequences_train=padded_sequences_train)
model.test(validation=validation,padded_sequences_validation=padded_sequences_validation)