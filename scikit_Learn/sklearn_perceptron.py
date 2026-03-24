''' Implementação da RNA Perceptron para determinar a classe da flor iris,ajustar o mesmo algoritmo, para a execução do dataset Bancario. Fazer testes com valores diferentes das amostras treinadas. '''
from sklearn import preprocessing # biblioteca para suporte ao pré-processamento
from sklearn.model_selection import train_test_split # biblioteca para separação de amostras para treino e teste
from sklearn.linear_model import Perceptron # biblioteca com funções para a execução da RNA Perceptron
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn import metrics # biblioteca para obtenção de métricas para avaliação dos modelos
import matplotlib.pyplot as plt # biblioteca para plotar gráfico
import numpy as np
import pandas as pd
import random  # biblioteca aplicada na geração de números randômicos

df = pd.read_csv("files/bancario.csv")

# Separando a coluna da classe
y = df['Classe'].values

# Substituindo o valor string em numérico
y = np.where(y == 'bom', 1, -1)

# Separando as colunas com as variáveis para determinar os inputs da RNA
X = df[['Renda', 'Dívida']].values

print(y.shape)
print(X.shape)

# Normalização dos dados sklearn - dados entre 0 e 1
scaler = preprocessing.MinMaxScaler()
X = scaler.fit_transform(X)

# Plotando o gráfico para verificação das amostras
plt.scatter(X[:, 0], X[:, 1], c=y)
plt.title("Bom x Mau" )
plt.xlabel('Renda')
plt.ylabel('Dívida')
plt.show()

# Separação do dataset em amostras para treino e teste, considerando 20% dos valores para teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=10)

print(X_train.shape)
print(y_train.shape)

# Treinamento do Perceptron
p = Perceptron(random_state=42, eta0=0.0001, alpha=0.1)
p.fit(X_train, y_train)

# Validação do conjunto de amostras treinadas
predictions_train = p.predict(X_train)
train_score = accuracy_score(predictions_train, y_train)
print("Acurácia com dados de treinamento: ", train_score)

# Validação do conjunto de amostras que não participaram do treinamento
predictions_test = p.predict(X_test)
test_score = accuracy_score(predictions_test, y_test)
print("Acurácia com dados de teste: ", test_score)

print(classification_report(predictions_test, y_test))

print("Número de épocas no treinamento: ", p.n_iter_)
print("Lista de parâmetros configurados na Perceptron: ", p.get_params())

# Apresentação gráfica da matriz de confusão dos testes classificados
conf_matrix = confusion_matrix(y_test, predictions_test)
cm_display = metrics.ConfusionMatrixDisplay(confusion_matrix=conf_matrix, display_labels=['Mau', 'Bom'])
cm_display.plot()
plt.show()

# Teste individual de amostras já normalizadas
A = np.array([2500, 400]) # Padrão correto = 1 (bom)
A_y = np.array([1])
B = np.array([1200, 600]) # Padrão correto = -1 (mau)
B_y = np.array([-1])

prediction_A = p.predict([A])
prediction_B = p.predict([B])
print("Acurácia com dados de A: ", accuracy_score(prediction_A, A_y))
print("Acurária com dados de B: ", accuracy_score(prediction_B, B_y))

