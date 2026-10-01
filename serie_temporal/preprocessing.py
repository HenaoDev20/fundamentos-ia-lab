import pandas as pd

def preparar_serie_temporal(datos):
    df = pd.DataFrame(datos, columns=['timestamp', 'precio'])
    df['fecha'] = pd.to_datetime(df['timestamp'], unit='ms')
    df.set_index('fecha', inplace=True)
    df.drop(columns=['timestamp'], inplace=True)
    
    # Variable de rezago (Lag 1) para predecir
    df['precio_ayer'] = df['precio'].shift(1)
    df.dropna(inplace=True)
    
    # División de datos (80% Entrenamiento, 20% Prueba)
    corte = int(len(df) * 0.8)
    train = df.iloc[:corte].copy()
    test = df.iloc[corte:].copy()
    
    return train, test