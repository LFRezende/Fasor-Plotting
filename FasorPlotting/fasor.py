from matplotlib import pyplot as p
import numpy as np


def fasor():
    """
        Função void interativa que pede os valores a e b na entrada, lendo-os como strings, e verifica
    se as entradas individualmente são imaginários puros. Então, plota o gráfico.

        LISA - Luis Felipe Silva Rezende Soares, ELE-24, 2022, ITA
    """
    ac = False
    bc = False
    grade = False
    a = str(input('Digite o coeficiente de x.')).strip().lower()
    b = str(input('Digite o coeficiente de y.')).strip().lower()
    # Check de cor
    while True:
        cor = str(input('Selecione a cor da linha:\nVermelha - V\nAzul - A\nVerde - G')).strip().lower()[0]
        if cor in 'vga':
            break
        print('Cor incorreta!')
    # Multiplexando cores
    if cor == 'v':
        cor = 'r-'
    elif cor == 'g':
        cor = 'g-'
    else:
        cor = 'b-'
    while True:
        opg = str(input('Deseja uma grade? [S/N]')).strip().lower()[0]
        if opg in 'sn':
            break
        print('Opção Inválida!')
    if opg == 's':
        grade = True
    na = ''
    nb = ''
    # Cheque se há complexo. Se for, retira-se o caractere.
    if 'i' in a or 'j' in a:
        for v in a:
            if v.isnumeric() or v in '.-':
                na += v
        ac = True
    if 'i' in b or 'j' in b:
        for v in b:
            if v.isnumeric() or v in '.-':
                nb += v
        bc = True
    # Repassagem dos valores caso não imaginários puros.
    if not ac:
        na = a
    if not bc:
        nb = b
    # Para o caso de imaginário puro e unitário.
    if na == '' or na == '-':
        na += '1'
    if nb == '' or nb == '-':
        nb += '1'
    # Passagem para real
    _a = float(na)
    _b = float(nb)
    # Escala de gráfico ajustável aos inputs
    escala = max(abs(_a), abs(_b)) * 1.2
    # Tomada de um período com subdivisão de 0.01
    t = np.arange(0, 2*np.pi, 0.001)
    # Multiplex para qual tipo de par formar
    if ac:
        if bc:
            p.plot(_a*np.sin(t)*(-1), _b*np.sin(t)*(-1), cor)
        else:
            p.plot(_a*np.sin(t)*(-1), _b*np.cos(t), cor)
    else:
        if bc:
            p.plot(_a*np.cos(t), _b*np.sin(t)*(-1), cor)
        else:
            p.plot(_a*np.cos(t), _b*np.cos(t), cor)
    # Perfumarias
    ka = kb = ''
    if bc:
        kb = 'i'
    if ac:
        ka = 'i'
    # Teste de sinal
    if _b >= 0:
        p.title(f'Percurso do Fasor:  {_a:.1f}{ka}x + {_b:.1f}{kb}y')
    else:
        p.title(f'Percurso do Fasor:  {_a:.1f}{ka}x - {abs(_b):.1f}{kb}y')
    p.axis([-escala, escala, -escala, escala])
    p.grid(grade)
    p.show()
