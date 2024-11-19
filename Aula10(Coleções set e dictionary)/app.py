
#coleções que n repeti o item(distict)
# sempre tra aliatoriamente o resulte da lista


frutas = {"maçã", "Laranja", "Abacaxi" }

frutas.add("Pera")

frutas.remove("maçã")

frutas.pop()

print(frutas)

set1 = {"maçã", "Laranja", "Abacaxi"}

set2 = {0,3,50,-74}

set3 = {True,False,False,True}

set4 = {"Roger", 34, True}

print(set1)
print(set2)
print(set3)
print(set3)

#dictionary#

meses = {
    "Jan" : "1",
    "Fev" : "2",
    "Mar" : "3",
    "Abr" : "4",
    "Mai" : "5",
    "Jun" : "6",
    "Jul" : "7",
    "Ago" : "8",
    "Set" : "9",
    "Out" : "10",
    "Nov" : "11",
    "Dez" : "12",
    "PermiteMes" : True,
    "Ano" : "2024"
}

print(meses)

if len(meses) > 0:
    if meses.get("PermiteMes"):
        print(meses.get("Ano") + " / "+  meses.get("Dez"))
        meses["Ano"] = "2025"

print(meses.get("Ano"))



