class Conta:
    def __init__(self, idConta, nameAccount, Balance):
        self.idConta = idConta
        self.nameAccount = nameAccount
        self.Balance = Balance
        
    def deposit(self, value):
        self.Balance += value
        print(f"Depósito realizado com sucesso! Novo Balance: R${self.Balance:.2f}")
        
    def withdraw(self, value):
        if value <= self.Balance:
            self.Balance -= value
            print(f"Saque realizado com sucesso! Novo Balance: R${self.Balance:.2f}")
        else:
            print("Saldo insuficiente para realizar o saque.")
    
    def showBalance(self):
        print(f"Saldo atual: R${self.saldo:.2f}")

# Possivel heranca para corente e poupanca

account = Conta(1,'lorem',11.11)

print(f'Nome: {account.nameAccount}',
      f'Saldo: R${account.Balance}')