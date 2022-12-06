import requests

def get_veiculos():
    url = f'http://parallelum.com.br/fipe/api/v2/carros/brands'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    resposta_json = resposta.json()
    lista = resposta_json
    itlista = iter(lista)

    for resultado in itlista:
        print(f'Marcas: {resultado["name"]}')
        print(f'Código da Marca {resultado["code"]}')
        print('*'*30)

def modelos_veiculos(brand_id):
    url = (f'http://parallelum.com.br/fipe/api/v2/carros/brands/{brand_id}/models')

    headers = {'user-agent': 'MyStudyApp'}
    resposta = requests.get(url, headers=headers)
    resposta_json = resposta.json()
    lista = resposta_json
    itlista = iter(lista)

    for resultado in itlista:
        print(f'Modelo: {resultado["name"]}')
        print(f'Código do Modelo {resultado["code"]}')

def anos_modelo(id_marca, id_ano):
    url = f'http://parallelum.com.br/fipe/api/v2/carros/brands/{id_marca}/models/{id_ano}/years'

    headers = {'user-agent': 'MyStudyApp'}
    resposta = requests.get(url, headers=headers)
    resposta_json = resposta.json()
    lista = resposta_json
    itlista = iter(lista)

    for resultado in itlista:
        print(f'Modelo: {resultado["name"]}')
        print(f'Código do Modelo {resultado["code"]}')
    
def info_veiculos(marca, modelo, valor):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos/{modelo}/anos/{valor}'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    resposta_json = resposta.json()
    lista = resposta_json
    print(lista)

if __name__== '__main__':
    get_veiculos()
    
    marca = int(input('Digite o código da marca: '))
    brand_id = marca
    
    modelos_veiculos(brand_id)
    modelo = int(input('Digite o código do modelo: '))
    id_marca = marca
    id_ano = modelo
    anos_modelo(id_marca, id_ano)
    valor = str(input('Digite o código do modelo para consutar o valor: '))
    
    info_veiculos(marca, modelo, valor)

    
    
    
    
    
    

    
    
    
              
  