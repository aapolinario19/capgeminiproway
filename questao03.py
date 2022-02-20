# substring da string
def contadorAnagrama(palavra):
    # retorna o total de anagramas
    # substring em 'palavra'
    tamanhoPalavra = len(palavra)
    dicionario = dict()

    # loop para o tamanho da substring
    for i in range(tamanhoPalavra):
        sub = ''
        for j in range(i, tamanhoPalavra):
            sub = ''.join(sorted(sub + palavra[j]))
            dicionario[sub] = dicionario.get(sub, 0)

            # adiciona o contador correspondente ao dicionário
            dicionario[sub] += 1

    anagramas = 0

    # loop por todos os dicionários
    # items agregando ao contador da substring
    for k, v in dicionario.items():
        anagramas += (v * (v - 1)) // 2
    return anagramas

# input para entrada de dados do usuário
palavra = str(input('Digite algo: '))
print(contadorAnagrama(palavra))
