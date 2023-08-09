empresa = input("Ingresar nombre de empresa: ")
mes = input("Ingresar nombre del mes: ")
ano = input("Ingresar nombre del año: ")

nueva = ""

with open("contraseñas2021.txt", "r") as diccionario:
   
    modificar = [nueva.replace("[Empresa]",empresa).replace("[Mes]",mes).replace("2021",ano) for nueva in diccionario]

with open("diccionario.txt","w") as file:
    for nueva in modificar:
        file.write(nueva)


#for nueva in modificar:
 #   print(nueva.strip())
