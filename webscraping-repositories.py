#!usr/bin/python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup


def ler_arquivo():
    arquivo = open('repositories.txt')

    conteudo = arquivo.read()
    conteudo = conteudo.split('\n')

    for linha in conteudo:
        nome_repositorio = linha

        listar_linguagens(nome_repositorio)


def listar_linguagens(nome_repositorio):
    link = urlopen(f'https://github.com/{nome_repositorio}')
    linguagens = BeautifulSoup(link.read(), "html.parser")

    with open('result.txt', 'a') as resultado:
        resultado.write(f'[Projeto: {nome_repositorio}]' + '\n' + '\n')

    for i in linguagens.find_all('a', {'class': 'd-inline-flex flex-items-center flex-nowrap link-gray '
                                                'no-underline text-small mr-3'}):
        nome_linguagem = i.find_all('span')

        with open('result.txt', 'a') as resultado:
            resultado.write(f'{nome_linguagem[0].text}: {nome_linguagem[1].text}')
            resultado.write('\n')

    with open('result.txt', 'a') as resultado1:
        resultado1.write("\n")
        (listar_pastas(nome_repositorio))
        resultado1.write("-----------------------------------" + '\n')


def listar_pastas(nome_repositorio):
    link = urlopen(f'https://github.com/{nome_repositorio}')
    geral = BeautifulSoup(link.read(), "html.parser")

    with open('result.txt', 'a') as resultado:
        resultado.write("\n")
        resultado.write(f'[{nome_repositorio}]' + '\n')

    for diretorio in geral.find_all('a', {'class': 'js-navigation-open link-gray-dark'}):

        with open('result.txt', 'a') as resultado:
            resultado.write(f"|__ [{diretorio.text}]")
            resultado.write('\n')

        listar_subpastas(diretorio)


def listar_subpastas(diretorio):
    sub_link = urlopen(f"https://github.com{diretorio.get('href')}")
    sub_nivel = BeautifulSoup(sub_link.read(), 'html.parser')

    for sub_diretorio in sub_nivel.find_all('a', {'class': 'js-navigation-open link-gray-dark'}):
        with open('result.txt', 'a') as sub_resultado:
            sub_resultado.write(f"|   |__ [{sub_diretorio.text}]" + "\n")

        sub_link2 = urlopen(f"https://github.com{diretorio.get('href')}/{sub_diretorio.text}")
        sub_nivel = BeautifulSoup(sub_link2.read(), 'html.parser')

        for sub_diretorio2 in sub_nivel.find_all('a', {'class': 'js-navigation-open link-gray-dark'}):
            with open('result.txt', 'a') as sub_resultado:
                sub_resultado.write(f"|   |   |__ [{sub_diretorio2.text}]" + '\n')

            sub_link3 = urlopen(f"https://github.com{diretorio.get('href')}/{sub_diretorio.text}/{sub_diretorio2.text}")
            sub_nivel1 = BeautifulSoup(sub_link3.read(), 'html.parser')

            for sub_diretorio3 in sub_nivel1.find_all('a', {'class': 'js-navigation-open link-gray-dark'}):
                with open('result.txt', 'a') as sub_resultado1:
                    sub_resultado1.write(f"|   |   |   |__ [{sub_diretorio3.text}]" + '\n')


ler_arquivo()

