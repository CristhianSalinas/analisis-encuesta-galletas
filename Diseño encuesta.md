## Demograficas
sexo Tipo=RU
    _1 Masculino
    _2 Femenino
    _3 Otro
    Nota= rotar _1 y _2. mantener Otro al final de la fila

EdadNum Tipo=Abierta numerica
    _1 ingrese su edad (Numerica abierta) 
    _2 No quiero contestar *Finalizar
    Nota= FINALIZAR si se menor a 18 o mayor a 55

Region: ¿En que Ciudad Vive? Tipo=RU
    _1 Bogotá
    _2 Medellin
    _3 Bucaramanga
    Nota= si no seleccionan Bogotá FINALIZAR ENTREVISTA

## Bloque 2 Familiaridad
BD1: ¿Que tipo de galletas conoces? Tipo=Abierta
    Nota= Hacer una caja de texto.

FAM: ¿Cononce el producto? Tipo=Loop/DragandDrop
    Nunca_la_he_oido
    He_oido_pero_nunca_la_he_probado
    La_he_probado 

     Galletas:
        Galleta_Chocolate
        Galleta_Avena 
        Galleta_Mani
           
    Nota= Hacer que pueda arrastrar la respuesta en las casillas, Si selecciona todas en no he oido o escuchado FINALIZAR  
        Marcas conocidas =   He oido pero nunca la he probado ó La he probado 
        Marcas Probadas = La he probado

be1:en una escala de 10 a 1 donde 10 es bueno y uno es malo, que sabor es mejor.
    _1 10
    _2 9
    _3 8
    _4 7
    _5 6
    _6 5
    _7 4
    _8 3 
    _9 2
    _10 1

     Galletas:
        Galleta_Chocolate
        Galleta_Avena 
        Galleta_Mani
    Nota = Para las marcas conocidas como FAM, hacer las siguientes preguntas Dragand drop, mostrar el tipo de galleta y que se puedan arrastrar, hacer casillas para la escala.

Preferencia: ¿Que galleta Prefieres?  Tipo=RU
        Galleta_Chocolate
        Galleta_Avena 
        Galleta_Mani
    
LugarCS: ¿Donde a Probado las siguientes Galletas *Respuesta Marcas Probadas en FAM? Tipo= loop/RM
    Centro_comercial
    Panaderia_Cafeteria
    Otro
    Nota = Rotar respuestas







