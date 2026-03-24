''' Leitura do dataset: Carregando o arquivo CSV.
Pré-processamento: Limpando os dados, remover colunas irrelevantes, lidar com valores faltantes e normalizar os dados.
Treinamento e teste: Dividindo os dados em conjuntos de treino e teste.
Treinamento do modelo: Treinando o classificador Perceptron.
Avaliação do modelo: Avaliando o desempenho do classificador. '''

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import accuracy_score, classification_report

# Passo 1: Leitura do dataset
df = pd.read_csv('BreastCancerWisconsinDataSet.csv')

# Passo 2: Pré-processamento dos dados
# Remover colunas irrelevantes 'id' e 'Unnamed: 32'
df.drop(['id', 'Unnamed: 32'], axis=1, inplace=True)

# Transformar a coluna 'diagnosis' em valores numéricos: M -> 1, B -> 0
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Verificar valores ausentes e substituí-los se necessário, apenas nas colunas numéricas
df.fillna(df.mean(numeric_only=True), inplace=True)

# Separar características e rótulos
X = df.drop('diagnosis', axis=1)
y = df['diagnosis']

# Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Normalizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Passo 3: Treinamento do modelo
clf = Perceptron(max_iter=1000, tol=1e-3, random_state=42)
clf.fit(X_train, y_train)

# Passo 4: Avaliação do modelo
y_pred = clf.predict(X_test)

# Métricas de avaliação
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

print(f'Acurácia: {accuracy}')
print(f'Relatório de classificação:\n{report}')
