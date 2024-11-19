tenho_sede = True

if tenho_sede:
    print("beber agua")

print("Vida que segue")

esta_frio = False

if esta_frio:
    print("Vestir um casaco")
else:
    print("Vestir camiseta")

tenho_sede = False
tenho_fome = True
estou_em_dieta = True
if tenho_sede or tenho_fome:
    print("vou na cozinha")
else:
    print("ficar vendo netflix")

if tenho_sede and tenho_fome:
    print("fazer sanduiche e coca")
else:
    print("não tenho fome ou nao tenho sede")

if tenho_sede and tenho_fome:
    print("fazer sanduiche e coca")
elif tenho_sede and not(tenho_fome):
    if estou_em_dieta:
        print("tomar agua")
    else:
        print("Tomar uma coquinha")
elif not(tenho_sede) and tenho_fome:
    print("fazer um sanduiche")
else:
    print("ficar vendo netflix")

num1 = 5
num2 = 32

if num1 == num2:
    print("num1 é igual num2")
elif num1 != num2:
    print("num1 é diferente de num2")
elif num1 > num2:
    print("num1 é maior que num2")
elif num1 < num2:
    print("num1 é menor que num2")
elif num1 >= num2:
    print("num1 é maior igual a num2")
elif num1 <= num2:
    print("num1 é menor igual a num2")


#operadores logicos
# or => ou
# and => é
# not() => negação

# operadores de comparação
# == -> igual
# != -> diferente
# >  -> maior
# <  -> menor
# >= -> maior ou igual
# <= -> menor ou igual
