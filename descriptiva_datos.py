#!/usr/bin/env python3

#Carlos Bermudez 29668441 - Simulacion y modelos

import statistics as st
import csv
import matplotlib.pyplot as plt

def descriptiva_datos(file):
    with open(file, 'r') as f:
        
        lista = []
        alturas = []
        lector = csv.reader(f)
        # omite el encabezado
        #next(lector, None)

        for fila in lector:
            lista.append(list(map(float, fila)))

        for x in lista:
            alturas += x
        
        #print(f"Datos: {lista}")
        print("------------------------------------------------------------------------------------------------------------------------")
        print(f"Datos: {alturas}")
        print("------------------------------------------------------------------------------------------------------------------------")
        alturas.sort()
        print(f"1.Ordenar los datos(de menor a mayor): {alturas}")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("2.Medidas de Tendencia central")
        media = st.mean(alturas) #media 
        print(f"La media es: {media}")
        moda = st.mode(alturas) #moda 
        print(f"La mediana es: {moda}")
        mediana = st.median(alturas) #mediana
        print(f"La moda es: {mediana}")
        print("------------------------------------------------------------------------------------------------------------------------")
        print("3.Medidas de dispersion")
        varianza = st.variance(alturas) #varianza
        print(f"La varianza es: {varianza}")
        des_est = st.stdev(alturas) #desviacion estandar
        print(f"La desviacion estandar es: {des_est}")
        rango = alturas[len(alturas) - 1] - alturas[0]  #rango
        print(f"El rango es: {rango}")
        print("------------------------------------------------------------------------------------------------------------------------")

        #Graficas en Matplolib

        plt.hist(alturas, bins=[1.3,1.35,1.4,1.45,1.5,1.55,1.6,1.65,1.7,1.75,1.8,1.9,2],edgecolor='black')
        plt.xlabel('Estaturas')
        plt.ylabel('Veces que se repite')
        plt.title('Histograma de las estaturas')
        plt.show()


if __name__ == "__main__":
    file = 'datos1.csv'
    descriptiva_datos(file)