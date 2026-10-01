import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error

def evaluar_y_graficar(train, test):
    y_test = test['precio']
    
    # Cálculo de métricas
    mae_base = mean_absolute_error(y_test, test['prediccion_baseline'])
    rmse_base = np.sqrt(mean_squared_error(y_test, test['prediccion_baseline']))
    
    mae_modelo = mean_absolute_error(y_test, test['prediccion_modelo'])
    rmse_modelo = np.sqrt(mean_squared_error(y_test, test['prediccion_modelo']))
    
    print("\n--- RESULTADOS DE LAS MÉTRICAS ---")
    print(f"BASELINE (Naive) -> MAE: ${mae_base:.2f} | RMSE: ${rmse_base:.2f}")
    print(f"MODELO (Regresión) -> MAE: ${mae_modelo:.2f} | RMSE: ${rmse_modelo:.2f}")
    
    # Visualización
    plt.figure(figsize=(12, 6))
    plt.plot(train.index, train['precio'], label='Entrenamiento (Real)')
    plt.plot(test.index, test['precio'], label='Prueba (Real)', color='black', linewidth=2)
    plt.plot(test.index, test['prediccion_baseline'], label='Baseline (Naive)', linestyle='--', alpha=0.7)
    plt.plot(test.index, test['prediccion_modelo'], label='Regresión Lineal', linestyle=':', color='red')
    
    plt.title('Análisis de Serie Temporal: Precio de Bitcoin (Últimos 365 días)')
    plt.xlabel('Fecha')
    plt.ylabel('Precio (USD)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()