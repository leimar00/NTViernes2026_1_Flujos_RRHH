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
            "calificacion" : random.randint(0,5),
            "Aprobado" : random.choice(boolean)

        }
        Entrevistas.append(Entrevista)
    return Entrevistas


generarEntrevista(10)

