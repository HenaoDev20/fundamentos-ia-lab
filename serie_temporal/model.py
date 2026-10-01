from sklearn.linear_model import LinearRegression

def entrenar_y_predecir(train, test):
    # Baseline (Naive): El precio de hoy será igual al de ayer
    test['prediccion_baseline'] = test['precio_ayer']
    
    # Modelo Predictivo (Regresión Lineal)
    X_train, y_train = train[['precio_ayer']], train['precio']
    X_test = test[['precio_ayer']]
    
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Generar predicciones
    test['prediccion_modelo'] = modelo.predict(X_test)
    
    return test