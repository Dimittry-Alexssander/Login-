usuario = input('Digite o nome do usuário:').strip().lower()

if usuario =='admin':
    print('Agora digite a senha de acesso: ')
else: 
    print ('usuario invalido')



senha = '1234'
senha_acesso = input ('senha: ')
if usuario ==  "admin" and senha == senha_acesso:
    print ('Acesso permitido')
else: 
    print ('Acesso negado')


