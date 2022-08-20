edad=int(input("Digite la edad:"))

if(edad >= 0 and edad <14):
    print(f'usted es un niño')
elif(edad >= 14 and edad < 28):
    print(f'usted es un joven')
elif(edad >= 28 and edad < 60):
    print(f'usted es un adulto')
elif(edad >= 60 ):
    print(f'usted es un viejitoooooo')
else:
    print("Digite una edad valida")
