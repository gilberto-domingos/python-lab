import streamlit as st

# Carregar o CSS


def carregar_css(caminho):
    with open(caminho) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Função para exibir a página


def show():
    # Dados da tabela
    dados = [
        ["001", "Empresa 01", "01/24", "A1", "João Silva",
            10, 5, "01/12/2024", 20, 200, 50],
        ["002", "Empresa 02", "02/24", "B2", "Maria Santos",
            12, 6, "02/12/2024", 25, 150, 45],
        ["003", "Empresa 03", "03/24", "C3", "Carlos Lima",
            15, 4, "03/12/2024", 22, 300, 55],
        ["004", "Empresa 04", "04/24", "D4", "Ana Costa",
            9, 7, "04/12/2024", 30, 250, 60],
        ["005", "Empresa 05", "05/24", "E5", "Lucas Dias",
            8, 8, "05/12/2024", 18, 220, 50],
        ["006", "Empresa 06", "06/24", "F6", "Mariana Pinto",
            14, 6, "06/12/2024", 24, 180, 48],
        ["007", "Empresa 07", "07/24", "G7", "Paulo Sousa",
            11, 5, "07/12/2024", 28, 270, 57],
        ["008", "Empresa 08", "08/24", "H8", "Fernanda Alves",
            13, 7, "08/12/2024", 30, 290, 62],
        ["009", "Empresa 09", "09/24", "I9", "Ricardo Nunes",
            10, 5, "09/12/2024", 25, 310, 58],
        ["010", "Empresa 10", "10/24", "J10",
            "Sara Leite", 9, 6, "10/12/2024", 27, 330, 65],
    ]

    # Carregar o CSS
    carregar_css("css/homex.css")

    # Layout da barra superior
    st.markdown(
        """
        <div id="barra-superior">
            <div style="display: flex; align-items: center;">
                <span class="status-indicator"></span> Online
            </div>
            <div><span class="status-indicator"></span>Itamar Mosimann</div>
            <div>Empresa: Mosimann LTDA</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Título da página
    st.title("Conferência de Balanço")

    # Criar tabela em HTML
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

    # Exibir a tabela
    st.markdown(tabela_html, unsafe_allow_html=True)


#################  CSS  ##############################

/* Barra azul no topo */
#barra-superior {
    position: fixed;
    /* Fixa a barra no topo */
    top: 0;
    left: 0;
    width: 100%;
    /* Faz a barra ocupar toda a largura */
    display: flex;
    justify-content: space-between;
    align-items: center;
    background-color: #0077b6;
    color: white;
    padding: 10px 20px;
    font-size: 16px;
    font-family: Arial, sans-serif;
    z-index: 1000;
    /* Garante que a barra fique sobre outros elementos */
    box-sizing: border-box;
}

/* Indicador de status como bolinha verde */
.status-indicator {
    display: inline-block;
    width: 12px;
    height: 12px;
    margin-right: 8px;
    background-color: #28a745;
    /* Verde */
    border-radius: 50%;
}

/* Espaçamento entre os itens */
#barra-superior>div {
    margin: 0 10px;
}

/* Ajuste de layout para o conteúdo abaixo da barra */
#conteudo {
    margin-top: 60px;
    /* Evita sobreposição do conteúdo com a barra */
}

/* Tabela estilizada */
table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px auto;
}

th,
td {
    padding: 8px;
    text-align: center;
    /* Centraliza horizontalmente */
    vertical-align: middle;
    /* Centraliza verticalmente */
    border: 1px solid #ddd;
}

th {
    background-color: #0077b6;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #e8f5ff;
}

/* Responsividade */
@media screen and (max-width: 768px) {
    table {
        font-size: 12px;
    }

    #barra-superior {
        flex-direction: column;
        text-align: center;
    }
}