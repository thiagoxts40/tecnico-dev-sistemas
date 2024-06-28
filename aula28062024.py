op = 's'
while op.lower() == 's':
    email = input('Digite seu Email: ')
    try:
        if '@' in email and '.' in email.split('@')[-1]:
            email = email.replace('@', '').replace('.', '')
        else:
            raise ValueError('Email inválido')
    except ValueError as e:
        print(e)
    
    op = input('Quer prosseguir? S/N  ').strip().lower()

cp = 's'
vetorcpf = []
vetorcpf2 = []
while cp.lower() == 's':
    cpf = input('Digite seu CPF: ').replace('-', '').replace('.', '')
    vetorcpf.append(cpf)
    vetorcpf2.append(cpf)
    
    try:
        if len(cpf) != 11 or not cpf.isdigit():
            raise ValueError('CPF inválido')
        
        # Cálculo do primeiro dígito verificador
        peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
        total1 = sum(int(cpf[i]) * peso1[i] for i in range(9))
        resto1 = total1 % 11
        penultimonum = 0 if resto1 < 2 else 11 - resto1
        
        # Cálculo do segundo dígito verificador
        peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
        total2 = sum(int(cpf[i]) * peso2[i] for i in range(10))
        resto2 = total2 % 11
        ultimonum = 0 if resto2 < 2 else 11 - resto2
        
        if penultimonum == int(cpf[9]) and ultimonum == int(cpf[10]):
            print('CPF válido.')
        else:
            raise ValueError('CPF inválido')
            
    except ValueError as e:
        print(e)
    
    cp = input('Deseja continuar o programa? S/N ').strip().lower()
