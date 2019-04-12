import unirest
import json

estudiantes = unirest.get("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json" })

print "Lista de Estudiantes: \n" + str(estudiantes.body)

matricula = 1
estudiante = unirest.get("http://localhost:4567/rest/estudiantes/" + str(matricula), headers={ "Accept": "application/json" })

print "Estudiante consultado: \n" + str(estudiante.body)

crearEstudiante = unirest.post("http://localhost:4567/rest/estudiantes/", headers={ "Accept": "application/json", "Content-Type": "application/json" }, params=json.dumps({ "nombre": "Jean", "correo": "jeanlemoine@practica7.com", "carrera": "ISC" }))
print "Estudiante nuevo creado: \n" + str(crearEstudiante.body)