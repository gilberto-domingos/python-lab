import streamlit as st
import pandas as pd

# Função para carregar o CSS


def carregar_css(caminho):
    with open(caminho) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Função para exibir a página


def show():
    # Dados da tabela com empresas brasileiras famosas
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

    # Converter para DataFrame
    df = pd.DataFrame(dados, columns=[
        "Código", "Empresa", "Balanço", "Célula", "Funcionário", "T.E", "R.T", "Fech.Balanço", "IR", "V.", "R"
    ])

    # Carregar o CSS
    carregar_css("css/homex.css")

    # Layout da barra superior
    st.markdown(
        """
        <div id="barra-superior">
            <div style="display: flex; align-items: center;">
                <span class="status-indicator"></span> Online
            </div>
            <div>Usuário: Pedro Silva</div>
            <div>Empresa: Mosimann LTDA</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.title("Conferência de Balanço")

    st.dataframe(df, use_container_width=True)

    # Exibir a tabela em HTML
    tabela_html = """
    <table>
        <thead>
            <tr>
                <th>Código</th>
                <th>Empresa</th>
                <th>Balanço</th>
                <th>Célula</th>
                <th>Funcionário</th>
                <th>T.E</th>
                <th>R.T</th>
                <th>Fech.Balanço</th>
                <th>IR</th>
                <th>V.</th>
                <th>R</th>
            </tr>
        </thead>
        <tbody>
    """
    for linha in dados:
        tabela_html += "<tr>" + \
            "".join(f"<td>{col}</td>" for col in linha) + "</tr>"
    tabela_html += """
        </tbody>
    </table>
    """
    st.markdown(tabela_html, unsafe_allow_html=True)
