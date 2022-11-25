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

def get_veiculos(ID_MARCASELECIONADA):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{ID_MARCASELECIONADA}/modelos'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200: 
        print('Houve um erro na requisição')
    resposta_json = resposta.json()
    return resposta_json['modelos']


class Fipe():
    def __init__(self, ID_MARCASELECIONADA):
        self.ID_MARCASELECIONADA = ID_MARCASELECIONADA
        self.indice = 0
        self.modelos = []
    
    def __iter__(self):
        self.modelos = get_veiculos(self.ID_MARCASELECIONADA)
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
    ID_MARCASELECIONADA = 1
    lista_fipe = Fipe(ID_MARCASELECIONADA)   
    for veiculo in lista_fipe:
        print(veiculo['codigo'])
        print(veiculo['nome'])
        print('_________________')
        print('_________________')

