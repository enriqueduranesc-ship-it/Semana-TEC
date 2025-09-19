import pytesseract
pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import cv2 as cv

#Load data
#Va a ser incertada por otro colaborador

# Menu principal
def menu():
    print("Would you like to look for any question? \n",
                        "1) Gráfica de líneas del costo del agua \n",
                        "2) Total de agua consumida en $$ \n",
                        "3) Gráfica de Barras del costo del agua \n",
                        "4) Diferencia en costo con respecto al mes anterior \n",
                        "5) Exit")
    option = int(input("Choice: "))
    return option

# Función para gráfica de líneas del costo del agua
def lineas_costo_agua():
    # Datos temporales (serán reemplazados por la carga automática cuando se pueda)
    este_mes = float(input("¿Cuánto te cobró SIAPA este mes? $")) #Dato temporal
    mes_pasado = float(input("¿Cuánto te cobró SIAPA el mes pasado? $")) #Dato temporal
    dos_meses_atras = float(input("¿Cuánto te cobró SIAPA hace dos meses? $")) #Dato temporal
    
    # Crear listas para el gráfico
    meses = ['Hace 2 meses', 'Mes pasado', 'Este mes']
    costos = [dos_meses_atras, mes_pasado, este_mes] #Total de costos
    promedio = np.mean(costos) #Promedio de costos
    
    # Crear gráfica
    plt.figure(figsize=(10, 6))
    plt.plot(meses, costos, marker='o', linewidth=2, color='blue')
    
    # Agregar valores en cada punto
    for i, valor in enumerate(costos): #AGAIN
        plt.annotate(f'${valor:.0f}', (i, valor), textcoords="offset points", 
                    xytext=(0,10), ha='center')
    
    # Agregar línea de promedio
    plt.axhline(y=promedio, color='red', linestyle='--', alpha=0.7, 
                label=f'Promedio: ${promedio:.2f}')
    
    plt.title('Costo del Agua SIAPA - Últimos 3 Meses')
    plt.xlabel('Período')
    plt.ylabel('Costo ($)')
    plt.legend()
    plt.grid(True)
    plt.show()
    
    print(f"Costo promedio: ${promedio:.2f}")

# Función para total de agua consumida en pesos
def total_consumo_pesos():
    # Datos temporales (serán reemplazados por la carga automática)
    este_mes = float(input("¿Cuánto te cobró SIAPA este mes? $"))
    mes_pasado = float(input("¿Cuánto te cobró SIAPA el mes pasado? $"))
    dos_meses_atras = float(input("¿Cuánto te cobró SIAPA hace dos meses? $"))
    
    # Calcular total
    total = este_mes + mes_pasado + dos_meses_atras
    
    # Crear gráfica de torta
    meses = ['Hace 2 meses', 'Mes pasado', 'Este mes']
    costos = [dos_meses_atras, mes_pasado, este_mes]
    
    plt.figure(figsize=(8, 6))
    plt.pie(costos, labels=meses, autopct='$%.2f', startangle=90)
    plt.title(f'Distribución de Costos SIAPA\nTotal: ${total:.2f}')
    plt.show()
    
    print(f"Total gastado: ${total:.2f}")

# Función para gráfica de barras del costo
def barras_costo_agua():
    # Datos temporales (serán reemplazados por la carga automática)
    este_mes = float(input("¿Cuánto te cobró SIAPA este mes? $"))
    mes_pasado = float(input("¿Cuánto te cobró SIAPA el mes pasado? $"))
    dos_meses_atras = float(input("¿Cuánto te cobró SIAPA hace dos meses? $"))
    
    # Crear listas para el gráfico
    meses = ['Hace 2 meses', 'Mes pasado', 'Este mes']
    costos = [dos_meses_atras, mes_pasado, este_mes]
    
    # Crear gráfica de barras
    plt.figure(figsize=(8, 6))
    plt.bar(meses, costos, color='green')
    plt.title('Costo del Agua SIAPA por Mes')
    plt.xlabel('Período')
    plt.ylabel('Costo ($)')
    plt.show()
    
    max_costo = max(costos)
    mes_max = meses[costos.index(max_costo)]
    print(f"Mayor costo: ${max_costo:.2f} en {mes_max}")

# Función para diferencia en costo con mes anterior
def diferencia_costo_anterior():
    # Datos temporales (serán reemplazados por la carga automática)
    este_mes = float(input("¿Cuánto te cobró SIAPA este mes? $"))
    mes_pasado = float(input("¿Cuánto te cobró SIAPA el mes pasado? $"))
    dos_meses_atras = float(input("¿Cuánto te cobró SIAPA hace dos meses? $"))
    
    # Calcular diferencias
    diferencia_reciente = este_mes - mes_pasado
    diferencia_anterior = mes_pasado - dos_meses_atras
    
    # Crear gráfica de diferencias
    periodos = ['Mes pasado vs Hace 2 meses', 'Este mes vs Mes pasado']
    diferencias = [diferencia_anterior, diferencia_reciente]
    
    # Colores según si aumentó o disminuyó
    colores = ['red' if x < 0 else 'green' for x in diferencias]
    
    plt.figure(figsize=(10, 6))
    barras = plt.bar(periodos, diferencias, color=colores)
    
    # Agregar valores en cada barra
    for i, (barra, valor) in enumerate(zip(barras, diferencias)):
        plt.text(barra.get_x() + barra.get_width()/2, 
                barra.get_height() + (5 if valor > 0 else -10),
                f'${valor:+.2f}', 
                ha='center', va='bottom' if valor > 0 else 'top', fontweight='bold')
    
    plt.title('Diferencias de Costo Entre Meses')
    plt.xlabel('Comparación')
    plt.ylabel('Diferencia ($)')
    plt.axhline(y=0, color='black', linestyle='-', alpha=0.3)
    plt.show()
    
    print(f"Diferencia este mes vs mes pasado: ${diferencia_reciente:+.2f}")
    print(f"Diferencia mes pasado vs hace 2 meses: ${diferencia_anterior:+.2f}")

# Programa principal 
user_choice = 6

while user_choice > 5:
    
    choice = menu()
    
    # Opción 1: Gráfica de líneas del costo
    if choice == 1:
        lineas_costo_agua()
        print()
    
    # Opción 2: Total en pesos
    elif choice == 2:
        total_consumo_pesos()
        print()
    
    # Opción 3: Gráfica de barras del costo
    elif choice == 3:
        barras_costo_agua()
        print()
    
    # Opción 4: Diferencias en costo
    elif choice == 4:
        diferencia_costo_anterior()
        print()
    
    # Opción 5: Salir
    elif choice == 5:
        print("Saliendo del programa")
        break
    
    else:
        print("Por favor selecciona una opción válida")
        print()
