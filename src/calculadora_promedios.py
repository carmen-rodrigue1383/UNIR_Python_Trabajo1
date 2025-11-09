import prompts
import mensajes_usuario as mensajes
import reports
from constants import CALIFICACION_MINIMA, CALIFICACION_MAXIMA, UMBRAL_APROBACION

class CalificacionInvalida(Exception):
    """Excepción personalizada para calificaciones fuera del rango permitido [0-10]"""
    pass

def ingresar_calificaciones():
    """Permite al usuario introducir el nombre de una materia y su calificación correspondiente

    Raises:
        CalificacionInvalida: Excepción personalizada para calificaciones inválidas (fuera del rango admitido).

    Returns:
        materias: lista de los nombres de las materias ingresadas por el usuario.
        calificaciones: lista de las calificaciones correspondientes a las materias ingresadas por el usuario.
    """        
    materias = []
    calificaciones = []
    while True:
        materia_o_fin = prompts.pedir_materia()        
        if not materia_o_fin:
            mensajes.mensaje_materia_invalida()
            confirmacion = prompts.pedir_confirmacion_finalizacion()
            if confirmacion.lower() == 's':
                break
            else:
                continue
        elif(materia_o_fin.strip().lower() == 'fin'):
            break
        else:
            materia = materia_o_fin.strip()
            calificacion_valida = False            
            while not calificacion_valida:
                calificacion_entrada = prompts.pedir_calificacion(materia)
                try:
                    calificacion = float(calificacion_entrada)
                    if(calificacion < CALIFICACION_MINIMA or calificacion > CALIFICACION_MAXIMA):
                        raise CalificacionInvalida(f"Calificación fuera de rango [{CALIFICACION_MINIMA},{CALIFICACION_MAXIMA}]")
                    materias.append(materia)
                    calificaciones.append(calificacion)
                    calificacion_valida = True
                except (ValueError, CalificacionInvalida) as e:        
                    mensajes.mensaje_calificacion_invalida(calificacion_entrada)
    return materias, calificaciones

def calcular_promedio(calificaciones):
    """Calcula el promedio de un listado de calificaciones

    Args:
        calificaciones (list): calificaciones para las que calcular el promedio

    Returns:
        promedio: promedio de las calificaciones aportadas
    """ 
    if(calificaciones == []):        
        mensajes.mensaje_sin_calificaciones_para_funcionalidad("calcular el promedio")
        return 0    
    try:
        promedio = sum(calificaciones) / len(calificaciones)
        return promedio 
    except:
        return 0

def determinar_estado(calificaciones, umbral = UMBRAL_APROBACION):
    """Dado un umbral de aprobación, determina qué materias están aprobadas y cuáles reprobadas.

    Args:
        calificaciones (list): calificaciones a evaluar
        umbral (float): umbral de aprobación (fijado por defecto en 5.0)

    Returns:
        aprobadas (list): lista con las materias aprobadas
        reprobadas (list): lista con las materias reprobadas
    """    
    aprobadas = []
    reprobadas = []
    if(calificaciones == []):        
        mensajes.mensaje_sin_calificaciones_para_funcionalidad("calcular aprobadas y reprobadas")        
    else:
        for i in range(len(calificaciones)):
            if calificaciones[i] >= umbral:
                aprobadas.append(i)
            else:
                reprobadas.append(i)    
    return aprobadas, reprobadas

def encontrar_extremos(calificaciones): 
    """Identifica los índices de la calificación más alta y la más baja de la lista de calificaciones recibida, y los devuelve.

    Args:
        calificaciones (list): lista de calificaciones

    Returns:
        extremos (dictionary): diccionario con los índices de las calificaciones más alta (mayor) y más baja (menor)
    """            
    if(calificaciones == []):        
        mensajes.mensaje_sin_calificaciones_para_funcionalidad("encontrar extremos")        
        return ({"mayor": 0, "menor": 0})
    else:
        mayor = max(calificaciones)
        menor = min(calificaciones)
        indice_mayor = calificaciones.index(mayor)
        indice_menor = calificaciones.index(menor)
        return { "mayor": indice_mayor, "menor": indice_menor } 
        
def main():
    """Función principal que orquesta la entrada de datos, el cálculo de promedios,
    la determinación de materias aprobadas y reprobadas, la identificación de extremos,
    y la generación del reporte final.
    """    
    materias, calificaciones = ingresar_calificaciones()

    if(materias == [] or calificaciones == []):
        mensajes.mensaje_sin_calificaciones_para_funcionalidad("generar reporte")
        return    

    promedio = calcular_promedio(calificaciones)
    aprobadas_indices, reprobadas_indices = determinar_estado(calificaciones)   
    aprobadas = {materias[i]: calificaciones[i] for i in aprobadas_indices}
    reprobadas = {materias[i]: calificaciones[i] for i in reprobadas_indices}
    extremos = encontrar_extremos(calificaciones)   
    mejor_materia = materias[extremos["mayor"]]
    mejor_calificacion = calificaciones[extremos["mayor"]]
    peor_materia = materias[extremos["menor"]]
    peor_calificacion = calificaciones[extremos["menor"]]

    reports.materias({
        'calificaciones_por_materia': {materias[i]: calificaciones[i] for i in range(len(materias))},
        'promedio': promedio,
        'aprobadas': aprobadas,
        'reprobadas': reprobadas,
        'mejor_materia': mejor_materia,
        'mejor_calificacion': mejor_calificacion,
        'peor_materia': peor_materia,
        'peor_calificacion': peor_calificacion
    })

if __name__ == "__main__":
    main()