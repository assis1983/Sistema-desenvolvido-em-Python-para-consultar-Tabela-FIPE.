import requests
import os
from datetime import datetime

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
        print(f'*'*30)

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
        print('*'*30)
    
def info_veiculos(marca, modelo, valor):
    url = f'https://parallelum.com.br/fipe/api/v1/carros/marcas/{marca}/modelos/{modelo}/anos/{valor}'
    headers = {'user-agent': 'MyStudyApp'}
    
    resposta = requests.get(url, headers=headers)
    resposta_json = resposta.json()
    lista = resposta_json
    dados = [lista]
    for resultado in dados:
        print(f'Valor do veículo: {resultado["Valor"]}')
        print(f'Marca do veículo: {resultado["Marca"]}')
        print(f'Modelo do veículo: {resultado["Modelo"]}')
        print(f'Ano do veículo: {resultado["AnoModelo"]}')
        print(f'Combustível do veículo: {resultado["Combustivel"]}')
        print(f'Mês de Referência: {resultado["MesReferencia"]}')
        data_atual = datetime.now()
        data_consulta = data_atual.strftime('%d/%m/%Y %H:%M')
        print(f'Data da consulta: {data_consulta}')
        print('*'*30)

class Fipe():
    def __init__(self, brand_id):
        self.brand_id = brand_id
        self.indice = 0
        self.modelos = []
           
    def __iter__(self):
        self.modelos = get_veiculos(self.brand_id)
        return self 
    def __next__(self):
        if self.indice >= len(self.modelos):
            raise StopIteration
        else:
            modelo = self.modelos[self.indice]
            self.indice += 1
            return modelo

if __name__== '__main__':
    get_veiculos()
    
    marca = int(input('Digite o código da marca: '))
    brand_id = marca
    os.system('cls')
    modelos_veiculos(brand_id)
    modelo = int(input('Digite o código do modelo: '))
    id_marca = marca
    id_ano = modelo
    os.system('cls')
    anos_modelo(id_marca, id_ano)
    valor = str(input('Digite o código do modelo para consutar o valor: '))
    
    info_veiculos(marca, modelo, valor)

    
    
    
    
    
    

    
    
    
              
  