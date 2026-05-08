import random 

def generar_Personas(numPersonas):
    listaNombres = ["Pedro Picapiedra","John Lennon","David Bisbal","Gustavo Petro", "West Col"]

    listaEmails = ["picapiedro123@gmail.com", "johnlivent69@hotmail.com","dabal890@cesde.edu.co","mgustavo19@gmail.com","colWest6969@hotmail.com"]

    listaTelefonos = ["3156452345","3247809641","3126780978","3196756643","3272956578"]

    listaPersonas = []

    for _ in range(numPersonas):
        persona= {
            "id_persona" : random.randint(0,20),
            "nombreCompleto" : random.choice(listaNombres),
            "email" : random.choice(listaEmails),
            "telefono" : random.choice(listaTelefonos),
        }

        #Inyectando errores controlados en nuestra base de datos
        #Proceso estocástico
        probabilidadError = random.random()

        if probabilidadError <0.1:
            persona["nombreCompleto"] = " "+persona["nombreCompleto"]+" "
        elif probabilidadError < 0.2:
            persona["email"] = None
        elif probabilidadError < 0.3:
            persona["id_persona"] = random.choice([-1,-10,0])
        elif probabilidadError < 0.4:
            persona["telefono"] = random.choice([1, -10000, "sisas"])
        elif probabilidadError < 0.5:
            persona["telefono"] = persona["telefono"] + f"{random.choice(["f","r","t"])}"
        elif probabilidadError < 0.6:
            persona["nombreCompleto"] = None
        elif probabilidadError < 0.7:
            persona["id_persona"] = None


        listaPersonas.append(persona)

        if len(listaPersonas) >= 2:
            listaPersonas.append(listaPersonas[0].copy())


    return listaPersonas


print(generar_Personas(5))
