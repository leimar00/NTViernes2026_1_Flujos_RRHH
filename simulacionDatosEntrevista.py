import random

from datetime import datetime, timedelta

def generarEntrevista(numeroEntrevistas):

    Entrevistas=[]

    listaEntrevistador=["leimar_henao", "julian_mendez", "Alma_Marcela_gozo","Homero_sipson"]

    fechaInicio = datetime(2026,1,1)

    listaComentarios=["tiene conociemiento sobre todo lo requerido", "tiene conocimientos basicos en PY y necesita reforzar en React", "no cumple con los requisitos minimos para developer junior"]

    boolean=["true", "false"]
    for i in range(numeroEntrevistas):
        
        fecha=fechaInicio + timedelta(days=random.randint(0, 60))


        Entrevista={
            "id_entrevistador" : random.randint(0,100),
            "fecha": fecha.strftime("%y/%m/%d"),
            "entrevistador" : random.choice(listaEntrevistador),
            "comentarios" : random.choice(listaComentarios),
            "calificacion" : random.randint(1,5),
            "Aprobado" : random.choice(boolean)

        }

        #Inyectando errores controlados

        probabilidadError=random.random()

        if probabilidadError<0.1:
            Entrevista["entrevistador"]="123 " + Entrevista["entrevistador"]+"asdwawsdwa "
        elif probabilidadError<0.2:
            Entrevista["comentarios"]=random.choice(["queso", "aguacate", "peyeton"])
        elif probabilidadError<0.3:
            Entrevista["id_entrevistador"]=random.choice([-1,-10,-0,0,-5])
        elif probabilidadError<0.4:
            Entrevista["calificacion"]=random.choice([1,-10000,"sisas","epaLaArepa","aguadulce"])
        elif probabilidadError<0.5:
            Entrevista["fecha"]=fechaInicio.strftime("%d/%m")
        elif probabilidadError<0.6:
            Entrevista["Aprobado"]=None
        elif probabilidadError<0.7:
            Entrevista["Aprobado"]=random.choice(["aguapanela", 1234567890])
        elif probabilidadError<0.8:
            Entrevista["id_entrevistador"]=None
        elif probabilidadError<0.9:
            Entrevista["entrevistador"]=Entrevista["entrevistador"]+Entrevista["entrevistador"]

        

        Entrevistas.append(Entrevista)
    
    #simulacion de datos duplicados

    if len(Entrevistas)>=2:
        Entrevistas.append(Entrevistas[0].copy())



    print(Entrevistas)


generarEntrevista(2)

