try:
    numero = int(input("Digite um numero: "))
    print(numero)
#    10/0
except ZeroDivisionError:
    print("Divisão por zero não é possivel")
except ValueError:
    print("digite um valor Valido.")
except:
    print("Erro inesperado")
finally:
    print("Sempre Execute")