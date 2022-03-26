# IDEIA: ADICIONAR O CASO DE TER 1 + J COMO COEFICIENTE DE UM DELES.
# Função para Plot de Fasores
# Bibliotecas
from fasor import fasor
# Textinhos
print('=-='*20)
print(f'{"PLOT DE FASOR":^60}')
print('=-='*20)
print("""Observação: Esta função, por ora, não é capaz de calcular 
coeficientes multiplicados por (x + yi), x*y != 0. 
Quem sabe numa próxima versão :P)\n""")
# Laço de chamada de função
while True:
    fasor()
    # Check de usuário câncer
    while True:
        manter = str(input('Deseja continuar?[S/N]')).strip().lower()[0]
        if manter in 'sn':
            break
        print('Opção Inválida!')
    if manter == 'n':
        break
# Textos finais
print('=-='*20)