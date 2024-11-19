#open("caminho","r")

#MODE
"""
r - leitura
a - append / incrementar
w - Escrita remove o que esta escrito e escreve novamnete tbm se o arquivo n exister ele criar
x - criar arquivo
r+ - Leitura + escrita
"""

"""
arquivo = open("test.txt","r")

print(arquivo.readable())
print(arquivo.read())
print(arquivo.readline())#linha 1
print(arquivo.readline())#linha 2
print(arquivo.readline())#linha 3
print(arquivo.readline())#linha 4
lista = arquivo.readlines()
print(lista)
print(lista[3])
"""

"""
# a w x
arquivo = open("test.txt","a")
arquivo.write("Python\n")
arquivo.write("C++\n")
arquivo.write("Terraform\n")
"""

"""
arquivo = open("test3.txt","w")
arquivo.write("Python\n")
arquivo.write("C++\n")
arquivo.write("Terraform\n")
"""

"""
arquivo = open("cria.txt","x")
arquivo.write("Python\n")
arquivo.write("C++\n")
arquivo.write("Terraform\n")

arquivo.close()#sempre fecha o arquivo no fim

"""

import os

if os.path.exists("Aula12/tes2.txt"):
    os.remove("Aula12/tes2.txt")
else:
    print("Arquivo não existe")

#os.rmdir("Aula12/nova_pasta") #os.rmdir remove uma pasta se a mesma estiver vazia
