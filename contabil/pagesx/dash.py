import streamlit as st
import pandas as pd
import plotly.express as px

print("passando pelo ponto 1")
print("passando pelo ponto 2")
print("passando pelo ponto 3")
print("passando pelo ponto 4")
print("passando pelo ponto 5")
print("passando pelo ponto 6")

names = ["gilson", "scott", "mat"]
for i in names:
    print(i)

print("passando pelo ponto 7")

df = pd.read_excel("./data/situationx.xlsx")