#!/usr/bin/python
# -*- coding: utf-8 -*-
 
import os
import zeep
from zeep import Client


wsdl ="http://localhost:7777/ws/AcademicoWebService?wsdl"
client = zeep.Client(wsdl=wsdl)




 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear') # NOTA para windows tienes que cambiar clear por cls
	print ("Selecciona una de las siguientes opciones")
	print ("\t1 Listar todos los estudiantes")
	print ("\t2 Consultar una asignatura")
	print ("\t3 Consultar un profesor")
	print ("\t9 - salir")
 
 
while True:
	# Mostramos el menu
	menu()
 
	# solicituamos una opción al usuario
	opcionMenu = input("Digite la opcion que desea: ")
 
	if opcionMenu=="1":
		#Listar todos los estudiantes
		print (client.service.getAllEstudiante())
		input("Has pulsado la opcion de listar todos los estudiantes ...\npulse enter para continuar")
	elif opcionMenu=="2":
		#Consultar una asignatura
		print (client.service.getAsignatura(1).nombre)
		input("Has pulsado opcion de consultar una asignatura...\npulse enter para continuar")
	elif opcionMenu=="3":
		#Consultar un profesor
		print (client.service.getProfesor('123123').nombre)
		input("Has pulsado opcion de consultar un profesor...\npulse enter para continuar")
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")