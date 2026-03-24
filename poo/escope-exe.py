# Exemplo de escopo, aninhados, variaveis local, global etc...

def sistema_principal():

    def altera_local():
        mensagem = "mensagem LOCAL"
        # só existe aqui dentro

    def altera_na_funcao_externa():
        nonlocal mensagem
        mensagem = "mensagem NÃO-LOCAL (da função externa)"

    def altera_global():
        global mensagem_global
        mensagem_global = "mensagem GLOBAL"

    mensagem = "mensagem INICIAL da função externa"

    altera_local()
    print("Depois da função local:", mensagem)

    altera_na_funcao_externa()
    print("Depois da função não-local:", mensagem)

    altera_global()
    print("Depois da função global:", mensagem)


sistema_principal()
print("No escopo global:", mensagem_global)
