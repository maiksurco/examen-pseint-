Algoritmo calcularelsalariominimoRMSA
	Definir puntos ,salario ,premio como real
	//datos de entrada
	Escribir "ingrese el salario minimo "
	Leer salario
	Escribir "ingrese cuantos puntos consiguio"
	Leer puntos
	//proceso
	Si puntos >=20 y puntos<=100 entonces
	Premio<-salario/10
	Sino si puntos >=101 y puntos<=200 
		Premio<-salario/2
	Sino  si puntos >=201
		Premio <-salario 
	FinSi
FinSi
finsi
//datos de salida 
escribir "si el salario es : ",salario , " y tienes ",puntos, " puntos recibiras ",premio ," $ "
FinAlgoritmo