#!/usr/bin/env python
# -*- coding: utf-8 *-*

import MySQLdb

db_origen = MySQLdb.connect(host='localhost', user='root',
    passwd='local', db='audith')
db_destino = MySQLdb.connect(host='localhost', user='root',
    passwd='local', db='audith2')

cursor_origen = db_origen.cursor()
cursor_destino =  db_destino.cursor()

sql = 'SHOW TABLES;'
cursor_origen.execute(sql)
tablas = cursor_origen.fetchall()

for tabla in tablas:
    actual = tabla[0]
    
    sql = 'SHOW columns FROM ' + actual
    cursor_origen.execute(sql)
    columnas = cursor_origen.fetchall()
    
    sql = 'SELECT * FROM ' + actual
    cursor_origen.execute(sql)
    resultado = cursor_origen.fetchall()
    
    campos = ''
    
    for columna in columnas:
        campos = campos + str(columna[0]) + ', '
        
    campos = campos[:-2]
    
    valores = ''
    for reg in resultado:
        i = (len(reg))
        j = 0
        while (j < i):
            if reg[j] is None:
                valores = valores + "'0'" + ', '
            else:
                valores = valores + "'" + str(reg[j]) + "'" + ', '
            j = j + 1
        valores = valores[:-2]
        sql = 'INSERT INTO ' + actual + '(' + campos + ') VALUES' + ' (' + valores + ');'
        print sql
        cursor_destino.execute(sql)
        db_destino.commit()
        print "Number of rows inserted: %d" %cursor_destino.rowcount
        valores = ''
        
    sql = 'DELETE FROM ' + actual
    cursor_destino.execute(sql)
