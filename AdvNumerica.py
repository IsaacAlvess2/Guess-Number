import random

print("Seja bem vindo ao Guess Number")

choice_number = input("Digite o numero teto do desafio: ")

if choice_number.isdigit():
    choice_number = int(choice_number)
else:
    print("Erro: valor informado não é numérico")
    quit()

random_number = random.randint(0, choice_number)

n_choices = 0

while True:
    answer_user = input("Advinhe: ")

    if answer_user.isdigit():
        answer_user = int(answer_user)
    else:
        print("Erro: valor informado não é numérico")
        continue

    n_choices = n_choices + 1

    if answer_user == random_number:
        print("Acertou!")
        break
    elif answer_user > random_number:
        print("O número é menor que isso...")
    else:
        print("O número é maior que isso...")

print("Numero de tentativas:", n_choices)
