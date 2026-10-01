import requests
import time

def consumir_api_lmstudio(prompt):
    # Endpoint estándar que emula la API de OpenAI
    url = "http://localhost:1234/v1/chat/completions"
    
    payload = {
        "model": "phi-3-mini-4k-instruct", # Actualizado a tu modelo ligero actual
        "messages": [
            {"role": "system", "content": "Eres un ingeniero de software experto y conciso."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "stream": False 
    }
    
    print("Conectando a la API Local de LM Studio (Puerto 1234)...")
    inicio = time.time()
    
    try:
        respuesta = requests.post(url, json=payload)
        respuesta.raise_for_status()
        
        datos = respuesta.json()
        tiempo_total = time.time() - inicio
        
        # Navegación segura por el JSON de respuesta estilo OpenAI
        mensaje = datos.get("choices", [{}])[0].get("message", {}).get("content", "Sin respuesta")
        modelo_usado = datos.get("model", "Desconocido")
        
        print("\n=== RESPUESTA DEL MODELO ===")
        print(mensaje)
        
        print("\n=== REGISTRO TÉCNICO (EVIDENCIA) ===")
        print(f"Modelo ejecutado (según API): {modelo_usado}")
        print(f"Tiempo aproximado de respuesta: {tiempo_total:.2f} segundos")
        
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión. ¿Está encendido el Local Server en LM Studio? Detalle: {e}")

if __name__ == "__main__":
    print("--- PRUEBA LM STUDIO ---")
    consumir_api_lmstudio("Explica brevemente la diferencia entre un LLM y un modelo especializado en código.")