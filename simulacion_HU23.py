import random
from datetime import datetime, timedelta  

def generar_servicio(numeroServicios):   
    listaNombres = ["Desarrollador Python", "Diseñador UX", "Data Analyst", "DevOps Engineer", "QA Tester"]   
    listaCargoString = ["TI", "Diseño", "Analytics", "Infraestructura", "Calidad"]    
    listaDescripcion = [
        "Desarrollar aplicaciones backend",
        "Crear interfaces de usuario",
        "Analizar datos empresariales",
        "Gestionar infraestructura cloud",
        "Pruebas de software"
    ]      
    listaRequisitos = [
        "5 años experiencia",
        "3 años experiencia",
        "2 años experiencia",
        "4 años experiencia",
        "1 año experiencia"
    ]
    listaEstados = ["ABIERTA", "CERRADA", "EN_PAUSA"]
    listaSalarios = [2500.0, 3000.0, 2800.0, 3500.0, 2200.0]
    
    fecha_inicio = datetime(2023, 1, 1)  
    vacantes = [] 
    
    for i in range(numeroServicios):    
        fecha_vacante = fecha_inicio + timedelta(days=random.randint(0, 365))   
        vacante = {     
            "id": random.randint(1, 5000),     
            "titulo_log": random.choice(listaNombres),    
            "tituloCargo": random.choice(listaCargoString),     
            "descripcion": random.choice(listaDescripcion),
            "requisitosMinimos": random.choice(listaRequisitos),
            "estadoVacante": random.choice(listaEstados),
            "abierta_cerrada_en_pausa": random.choice(listaEstados),
            "presupuestoSalario": random.choice(listaSalarios),
            "fecha_vacante": fecha_vacante.strftime("%Y-%m-%d")     
        }
        
        #Inyectando errores controlados en nuestra base de datos
        #Proceso estocástico
        probabilidadError = random.random()

        if probabilidadError <0.1:
            vacante["titulo_log"] = " "+vacante["titulo_log"]+" "
        elif probabilidadError < 0.2:
            vacante["descripcion"] = None
        elif probabilidadError < 0.3:
            vacante["id"] = random.choice([-1,-10,0])
        elif probabilidadError < 0.4:
            vacante["presupuestoSalario"] = random.choice([1, -10000, "sisas"])
        elif probabilidadError < 0.5:
            vacante["presupuestoSalario"] = str(vacante["presupuestoSalario"]) + f"{random.choice(["f","r","t"])}"
        elif probabilidadError < 0.6:
            vacante["titulo_log"] = None
        elif probabilidadError < 0.7:
            vacante["id"] = None
        vacantes.append(vacante)
        if len(vacantes) >= 2:
            vacantes.append(vacantes[0].copy())
    
    return vacantes

# Uso:
vacantes = generar_servicio(10)
for v in vacantes:
    print(v)