import random
from datetime import datetime, timedelta

def generar_procesos(numeroProcesos):
    
   # listaIdProceso=[100,200,300,400,500]
    listaEstadoProceso =["Postulado", "filtrado", "en pruebas","entrevista","seleccionado","rechazado"]
    listaObservaciones=[" Cumple con los requisitos", "Buen desempeño en pruebas", "Entrevista exitosa", "No cumple con el perfil "]
    
    fechaInicio= datetime(2026, 1, 1)   #Fecha de inicio para generar fechas aleatorias 
    
    procesos = []
    
    for _ in range(numeroProcesos):
        fecha=fechaInicio+timedelta(days=random.randint(0,60))  
        
        proceso={
            "idProceso":random.randint(0,100),
            "fecha":fecha.strftime("%Y/%m/%d"),
            "estadoProceso":random.choice(listaEstadoProceso),
            "observaciones":random.choice(listaObservaciones),
            "puntajePruebas":round(random.uniform(0, 100), 2)
        }
        procesos.append(proceso)    
    
    
    return procesos