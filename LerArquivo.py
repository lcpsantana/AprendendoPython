class Cliente:
    def __init__(self, tipoReg, cpf, nome, cnpj, valor):
        self.tipo = tipoReg
        self.cpf = cpf
        self.nome = nome
        self.cnpj = cnpj
        self.valor = valor


clientes =   open ("514AVRENCAP000001484300058622082018S.txt")
for linhaCliente in clientes:
  dadosClientes = linhaCliente.split(";")
  cliente = Cliente(dadosClientes[0], 
                    dadosClientes[1],
                    dadosClientes[2],
                    dadosClientes[3],
                    dadosClientes[4])
  
  print ('Nome do cliente: ' + cliente.nome)
  print ('CPF: ' + cliente.cpf)
  print ('Valor a receber: ' + cliente.valor)
                    