import streamlit as st
import pandas as pd
from st_keyup import st_keyup


def carregar_css(caminho):
    with open(caminho) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def show():
    # Carregar o CSS primeiro
    carregar_css("css/homex.css")

    # Dados para o DataFrame
    dados = [
        ["001", "Petrobras", "01/24", "A1", "João Silva",
            10, 5, "01/12/2024", 20, 200, 50],
        ["002", "Itaú Unibanco", "02/24", "B2",
            "Maria Santos", 12, 6, "02/12/2024", 25, 150, 45],
        ["003", "Bradesco", "03/24", "C3", "Carlos Lima",
            15, 4, "03/12/2024", 22, 300, 55],
        ["004", "Ambev", "04/24", "D4", "Ana Costa",
            9, 7, "04/12/2024", 30, 250, 60],
        ["005", "Magazine Luiza", "05/24", "E5",
            "Lucas Dias", 8, 8, "05/12/2024", 18, 220, 50],
        ["006", "Natura", "06/24", "F6", "Mariana Pinto",
            14, 6, "06/12/2024", 24, 180, 48],
        ["007", "Banco do Brasil", "07/24", "G7",
            "Paulo Sousa", 11, 5, "07/12/2024", 28, 270, 57],
        ["008", "Gerdau", "08/24", "H8", "Fernanda Alves",
            13, 7, "08/12/2024", 30, 290, 62],
        ["009", "Embraer", "09/24", "I9", "Ricardo Nunes",
            10, 5, "09/12/2024", 25, 310, 58],
        ["010", "Vale", "10/24", "J10", "Sara Leite",
            9, 6, "10/12/2024", 27, 330, 65],
    ]

    # Criação do DataFrame
    df = pd.DataFrame(dados, columns=[
        "Código", "Empresa", "Balanço", "Célula", "Funcionário", "T.E", "R.T", "Fech.Balanço", "IR", "V.", "R"
    ])

    # Exibição do título
    st.title("Conferência de Balanço")

    # Componente de filtro dinâmico
    filtro = st_keyup("Digite para filtrar por empresa:",
                      debounce=300, key="filtro_empresa")

    # Filtrar a tabela com base no texto digitado
    if filtro:
        df_filtrado = df[df["Empresa"].str.contains(
            filtro, case=False, na=False)]
        st.write(f"Exibindo resultados para: **{filtro}**")
    else:
        df_filtrado = df
        st.write("Exibindo todas as empresas.")

    # Exibição do DataFrame
    st.dataframe(df_filtrado, use_container_width=True)
