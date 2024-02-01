#Sistema Bancário
#


def sacar(*, saldo, valor, extrato, saque_diario, limite_saques):
   
  if saque_diario > limite_saques:
        print(f"Limite máximo permitido por saque é de {limite_saques}.")
        
  elif valor > saldo:
        print("Desculpe, saldo insuficiente para a operação desejada")

  else:
        saldo -= valor
        saque_diario += 1
        extrato += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado")
   
  return saldo, extrato, saque_diario

def depositar(valor, saldo, extrato, /):
      
      if valor < 0:
        print("Valor inválido")

      else:
        saldo += valor
        print(saldo)
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(extrato)
        print("Depósito realizado")
   
      return saldo, extrato
   
def exibir_extrato(saldo, /, *, extrato):
   
    print("\n******** EXTRATO ********")
    print("Não existem movimentações" if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("\n*************************")


def criar_cliente(clientes):
      
      cpf = input("Informe o CPF do cliente - somente números: ")
      cliente = filtrar_cliente(cpf, clientes)

      if cliente:
         print("Já existe um usuário com este CPF")
         return
      
      nome = input("Digite o nome completo: ")
      data_nascimento = input("Digita a data de nascimento: ")
      endereco = input("Digite o enderço com logradouro,número, bairro, cidade/sigla estado")
   
      clientes.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

      print("Usuário criado com sucesso")

def filtrar_cliente(cpf, clientes):

  clientes_filtrados = [cliente for cliente in clientes if cliente[cpf] == cpf] 
  return clientes_filtrados[0] if clientes_filtrados else None

def criar_conta(AGENCIA, numero_conta, clientes):
   
  cpf = input("Informe o CPF do cliente - somente números: ")
  cliente = filtrar_cliente(cpf, clientes)

  if cliente:
    print("Conta criada com sucesso!")
    return {"agencia": AGENCIA, "numero_conta": numero_conta, "cliente": cliente}
   
  print("Usuário não encontrado. Não foi possível criar uma conta")

def main():

  menu = """
  *********** MENU **********

    [1] Depósito
    [2] Saque
    [3] Extrato
    [4] Cadastrar cliente
    [5] Criar conta
    [4] Sair

    Por favor digite sua opção

  ****************************
  """
   
  saldo = 0
  saque_diario = 0
  extrato = ""
  clientes = []
  contas = []
  LIMITE_SAQUE_DIARIO = 3
  LIMITE_SAQUE = 500
  AGENCIA = "0001"
   
  while True:

    opcao = input(menu)

    if opcao == "1":
      valor = int(input("Digite o valor desejado: "))

      saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "2":
      if saque_diario >= LIMITE_SAQUE_DIARIO:
        print("Limite diário excedido.")
        continue

      valor = int(input("Digite o valor desejado: "))

      saldo, extrato, saque_diario = sacar(saldo=saldo, valor=valor, extrato=extrato, saque_diario=saque_diario, limite_saques=LIMITE_SAQUE)
      
    elif opcao == "3":

      exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
       criar_cliente(clientes)

    elif opcao == "5":
      numero_conta = len(contas) + 1 # solução válida sem exclusão de contas
      conta = criar_conta(AGENCIA, numero_conta, clientes)
      
      if conta:
         contas.append(conta)

    elif opcao == "6":
      break
    else:
      print("Opção inválida. Por favor selecione novamente a opção desejada.")


main()
