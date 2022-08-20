#DATO DE ENTRADA PARA ALMACENAR EL VALOR DEL NIVEL DEL AGUA

nivelAgua=int(input("Digite el nivel de Agua"))

#CONDICIONES MULTIPLES CON PYTHON
if(nivelAgua>=0 and nivelAgua<20):
    print(f'peligro el nivel de Agua es: {nivelAgua} y es bajo')
elif(nivelAgua>=20 and nivelAgua<400):
    print(f'el nivel de Agua es {nivelAgua} es optimo')
elif(nivelAgua>=400):
     print(f'peligro el nivel de Agua es {nivelAgua} y es muy alto')
else:
    print("Digite una opcion valida")