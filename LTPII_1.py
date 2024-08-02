class Veiculo(object): #superclasse
    def __init__(self, valor, modelo, km=0): #construtor com valor default
        self.valor = valor #atributos de instancia 
        self.modelo = modelo
        self.km = km
    def get_valor(self): #consulta
        return self.valor
    def get_modelo(self):
        return self.modelo
    def set_valor(self, novo_valor): 
        self.valor = novo_valor
class Carro(Veiculo): 
    def __init__(self, valor, modelo, km=1, qtd_portas=4): 
        super().__init__(valor, modelo, km) #chama construtor da superclasse
        self.qtd_portas = qtd_portas
    def get_qtd_portas(self): 
        return self.qtd_portas
    def set_qtd_portas(self, nova_qtd):
        self.qtd_portas = nova_qtd
if __name__ == '__main__' :
    c1 = Veiculo (100000.00, "Yaris", 20000)
    print("- Veiculo 1: ", c1)
    print(f'Valor: {c1.get_valor()}')
    print('Modelo: ', c1.get_modelo())
    c1.set_valor(110000.00)
    print(f'Valor alterado: {c1.get_valor()}')
    c2 = Carro(99000.00, "Civic", 1000, 4) #instancia de objeto na subclasse
    print('- Carro 1:\n', c2)
    print(f'valor: {c2.get_valor():.2f}')
    print('Modelo:', c2.get_modelo())
    print('Qtd.portas', c2.get_qtd_portas())
    c3 = Carro(99900, "Vectra")
    print('Carro 2:\n: ', c3)
    print(f'valor: {c3.get_valor()}')
    print('Modelo:', c3.get_modelo())
    print('Qtd.portas', c3.get_qtd_portas())