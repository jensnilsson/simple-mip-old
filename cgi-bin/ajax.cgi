#!/usr/bin/python2.7
# -*- coding: UTF-8 -*-

print "Content-type: text/html"
print ""

#print "test"
import cgitb
#cgitb.enable()

from solver import Solver
import cgi
import json

jsonInput = cgi.FieldStorage()

inputJSON = jsonInput["data"].value

y = Solver(inputJSON)

y.solve()
outputJSON = y.getJSONsolution()

print outputJSON

#jsonData = json.loads(outputJSON)
#solved = int(jsonData["solution"]["solved"])

#import MySQLdb

#db = MySQLdb.connect("", "", "", "")
#db_cursor = db.cursor()

#try:
#	insertString = """INSERT INTO problems (input, output, solved, reported) VALUES ('%s','%s',%i,%i)""" %(MySQLdb.escape_string(inputJSON),MySQLdb.escape_string(outputJSON),solved,0)
#	db_cursor.execute(insertString)
#	db.commit()
#except:
#	db.rollback()

#db_cursor.close()
#db.close()
