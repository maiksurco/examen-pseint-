Algoritmo calcularslarioincialdelprofesorRMSA
	Definir contadordea�os como entero
	Definir Valordel_10decada_a�o,salario_inicial como real
	Contadordea�os<-1
	Salario_inicial<-1400
	//datos de entrada y proceso
	Mientras contadordea�os<=6 hacer
		Escribir "ingrese los porcientos de (10%) de cada a�o "  ,contadordea�os          
		Leer  Valordel_10decada_a�o
		Salario_inicial<-salario_inicial+Valordel_10decada_a�o
		Contadordea�os<-contadordea�os+1
	finmientras
	//datos de salida
	Escribir "la suma de los porcentajes de los 6 a�os es : ",salario_inicial
	Escribir "salario del primer a�o es 140 $"
	Escribir "salario del segundo a�o es 154 $"
	Escribir "salario del terce a�o es 169 $"
	Escribir "salario de  cuarto a�o es 186 $"
	Escribir "salario del quinto a�o es 204 $"
	Escribir "salario del sexto a�o es 225 $"
FinAlgoritmo
