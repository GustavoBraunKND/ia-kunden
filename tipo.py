# tipo.py
from tensorflow import keras
import numpy as np
import json

# carrega o modelo UMA vez
model = keras.models.load_model('question.keras')

# carrega os índices
with open('index_labels.json') as f:
    index_labels = json.load(f)

with open('idx_to_label.json') as f:
    idx_to_label = json.load(f)


def classificar(descricao: str):
    """
    Recebe uma descrição e retorna:
    - classe prevista (str)
    - confiança (float)
    """
    pred = model.predict(np.array([descricao], dtype=object))[0]

    classe_idx = int(np.argmax(pred))
    classe = idx_to_label[str(classe_idx)]
    confianca = float(pred[classe_idx])

    return classe, confianca * 100