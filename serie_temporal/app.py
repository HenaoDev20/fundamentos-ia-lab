from api_client import obtener_datos_api
from preprocessing import preparar_serie_temporal
from model import entrenar_y_predecir
from evaluation import evaluar_y_graficar

def main():
    print("--- INICIANDO PIPELINE DE SERIES TEMPORALES ---")
    
    # 1. Extracción
    datos_crudos = obtener_datos_api()
    
    # 2. Transformación
    train, test = preparar_serie_temporal(datos_crudos)
    
    # 3. Modelado
    test_con_predicciones = entrenar_y_predecir(train, test)
    
    # 4. Evaluación
    evaluar_y_graficar(train, test_con_predicciones)

if __name__ == "__main__":
    main()