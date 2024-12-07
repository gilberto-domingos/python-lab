import datetime
import streamlit as st
 import pandas as pd
  import locale

   def load_css(file_name):
        with open(file_name) as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    # -------------------------------------------------------------------

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
    # -----------------------------------------------------------------------

    def show():
        display_comparate()

    def display_clients():
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

        st.title("Consulta de Clientes")
        filtro_nome = st.text_input(
            "Digite a empresa para filtrar:", "").strip()

        if filtro_nome:
            df_filtrado = df[df["Empresa"].str.contains(
                filtro_nome, case=False, na=False)]
            st.write(f"Exibindo resultados para: **{filtro_nome}**")
        else:
            df_filtrado = df
            st.write("Exibindo todas as empresas")

        st.dataframe(df_filtrado, use_container_width=True)

        # Gerar a tabela HTML
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
        tabela_html += "</tbody></table>"

        st.markdown(tabela_html, unsafe_allow_html=True)
    # -----------------------------------------------------------------------------------

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

    # --------------------------------------------------------------

    def display_tool_selection():
        option_map = {
            0: ":material/add:",
            1: ":material/zoom_in:",
            2: ":material/zoom_out:",
            3: ":material/zoom_out_map:",
        }

        selection = st.radio(
            "Ferramenta",
            # Transforma as chaves em uma lista
            options=list(option_map.keys()),
            format_func=lambda option: option_map[option],
        )
        st.write(
            "A opção selecionada foi: "
            f"{None if selection is None else option_map[selection]}"
        )

    # ---------------------------------------------------------------------------------

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

    # ----------------------------------------------------------------------
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

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

    # ------------------------------------------------------------

    def show():
        load_css("css/comp.css")
        display_comparate()
        display_clients()
        display_tool_selection()
        display_buttons()
        display_date_input()
