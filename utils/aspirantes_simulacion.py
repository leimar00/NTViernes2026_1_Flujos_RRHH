import random

from datetime import datetime,timedelta

def generar_simulacion_aspirantes(numeroSimulaciones):

    nombres_aspirantes=["Juan","María","Carlos","Ana","Pedro","Laura","Roberto","Sofia"]
    experiencias_lista=["Desarrollo web","Análisis de datos","Diseño gráfico","DevOps","QA Testing"]
    habilidades=["Python","JavaScript","SQL","React","Java","C++","Docker","AWS"]
    formacion=["Licenciatura en Informática","Bootcamp Full Stack","Técnico en Programación","Ingeniería de Sistemas"]
    
    fechaInicio=datetime(2026,1,2)

    simulaciones=[]
    for _ in range(numeroSimulaciones):

        simulacion={
            "id":random.randint(1,500),
            "nombre":random.choice(nombres_aspirantes),
            "anos_experiencia":random.randint(0,15),
            "experiencias":random.choice(experiencias_lista),
            "habilidades_tecnicas":random.choice(habilidades),
            "formacion_academica":random.choice(formacion),
            "fecha_solicitud":fechaInicio+timedelta(days=random.randint(0,60))
        }

        #Inyectando errores controlados 
        probabilidadError=random.random()
        if(probabilidadError<0.15):
            simulacion["id"]=None
        elif(probabilidadError<0.3):
            simulacion["nombre"]=random.choice(["123","@#$"])
        elif(probabilidadError<0.45):
            simulacion["anos_experiencia"]=random.choice([-5,None,1000])
        elif(probabilidadError<0.6):
            simulacion["experiencias"]=random.choice(["ventas","limpieza"])
        elif(probabilidadError<0.75):
            simulacion["habilidades_tecnicas"]=" "+simulacion["habilidades_tecnicas"].upper()
        elif(probabilidadError<0.85):
            simulacion["formacion_academica"]=random.choice(["primaria incompleta","sin estudio"])
        elif(probabilidadError<0.95):
            simulacion["fecha_solicitud"]=None

        simulaciones.append(simulacion)
    return simulaciones
