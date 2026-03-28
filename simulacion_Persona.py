import random 

def generar_Personas():
    listaNombres = ["Pedro Picapiedra","John Lennon","David Bisbal","Gustavo Petro", "West Col"]

    listaEmails = ["picapiedro123@gmail.com", "johnlivent69@hotmail.com","dabal890@cesde.edu.co","mgustavo19@gmail.com","colWest6969@hotmail.com"]

    listaTelefonos = ["3156452345","3247809641","3126780978","3196756643","3272956578"]

    listaPersonas = []

    for _ in range(20):
        persona = {
            "id_persona" : random.randint(0,20),
            "nombreCompleto" : random.choice(listaNombres),
            "email" : random.choice(listaEmails),
            "telefono" : random.choice(listaTelefonos),
        }
        listaPersonas.append(persona)
    return listaPersonas
