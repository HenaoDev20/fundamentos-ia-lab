import requests
import time

# Cambié el modelo por defecto al nombre exacto que tienes instalado
def consumir_api_ollama(prompt, modelo="gemma4:latest"):
    url = "http://localhost:11434/api/generate"
    
    payload = {
        "model": modelo,
        "prompt": prompt,
        "stream": False # False para recibir toda la respuesta junta
    }
    
    print(f"Conectando a API Local (Modelo: {modelo})...")
    inicio = time.time()
    
    try:
        respuesta = requests.post(url, json=payload)
        respuesta.raise_for_status() 
        
        datos = respuesta.json()
        tiempo_total = time.time() - inicio
        
        print("\n=== RESPUESTA DEL MODELO ===")
        print(datos.get("response", "No se encontró respuesta."))
        
        print("\n=== REGISTRO TÉCNICO (EVIDENCIA) ===")
        print(f"Modelo ejecutado: {datos.get('model')}")
        print(f"Tiempo aproximado de respuesta: {tiempo_total:.2f} segundos")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión con Ollama. Detalle: {e}")

if __name__ == "__main__":
    # Prueba 1: Modelo generalista usando el nombre exacto de tu terminal
    print("--- PRUEBA 1: GENERALISTA ---")
    consumir_api_ollama("Explica brevemente qué es el patrón de arquitectura por capas.", modelo="gemma4:latest")
    
    print("\n" + "="*50 + "\n")
    
    # Prueba 2: Modelo de código que acabas de descargar
    print("--- PRUEBA 2: CÓDIGO ---")
    consumir_api_ollama("Escribe una función en JavaScript para filtrar números pares de un array.", modelo="qwen2.5-coder:1.5b")