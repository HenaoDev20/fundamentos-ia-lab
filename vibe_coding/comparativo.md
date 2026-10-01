# Comparativa Vibe Coding: Modelo Local vs. Cloud

## 1. El Reto (Prompt)
**Prompt utilizado:** "Escribe un script en Python que reciba una lista de direcciones IPv4, valide cuáles tienen un formato correcto y clasifique las válidas en su respectiva clase de red (A, B o C). El código debe ser eficiente y tener comentarios explicativos."

## 2. Ejecución Local (LM Studio - [phi-3-mini-4k-instruct])
* **Tiempo de respuesta:** [ total time =    7898.67 ms /    88 tokens]
* **Código generado:**
```python

import re

from ipaddress import IPv4Address, IPv4Network


def validate_ipv4(ip):

    """Validate if the given IP is a valid IPv4 address."""

    try:

        # Attempt to create an IPv4 object which will raise ValueError for invalid inputs

        ip = IPv4Address(ip)

        return True

    except ValueError:

        return False


def classify_by_cidr(ip):

    """Classify the given IP by its CIDR."""

    network = IPv4Network(ip + '/32')  # Add /32 to make it a single host for simplicity

    if network.is_global:  # Check if the address is globally unique (not reserved)

        return 'A'

    elif network.network_address in [IPv4Address('10.0.0.0'), IPv4Address('172.16.0.0'), IPv4Address('192.168.0.0')]:

        return 'B'

    else:

        return 'C'


def main():

    ip_list = ["192.168.1.1", "172.24.1.1", "10.0.0.1", "999.999.999.999"]  # Sample list of IPs

    valid_ips = {}


    for ip in ip_list:

        if validate_ipv4(ip):

            cidr_class = classify_by_cidr(ip)

            valid_ips.setdefault(cidr_class, []).append(ip)


    print("Valid IPs by Class:", valid_ips)


if __name__ == "__main__":

    main()

# Componente 3: Vibe Coding - Comparativa Local vs. Cloud

## 1. El Reto (Prompt)
**Prompt utilizado:** "Escribe un script en Python que reciba una lista de direcciones IPv4, valide cuáles tienen un formato correcto y clasifique las válidas en su respectiva clase de red (A, B o C). El código debe ser eficiente y tener comentarios explicativos."

## 2. Ejecución cloud
* **Herramienta:** Gemini
* **Modelo utilizado:** [gemini pro]
* **Tiempo de respuesta:** [3456.67 ms /    56 tokens]

### Código Generado (cloud)
```python
import ipaddress

def clasificar_ips(lista_ips):
    """
    Valida si son IPv4 correctas usando la librería nativa ipaddress 
    y las clasifica en Clase A, B o C.
    """
    resultados = {"Clase_A": [], "Clase_B": [], "Clase_C": [], "Invalidas_u_Otras": []}

    for ip_str in lista_ips:
        try:
            ip = ipaddress.IPv4Address(ip_str)
            primer_octeto = int(str(ip).split('.')[0])
            
            if 1 <= primer_octeto <= 126:
                resultados["Clase_A"].append(ip_str)
            elif 128 <= primer_octeto <= 191:
                resultados["Clase_B"].append(ip_str)
            elif 192 <= primer_octeto <= 223:
                resultados["Clase_C"].append(ip_str)
            else:
                resultados["Invalidas_u_Otras"].append(ip_str)
                
        except ipaddress.AddressValueError:
            # Atrapa errores si el string no es una IP (ej. "texto")
            resultados["Invalidas_u_Otras"].append(ip_str)
            
    return resultados

# --- Prueba ---
ips_de_prueba = ["10.0.0.1", "172.16.5.4", "192.168.1.25", "127.0.0.1", "999.999", "direccion_ip"]
reporte = clasificar_ips(ips_de_prueba)

for categoria, ips in reporte.items():
    print(f"{categoria.replace('_', ' ')}: {ips}")

   ## 4. Análisis Comparativo

| Criterio | Local (Phi-3-mini) | Cloud (Gemini Pro) |
| :--- | :--- | :--- |
| **Velocidad** | **~7.9s.** Lento, limitado por el hardware local. | **~2.0s.** Muy rápido, impulsado por servidores dedicados. |
| **Lógica de Redes** | **Incorrecta.** Confundió IPs públicas/privadas con las Clases (A, B, C). | **Precisa.** Aplicó la regla estándar validando el primer octeto. |
| **Calidad de Código** | Regular. Importó librerías innecesarias (`re`) y lógica frágil. | Excelente. Código limpio y uso óptimo de la librería `ipaddress`. |
| **Manejo de Errores** | Básico. Usa un `try-except` genérico. | Robusto. Captura excepciones específicas (`AddressValueError`). |

## 5. Conclusiones

* **Capacidad de Razonamiento:** Se evidenció una brecha importante; el modelo Cloud resolvió el problema técnico con precisión, mientras que el modelo local (SLM) falló en la teoría de redes.
* **Aplicabilidad:** Los modelos locales pequeños son excelentes para sintaxis rápida y trabajar sin internet. Sin embargo, para lógica de negocio estricta o arquitecturas complejas, los modelos en la nube (LLMs) siguen siendo la opción más confiable.