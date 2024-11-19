"""
Aqui vai um problema de lógica interessante que você pode resolver com Python:

Problema: O Desafio dos Guardas e Prisioneiros

Em uma prisão, há 100 prisioneiros e 100 celas, numeradas de 1 a 100. Inicialmente, todas as celas estão fechadas.

Um grupo de 100 guardas é instruído a fazer o seguinte:

O primeiro guarda abre todas as celas.
O segundo guarda fecha todas as celas que têm um número par.
O terceiro guarda muda o estado (abre se estiver fechada e fecha se estiver aberta) de todas as celas que têm um número múltiplo de 3.
O quarto guarda faz o mesmo para todas as celas múltiplas de 4, e assim por diante, até o centésimo guarda, que altera o estado apenas da cela 100.
Pergunta: Após todos os guardas terem passado, quantas celas permanecem abertas?

Regras:
A célula só pode estar "aberta" ou "fechada".
Cada guarda age de acordo com seu número (Guarda n modifica as celas múltiplas de n).
Tenta resolver esse problema em Python! É um ótimo desafio de lógica.
"""

prisioneiros = 100
celas = 100
guardas =100
celas_abertafechada = []
guarda_definidos =[]

prisioneiros = 100
celas = 100
guardas = 100
celas_abertafechada = []
guarda_definidos = []

def Inicializacao_de_Celas():    
    for i in range(100):
        celas_abertafechada.extend(["Fechado"])

def Guarda_Definidos():    
    for i in range(1, 101):
        guarda_definidos.extend([i])

def Mudanca_de_Estado_das_Celas():
    for guarda in guarda_definidos:
        for i in range(len(celas_abertafechada)):
            numerocela = i + 1
            if Verificacao_de_Multiplos(numerocela, guarda):
                if celas_abertafechada[i] == "Fechado":
                    celas_abertafechada[i] = "Aberto"
                else:
                    celas_abertafechada[i] = "Fechado"

def Verificacao_de_Multiplos(numerocela, multiplo):
    return numerocela % multiplo == 0

Inicializacao_de_Celas()
Guarda_Definidos()
Mudanca_de_Estado_das_Celas()

print(celas_abertafechada)
