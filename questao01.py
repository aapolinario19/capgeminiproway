# 'n' recebe um valor inteiro
n = int(input('n: '))
# loop começando no número 1 sempre
# a cada passada o 'n' acrescenta +1
for i in range(1, n+1):
    # convertendo o total de loops menos o 'n' por espaços
    # imprime a variável 'n' dada pelo usuário convertida para '*'
    print((n - i) * ' ' + (i * '*'))
