Algoritmo tiposdevacunacovidRMSA
	Definir tipodevacuna ,sexo como entero
	Definir Edad como real
	//datos de entrada
	Escribir "ingrese su edad"
	Leer Edad
	escribir "ingrese su genero sexual"
	Leer sexo
	//proceso
	Si edad>=70 entonces
		Escribir "se le aplica la vacuna c";
	Sino si edad>=16 y edad  <=69 y sexo=1
		Escribir "se le aplica vacuna B";
	Sino si  edad>=16 y edad  <=69 y sexo=2
		Escribir "se le aplica vacuna A";
	Sino si edad <16 
		escribir "se le aplica vacuna A";
	Sino
	    Escribir "no se le aplica nada";                          
   FinSi
FinSi
FinSi
FinSi
//datos de salida
Escribir "si usted tiene ",edad," años y su sexo es ",sexo
FinAlgoritmo
