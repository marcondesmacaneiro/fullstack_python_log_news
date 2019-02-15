#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import psycopg2

DBNAME = "news"


# Consulta no Banco de Dados
def consulta_dados(consulta):
    """Buscando os dados"""
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(consulta)
    result = c.fetchall()
    db.close()
    return result


# Busca os artigos mais acessados no banco de dados
def artigoscontagem():
    result = consulta_dados("select title, views "
                            "from artigoscontagem limit 3")
    print('Os três artigos mais acessados são: ')
    print('')
    for title, views in result:
        print('"{title}" -- {views} Acessos'
              .format(title=title, views=views))


# Busca os autores mais populares
def popularidade():
    result = consulta_dados("select name, views from popularidade")
    print('Os autores mais populares são: ')
    print('')
    for name, views in result:
        print('"{name}" -- {views} Acessos'
              .format(name=name, views=views))


# Conta os erros de acesso por data
def logerro():
    result = consulta_dados("select data, erros from logerro "
                            "where erros > 1")
    print('Os dias em que mais de 1% das requisições '
          'resultaram em erros foram: ')
    print('')
    for data, erros in result:
        print('"{data}" -- {erros}'
              .format(data=data, erros=erros))


# Imprime os resultados
if __name__ == '__main__':
    artigoscontagem()
    print('')
    popularidade()
    print('')
    logerro()
