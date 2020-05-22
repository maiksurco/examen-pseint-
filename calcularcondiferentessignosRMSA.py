Algoritmo calcularcondiferentessignosRMSA
	Definir unidad1,unidad2,respuesta como real
	Definir tiposdesignos como entero 
	//datos de entrada
	Escribir "ingrese su primer numero"
	Leer unidad1
	Escribir "ingrese su segundo numero"
	Leer unidad2
	Escribir "ingrese el numero de signo que desea"
	Leer tiposdesignos
	//proceso
	Segun tiposdesignos hacer 
	1:respuesta<-unidad1+unidad2
	2: respuesta<-unidad1-unidad2
	3: respuesta<-unidad1/unidad2
	4: respuesta<-unidad1*unidad2 
	5: respuesta<-unidad1^unidad2
	De otro modo
		Escribir "no hay respuesta" 
	FinSegun
	//datos de salida
escribir " la respuesta es : ",respuesta 
FinAlgoritmo
