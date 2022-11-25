import requests

def lista_marcas():

    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas'
    headers = {'user-agent': 'MyStudyApp'}

    resposta = requests.get(url, headers=headers)
    
    resposta_json = resposta.json()
    lista = resposta_json
    itlista = iter(lista)
    
    for marca in itlista:
        print(f'Código: {marca["codigo"].capitalize()}')
        print(f'Marca: {marca["nome"].capitalize()}')
        print('*' * 30) 

def get_veiculos(id_marcaseleciconada):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marcaseleciconada}/modelos'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200: 
        print('Houve um erro na requisição')
    resposta_json = resposta.json()
    return resposta_json['modelos']


class Fipe():
    def __init__(self, id_marcaseleciconada):
        self.id_marcaseleciconada = id_marcaseleciconada
        self.indice = 0
        self.modelos = []
    
    def __iter__(self):
        self.modelos = get_veiculos(self.id_marcaseleciconada)
        return self 

    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration
        else:
            modelo = self.modelos[self.indice]
            self.indice += 1
            return modelo


if __name__ == '__main__':
    lista_marcas()
    id_marcaseleciconada = ' '
    while id_marcaseleciconada == ' ':
        try:
            id_marcaseleciconada = int(input('DIGITE O CÓDIGO DA MARCA PARA COSULTAR OS MODELOS: '))
        except ValueError:
            print('VALOR INVÁLIDO')
        
    lista_fipe = Fipe(id_marcaseleciconada)   
    for veiculo in lista_fipe:
        print(veiculo['codigo'])
        print(veiculo['nome'])
        print('_________________')
        print('_________________')

