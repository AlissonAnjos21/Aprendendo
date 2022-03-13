from contas.contacorrente import ContaCorrente
from contas.contapoupanca import ContaPoupanca

cp = ContaPoupanca('Maria', 1234, 21)
cp.retirar(20)
cp.retirar(20)
cp.depositar(20)

print('-------------------------------------------------------------------------------------')

cc = ContaCorrente('Alice', 5678, 2100)
cc.retirar(2121)  # Saldo da Conta: -21
cc.depositar(210)  # Saldo da Conta: 189
cc.retirar(189)  # Saldo da Conta: 0
cc.retirar(220)  # A quantia a ser retirada excede o limite da conta!!!
