import random
from datetime import datetime, timedelta

def generar_procesos(numeroProcesos):
    
    listaEstadoProceso = ["Postulado", "filtrado", "en pruebas", "entrevista", "seleccionado", "rechazado"]
    listaObservaciones = ["Cumple con los requisitos", "Buen desempeño en pruebas", "Entrevista exitosa", "No cumple con el perfil"]
    
    fechaInicio = datetime(2026, 1, 1)
    
    procesos = []
    
    for _ in range(numeroProcesos):
        fecha = fechaInicio + timedelta(days=random.randint(0, 60))
        
        proceso = {
            "idProceso": random.randint(1, 100),
            "fecha": fecha.strftime("%Y/%m/%d"),
            "estadoProceso": random.choice(listaEstadoProceso),
            "observaciones": random.choice(listaObservaciones),
            "puntajePruebas": round(random.uniform(0, 100), 2)
        }

        # Inyección de errores 
        probabilidad = random.random()

        if probabilidad < 0.2:
            # Error: espacios en texto
            proceso["estadoProceso"] = " " + proceso["estadoProceso"] + " "
        
        elif probabilidad < 0.4:
            # Error: tipo incorrecto
            proceso["puntajePruebas"] = random.choice(["alto", None, "100"])
        
        elif probabilidad < 0.6:
            # Error: valores fuera de rango
            proceso["puntajePruebas"] = random.choice([-10, 150])
        
        elif probabilidad < 0.8:
            # Error: fecha mal formateada
            proceso["fecha"] = fecha.strftime("%d-%m")
        
        else:
            # Error: datos incompletos
            proceso["observaciones"] = None

        procesos.append(proceso)

    # 🔁 Duplicado intencional
    if len(procesos) >= 2:
        procesos.append(procesos[0].copy())

    return procesos