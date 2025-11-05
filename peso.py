peso = int (input("Digite seu peso em kg: "))
altura = float(input ('Digite sua altura com uma casa decimal'))

imc = peso / (altura**2)

print (f'{imc:.2f}')


if imc <= 18.5:
    print ("Você está abaixo do peso ")
elif imc <= 24.9:
    print ('Você está no peso ideal')
elif imc <= 29.9:
    print ('Voce está com sobrepeso')
else:
    print ('Voce está obeso')


print ("Fim do codigo") 
    