nome = input('Usuário: ')
# variável recebe strings específicas para comparação
especiais = '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+'
# variável 'senha' usada no programa para comparações com os requisitos
senha = input('Senha: ')
# verifica se o tamanho da senha é menor que 6 caracteres
if len(senha) < 6:
    print('A senha precisa ter 6 caracteres ou mais!')
# verifica se há pelo menos 1 dígito pela string da senha
if not any(char.isdigit() for char in senha):
    print('A senha precisa de 1 dígito!')
# converte a senha para maiúscula e compara com a senha
if senha.upper() == senha:
    print('A senha precisa de 1 letra minúscula')
# converte a senha para minúscula e compara com a senha
if senha.lower() == senha:
    print('A senha precisa de 1 letra maiúscula!')
# loop pela variável 'especiais'
for caractere in especiais:
    # verifica se possui caractere especial
    if caractere in senha:
        # boolean recebe valor True
        temcaractere = True
        # se a condição for satisfeita o programa finaliza aqui
        break
    else:
        # caso não seja satisfeita o programa entra no else
        # boolean recebe o valor False
        temcaractere = False
# condição recebe False e imprime o que necessita na senha
if temcaractere == False:
    print('A senha precisa de 1 caractere especial!')
