mes=(input("Digite el mes del año "))

if(mes == "enero" or mes == "febrero" or mes == "marzo"):
    print(f'el mes {mes} esta en la estacion invierno')
elif(mes == "abril" or mes == "mayo" or mes == "junio"):
    print(f'el mes {mes} esta en la estacion primavera')
elif(mes == 'julio" or mes == "agosto" or mes == "septiembre'):
    print(f"el mes {mes} esta en la estacion verano")
elif(mes == "octubre" or mes == "noviembre" or mes == "diciembre"):
    print(f'el mes {mes} esta en la estacion otoño')
else:
    print("digite una opcion valida")
