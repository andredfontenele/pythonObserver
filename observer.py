class Loja:
    def __init__(self):
        self._observadores = []

    def anexar(self, observador):
        self._observadores.append(observador)

    def desanexar(self, observador):
        self._observadores.remove(observador)

    def notificar(self):
        for observador in self._observadores:
            observador.atualizar(self)

class Estoque(Loja):
    def __init__(self, nome, quantidade):
        super().__init__()
        self._nome = nome
        self._quantidade = quantidade

    @property
    def quantidade(self):
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self._quantidade = quantidade
        self.notificar()

    def vender(self, quantidade):
        if self._quantidade == 0:
            print(f"Não é possível efetuar a venda. A quantidade de {self._nome} é zero.")
        elif quantidade > self._quantidade:
            print(f"Não é possível efetuar a venda de {quantidade} unidades. A quantidade de {self._nome} é insuficiente.")
        else:
            self.quantidade -= quantidade
            print(f"{quantidade} unidades de {self._nome} vendidas. Nova quantidade: {self._quantidade}")
            print("-----")

class Compras:
    def atualizar(self, assunto):
        if assunto.quantidade < 10:
            print(f"Departamento de compras notificado: estoque de {assunto._nome} está baixo. Quantidade atual: {assunto.quantidade}")

class Relatorios:
    def atualizar(self, assunto):
        print(f"Relatório atualizado: quantidade atual de {assunto._nome}: {assunto.quantidade}")

class AlertaEstoque:
    def atualizar(self, assunto):
        if assunto.quantidade < 5:
            print(f"Alerta: estoque de {assunto._nome} está criticamente baixo! Quantidade atual: {assunto.quantidade}")
        if assunto.quantidade == 0:
            print(f"A quantidade de {assunto._nome} é ZERO.")

# Criação do estoque e observadores
estoque = Estoque("Pães", 100)
compras = Compras()
relatorios = Relatorios()
alerta = AlertaEstoque()

# Ligação dos observadores ao estoque
estoque.anexar(compras)
estoque.anexar(relatorios)
estoque.anexar(alerta)

# Simulação de vendas
estoque.vender(5)
estoque.vender(10)
estoque.vender(2)
estoque.vender(83)  # Vai zerar o estoque
estoque.vender(1)   # Tentativa de vender quando o estoque é zero
estoque.quantidade = 101  # Atualizando a quantidade de pães para 101
estoque.vender(1)   # Tentativa de vender com quantidade inválida