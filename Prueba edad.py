import pandas as pd
import seaborn as sb
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv("people_data_age.csv")

X_transformed = np.array(df[["Altura(mts)", "Edad(yr)"]])
Y_transformed = np.array(df["Peso(kg)"]).reshape(-1, 1)

# Visualización de los datos
sb.scatterplot(
    x="Altura(mts)", y="Peso(kg)", data=df, hue="Edad(yr)", palette="coolwarm"
)
plt.show()

modelo = LinearRegression()

modelo.fit(X_transformed, Y_transformed)

# Prueba de la predicción con dato conocido
altura = 1.70
edad = 24
prediction = modelo.predict([[altura, edad]])
print(
    f"La predicción es de: {prediction.item():.2f} kg para una persona de {altura} mts de altura y {edad} años"
)

# Prueba de la predicción con dato desconocido
height = 1.67
age = 23
peso_real = 53.338224
prediction_2 = modelo.predict([[height, age]])
desviacion = abs(prediction_2.item() - peso_real)
precision = 1 - desviacion / peso_real

print(
    f"La predicción es de: {prediction_2.item():.2f} kg para una persona de {height} mts de altura y {age} años"
)
print(f"La desviación del peso real es de: {desviacion:.2f} kg")

print(f"La precisión de la predicción es de: {precision:.2f}")

print(f"Exactitud del modelo: {modelo.score(X_transformed, Y_transformed)}")

# Resultados de peso y sesgo
# print(f"Peso: {modelo.coef_}")
# print(f"sesgo (Bias): {modelo.intercept_}")

# Las respuestas a las preguntas planteadas se encuentran en el README
