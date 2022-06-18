import random
import sys

#Classe Cliente
class Cliente():#Construtor com parametros
    def __init__(self, nome, numero_conta, saldo=0):
        self.nome = nome
        self.numero_conta = numero_conta
        self.saldo = saldo
    #imprime os detalhes da conta
    def account_detail(self):
        print("\n----------DETALHES DA CONTA----------")
        print(f"Titular da conta: {self.nome.upper()}")
        print(f"Número da conta: {self.numero_conta}")
        print(f"saldo disponível: Nu.{self.saldo}\n")
    #realiza o deposito
    def deposit(self, amount):
        self.amount = amount
        self.saldo = self.saldo + self.amount
        print("Saldo da conta corrente: Nu.", self.saldo)
        print()
    #verifica se tem saldo para subtrair
    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.saldo:
            print("Fundos insuficientes!")
            print(f"Seu saldo é Nu.{self.saldo} somente.")
            print("Tente com valor menor que o saldo.")
            print()
        else:
            self.saldo = self.saldo - self.amount
            print(f"Nu.{amount} retirada bem sucedida!")
            print("Saldo da conta corrente: Nu.", self.saldo)
            print()
    #verifica o saldo
    def check_balance(self):
        print("saldo disponível: Nu.", self.saldo)
        print()
    #Realiza as transaçoes
    def transaction(self):
        print("""
            TRANSAÇÃO
        *********************
            Menu:
            1. Detalhe da conta
            2. Verificar saldo
            3. Depósito
            4. Retirar
            5. Sair
        *********************
        """)
        #Loop infinito para mostrar o menu de opções
        while True:
            try:
                option = int(input("Enter 1, 2, 3, 4 ou 5:"))
            except:
                print("Error: Entre 1, 2, 3, 4, ou 5 somente!\n")
                continue
            else:
                if option == 1:
                    atm.account_detail()
                elif option == 2:
                    atm.check_balance()
                elif option == 3:
                    amount = int(input("Quanto você quer depositar(Nu.):"))
                    atm.deposit(amount)
                elif option == 4:
                    amount = int(input("Quanto você deseja retirar(Nu.):"))
                    atm.withdraw(amount)
                elif option == 5:
                    #Imprime as informaçoes do Recibod o Cliente
                    print(f"""
                impressão de recibo..............
          ******************************************
              A transação foi concluída.                         
              Número da transação: {random.randint(10000, 1000000)} 
              Titular da conta: {self.nome.upper()}                  
              Número da conta: {self.numero_conta}                
              saldo disponível: Nu.{self.saldo}                    

              Obrigado por nos escolher como seu banco                
          ******************************************
          """)
                    sys.exit()

#Imprime caso a conta tenha sido criada
print("*******BEM-VINDO AO BANCO DO InaToken*******")
print("___________________________________________________________\n")
print("----------CRIAÇÃO DE CONTA----------")
nome = input("Digite seu nome: ")
numero_conta = input("Digite o número da sua conta: ")
print("Parabéns! Conta criada com sucesso......\n")
#Cria o objeto e passa os parametros
atm = Cliente(nome, numero_conta)
#Pergunta ao cliente, se ele deseja continuar a usar o caixa eletronico
while True:
    trans = input("Você quer fazer alguma transação?(s/n):")
    if trans == "s":
        atm.transaction()
    elif trans == "n":
        print("""
    -------------------------------------------
   | Obrigado por nos escolher como seu banco |
   | Visite nos novamente!                    |
    -------------------------------------------
        """)
        break
    else:
        print("Comando errado! Digite 's' para sim e 'n' para NÃO.\n")
