import random

from datetime import datetime,timedelta

def generar_candidatos(num_candidatos):
    candidatos = []
    lista_nombres = ["ana", "juan", "maria", "carlos", "luis", "sofia", "diego", "laura", "pedro", "lucia"]
    formacion_academica = [ "ingenieria", "medicina", "derecho", "arquitectura", "administracion", "psicologia", "economia", "educacion", "comunicacion", "arte"]
    años_experiencia = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    habilidades = ["programacion", "gestion de proyectos", "comunicacion", "trabajo en equipo", "liderazgo", "resolucion de problemas", "creatividad", "adaptabilidad", "pensamiento critico", "inteligencia emocional"]
    hoja_vida = ["experiencia laboral","educacion","habilidades","referencias personales","idiomas","estudios academicos"]
    calificacion = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    fechainicio= datetime(2026,1,1)

    for _ in range(num_candidatos):
        fecha: datetime=fechainicio + timedelta(days=random.randint(0,60))
        candidato = {
            "id": random.randint(1, 1000),
            "nombre": random.choice(lista_nombres),
            "formacion_academica": random.choice(formacion_academica),
            "años_experiencia": random.choice(años_experiencia),
            "habilidades": random.sample(habilidades, k=3),
            "hoja_vida": random.sample(hoja_vida, k=3),
            "calificacion": random.choice(calificacion)
        }
        candidatos.append(candidato)
    return candidatos
