import pandas as pd
import tensorflow as tf
import numpy as np
from tensorflow.keras.layers import TextVectorization, Embedding, GlobalAveragePooling1D, Dense
from tensorflow.keras import Sequential
from tensorflow.keras.optimizers import Adam
import json

dados = pd.read_csv('descricoes.csv', sep=';')

descricoes = dados['DESCRICAO'].astype(str).values
labels = dados['LABEL'].astype(str).values

index_labels = {v: i for i, v in enumerate(set(labels))}
idx_to_label = {v: k for k, v in index_labels.items()}
y = tf.constant([index_labels[x] for x in labels])

vectorizer = TextVectorization(max_tokens=5000, output_sequence_length=50)
vectorizer.adapt(descricoes)

model = Sequential([
    vectorizer,
    Embedding(input_dim=5000, output_dim=16),
    GlobalAveragePooling1D(),
    Dense(8, activation='relu'),
    Dense(len(index_labels), activation='softmax')
])

model.compile(
    optimizer=Adam(learning_rate=0.001),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

model.fit(descricoes, y, epochs=1000, batch_size=32)

model.save('words.keras')

with open('index_labels.json', 'w') as f:
    json.dump(index_labels, f)

with open('idx_to_label.json', 'w') as f:
    json.dump(idx_to_label, f)