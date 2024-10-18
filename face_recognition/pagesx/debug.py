def formatação(quem, prog, n):
    return f'{quem} está aprensentando a {prog} #{n}'

nome = 'Eduardo'
programa = 'Live de python'
numero = '197'

breakpoint()

formatado = formatação(nome, programa, numero)

assert formatado == 'Eduardo está apresentando a Live de Python #197'