import datetime
import streamlit as st
import pandas as pd
import locale

# Função para carregar o CSS


def load_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# -------------------------------#


locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')


def comparate(ativo, passivo):
    ativo_formatado = locale.currency(ativo, grouping=True)
    passivo_formatado = locale.currency(passivo, grouping=True)

    if ativo == passivo:
        return f"Conferência de balanço realizada com sucesso !!! {ativo_formatado}", "green"
    else:
        return f"Conferência de balanço possui erros: {ativo_formatado} vs {passivo_formatado}", "red"


def display_comparate():
    ativo = 200000.00
    options = [46000.00, 500000.00, 200000.00]

    options_formatadas = [locale.currency(
        val, grouping=True) for val in options]

    st.title("O valor do Ativo é de R$200.000,00")

    option = st.selectbox(
        "Selecione o valor do passivo:",
        options=options_formatadas
    )

    # Encontrar o valor original numérico correspondente ao valor selecionado no selectbox
    option_valor = options[options_formatadas.index(option)]

    # Comparar o valor do ativo com o valor selecionado
    resultado, cor = comparate(ativo, option_valor)

    # Mostrar o botão/luz que acende verde/vermelho primeiro
    st.markdown(f"""
    <div class="light" style="background-color: {cor};"></div>
    """, unsafe_allow_html=True)

    # Exibir o resultado com a cor correspondente logo abaixo
    st.markdown(f"<h3 style='color: {cor};'>{
                resultado}</h3>", unsafe_allow_html=True)


def show():
    display_comparate()


def display_clients():
    data = {
        "ID": [1, 2, 3, 4, 5, 6, 8, 9, 10, 7],
        "Nome": [
            "João Silva", "Maria Oliveira", "Carlos Souza", "Ana Costa",
            "Fernanda Santos", "Paulo Almeida", "Rafael Rodrigues",
            "Mariana Lima", "Eduardo Martins", "Juliana Silva Pereira",
        ],
        "Email": [
            "joao.silva@example.com", "maria.oliveira@example.com",
            "carlos.souza@example.com", "ana.costa@example.com",
            "fernanda.santos@example.com", "paulo.almeida@example.com",
            "rafael.rodrigues@example.com", "mariana.lima@example.com",
            "eduardo.martins@example.com", "juliana.pereira@example.com",
        ],
        "Telefone": [
            "4711987654321", "4721987654321", "4731987654321", "4741987654321",
            "4751987654321", "4761987654321", "4781987654321", "4791987654321",
            "4711987654322", "4771987654321",
        ],
    }

    df = pd.DataFrame(data)

    st.title("Consulta de Clientes")
    filtro_nome = st.text_input("Digite o nome para filtrar:", "").strip()

    if filtro_nome:
        df_filtrado = df[df["Nome"].str.contains(
            filtro_nome, case=False, na=False)]
        st.write(f"Exibindo resultados para: **{filtro_nome}**")
    else:
        df_filtrado = df
        st.write("Exibindo todos os clientes")

    st.dataframe(df_filtrado, use_container_width=True)

# Função para exibir a seleção de ferramentas com ícones


def display_tool_selection():
    option_map = {
        0: ":material/add:",
        1: ":material/zoom_in:",
        2: ":material/zoom_out:",
        3: ":material/zoom_out_map:",
    }

    selection = st.radio(
        "Ferramenta",
        options=list(option_map.keys()),  # Transforma as chaves em uma lista
        format_func=lambda option: option_map[option],
    )
    st.write(
        "A opção selecionada foi: "
        f"{None if selection is None else option_map[selection]}"
    )

# Função para exibir botões de interação


def display_buttons():
    col1, col2, col3, col4 = st.columns(4)

    if col1.button("Botão simples", use_container_width=True):
        col1.markdown("Você clicou no botão simples.")

    if col2.button("Botão de emoji", icon="😃", use_container_width=True):
        col2.markdown("Você clicou no botão de emoji.")

    if col3.button("Botão material", icon=":material/mood:", use_container_width=True):
        col3.markdown("Você clicou no botão material.")

    if col4.button("Botão customizado", icon="🔥", use_container_width=True):
        col4.markdown("Você clicou no botão customizado.")

# Função para exibir o seletor de data


def display_date_input():
    today = datetime.datetime.now()
    next_year = today.year + 1
    jan_1 = datetime.date(next_year, 1, 1)
    dec_31 = datetime.date(next_year, 12, 31)

    d = st.date_input(
        "Buscar arquivos por data :",
        (jan_1, datetime.date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="DD.MM.YYYY",
    )

    d = st.date_input("Selecione a data do compromisso",
                      datetime.date(2019, 7, 6))
    st.write("A data selecionada foi:", d)

# Função principal para carregar todos os componentes


def show():
    load_css("css/comp.css")
    display_comparate()
    display_clients()
    display_tool_selection()
    display_buttons()
    display_date_input()
