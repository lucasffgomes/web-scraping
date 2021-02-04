# Web Scraping
Este repositório contém um script em Python3 que rastreia uma página HTML e extrai dados estruturados como informações de repositórios hospedados no Github, tecnologias usadas e uma visão geral do diretório do projeto.

## Requisitos
- Python 3.7 ou superior
- Biblioteca Python (BeautifulSoup4 4.9.3)

## Como instalar a biblioteca *BeautifulSoup*
Abra o interpretador do Python no CMD e digite o seguinte comando:
```
pip install beautifulsoup4
```
Após baixar e instalar os pacotes, o script funcionará normalmente.

## Atenção!
Antes de executar o script, preencha o arquivo na pasta raiz desse projeto chamado `repositories.txt` de acordo com o exemplo abaixo:
```
lucasffgomes/innout
lucasffgomes/App_Klimatos
```
Pode-se inserir quantos repositórios desejar, ao final o script irá gerar um arquivo de nome `result.txt` com as informações dos repositórios inseridos anteriormente.
Abra-o e verá todas as pesquisas feitas pelo script.

Críticas, comentários e sugestões por favor envie um e-mail para lucasffgomes@hotmail.com
