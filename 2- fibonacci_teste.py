fib_nums = [0, 1]  # Primeiros itens da sequência de fibonacci

input_usuario= int(input('Digite um número para checar\n'))

# Add new fibonacci terms until the input_usuario is reached
while fib_nums[-1] <= input_usuario:
    fib_nums.append(fib_nums[-1] + fib_nums[-2])

if input_usuario in fib_nums:
    print(f'Sim. O número {input_usuario} é um número da sequência.')
else:
    print(f'Não. O número {input_usuario} não é um número da sequência.')