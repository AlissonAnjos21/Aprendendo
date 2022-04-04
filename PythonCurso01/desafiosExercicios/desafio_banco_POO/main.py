"""
Exercício com Abstração, Herança, Encapsulamento e Polimorfismo
Criar um sistema bancário (extremamente simples) que tem clientes, contas e
um banco. A ideia é que o cliente tenha uma conta (poupança ou corrente) e que
possa sacar/depositar nessa conta. Contas corrente tem um limite extra. Banco
tem clientes e contas.

Dicas:
Criar classe Cliente que herda da classe Pessoa (Herança)
    Pessoa tem nome e idade (com getters)
    Cliente TEM conta (Agregação da classe ContaCorrente ou ContaPoupanca)
Criar classes ContaPoupanca e ContaCorrente que herdam de Conta
    ContaCorrente deve ter um limite extra
    Contas têm agência, número da conta e saldo
    Contas devem ter método para depósito
    Conta (super classe) deve ter o método sacar abstrato (Abstração e
    polimorfismo - as subclasses que implementam o método sacar)
Criar classe Banco para AGREGAR classes de clientes e de contas (Agregação)
Banco será responsável autenticar o cliente e as contas da seguinte maneira:
    Banco tem contas e clientes (Agregação)
    * Checar se a agência é daquele banco
    * Checar se o cliente é daquele banco
    * Checar se a conta é daquele banco
Só será possível sacar se passar na autenticação do banco (descrita acima)
"""

# Futuramente eu planejo melhorar o sistema criado nesse desafio
# Talvez transformando isso em algum tipo de mini-projeto

from conta import ContaCorrente, ContaPoupanca
from cliente import Cliente
from banco import Banco

# Criação da conta/cliente 1
conta_1 = ContaPoupanca(1234, 1, 21)
cliente_1 = Cliente('Maria', 42, conta_1)

# Criação da conta/cliente 2
conta_2 = ContaCorrente(1234, 2, 42, 100)
cliente_2 = Cliente('Marta', 21, conta_2)

# Criação do banco utilizando no momento a conta_1 e o cliente_1
banco = Banco(conta_1, cliente_1)

# Adicionei o servico conta_1 e cliente_1 ao sistema do banco
banco.adicionar_servico(conta_1, cliente_1)

# Validei, ou seja, verifiquei se a conta_1/cliente_1 estão cadastrados no sistema do banco
banco.validar()
banco.cliente.conta.sacar(20)
# A cada novo saque é necessário verificar a validação novamente
banco.validar()
banco.cliente.conta.sacar(1)
banco.cliente.conta.informar_saldo()

print('\n#############################################\n')

# Alterando a conta/cliente utilizados
banco.conta = conta_2
banco.cliente = cliente_2

# A operação será invalidada, pois eu ainda não adicionei essa conta/cliente no sistema de serviços do banco
banco.validar()
banco.cliente.conta.sacar(63)
banco.cliente.conta.informar_saldo()

# Agora adicionando o serviço
banco.adicionar_servico(conta_2, cliente_2)
banco.validar()
banco.cliente.conta.sacar(63)
banco.cliente.conta.informar_saldo()

banco.validar()
banco.cliente.conta.sacar(80)  # Saldo/limite insuficientes
banco.cliente.conta.informar_saldo() # Continua o mesmo
