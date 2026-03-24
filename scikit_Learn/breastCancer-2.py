''' Com a finalidade de aperfeiçoar a base de dados para a classificação, pesquisei sobre como ajustar os outliers do dataset e comparar a classificação para a situação sem ajuste de outliers '''

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron
from sklearn.metrics import classification_report, accuracy_score
from sklearn.impute import SimpleImputer

# Carregar o dataset
df = pd.read_csv('BreastCancerWisconsinDataSet.csv')

# Remover as colunas 'id' e 'Unnamed: 32'
df.drop(columns=['id', 'Unnamed: 32'], inplace=True)

# Codificar a coluna 'diagnosis' (M = 1, B = 0)
df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

# Identificação dos outliers usando IQR
def detect_outliers_iqr(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((data < lower_bound) | (data > upper_bound))

# Ajuste dos outliers
def adjust_outliers(data):
    Q1 = data.quantile(0.25)
    Q3 = data.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    data = np.where(data < lower_bound, lower_bound, data)
    data = np.where(data > upper_bound, upper_bound, data)
    return data

# Aplicar ajuste de outliers em todas as colunas exceto 'diagnosis'
df_adjusted = df.copy()
for column in df.columns[1:]:
    df_adjusted[column] = adjust_outliers(df_adjusted[column])

# Verificar e imputar valores NaN
imputer = SimpleImputer(strategy='mean')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
df_adjusted_imputed = pd.DataFrame(imputer.fit_transform(df_adjusted), columns=df_adjusted.columns)

# Dividir os dados em treinamento e teste
X = df_imputed.drop(columns=['diagnosis'])
y = df_imputed['diagnosis']

X_adj = df_adjusted_imputed.drop(columns=['diagnosis'])
y_adj = df_adjusted_imputed['diagnosis']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train_adj, X_test_adj, y_train_adj, y_test_adj = train_test_split(X_adj, y_adj, test_size=0.2, random_state=42)

# Padronizar os dados
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
X_train_adj = scaler.fit_transform(X_train_adj)
X_test_adj = scaler.transform(X_test_adj)

# Treinar o classificador Perceptron
clf = Perceptron(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

clf_adj = Perceptron(random_state=42)
clf_adj.fit(X_train_adj, y_train_adj)
y_pred_adj = clf_adj.predict(X_test_adj)

# Avaliar os resultados
print("Resultados sem ajuste de outliers:")
print(classification_report(y_test, y_pred))
print("Acurácia:", accuracy_score(y_test, y_pred))

print("\nResultados com ajuste de outliers:")
print(classification_report(y_test_adj, y_pred_adj))
print("Acurácia:", accuracy_score(y_test_adj, y_pred_adj))
