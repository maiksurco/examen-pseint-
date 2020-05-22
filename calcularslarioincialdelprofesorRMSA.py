Algoritmo calcularslarioincialdelprofesorRMSA
	Definir contadordeaños como entero
	Definir Valordel_10decada_año,salario_inicial como real
	Contadordeaños<-1
	Salario_inicial<-1400
	//datos de entrada y proceso
	Mientras contadordeaños<=6 hacer
		Escribir "ingrese los porcientos de (10%) de cada año "  ,contadordeaños          
		Leer  Valordel_10decada_año
		Salario_inicial<-salario_inicial+Valordel_10decada_año
		Contadordeaños<-contadordeaños+1
	finmientras
	//datos de salida
	Escribir "la suma de los porcentajes de los 6 años es : ",salario_inicial
	Escribir "salario del primer año es 140 $"
	Escribir "salario del segundo año es 154 $"
	Escribir "salario del terce año es 169 $"
	Escribir "salario de  cuarto año es 186 $"
	Escribir "salario del quinto año es 204 $"
	Escribir "salario del sexto año es 225 $"
FinAlgoritmo
