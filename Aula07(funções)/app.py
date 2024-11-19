

def fazer_big_mac(nome):
    print(f"sanduiche big mic {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_ref(tipo_ref, tamanho_ref):
    print(f"{tipo_ref} - {tamanho_ref}")


def fazer_combo_big_mac(nome,tamanho_batata,tipo_ref,tamanho_ref):
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_ref(tipo_ref,tamanho_ref)

fazer_combo_big_mac("Felipe","Grande","Coca","Média")

def soma_num(num1,num2):
    return num1 + num2

resultado = soma_num(15,20)
print(resultado)


def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

resultado_maior_num = maior_num([2123,12,126,48,56548,-45])
print(resultado_maior_num)