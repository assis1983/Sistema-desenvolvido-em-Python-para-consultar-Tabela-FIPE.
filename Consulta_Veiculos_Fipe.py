import requests
import os

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
        

def get_veiculos(id_marcaselecionada):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{id_marcaselecionada}/modelos'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    if resposta.status_code != 200: 
        print('Houve um erro na requisição')
    resposta_json = resposta.json()
    return resposta_json['modelos']

class Fipe():
    def __init__(self, id_marcaselecionada):
        self.id_marcaselecionada = id_marcaselecionada
        self.indice = 0
        self.modelos = []
           
    def __iter__(self):
        self.modelos = get_veiculos(self.id_marcaselecionada)
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
    
    id_marcaselecionada = int(input('DIGITE O CÓDIGO DA MARCA PARA COSULTAR OS MODELOS: '))
    os.system('cls')   
    lista_fipe = Fipe(id_marcaselecionada)   
    for veiculo in lista_fipe:
        print(f'Código do Veículo: {veiculo["codigo"]}')
        print(f'Nome do Veículo: {veiculo["nome"]}')

    
              
  