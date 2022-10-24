#!/usr/bin/env python3

#Carlos Bermudez 29668441 - Simulacion y modelos

import statistics as st
import csv

def descriptiva_datos(file):
    with open(file, 'r') as f:
        lector = csv.reader(f, delimiter = ",")
        # omite el encabezado
        next(lector, None)
        for fila in lector:
            estatura1 = float(fila[0])

        for i in range(len(fila)):
            fila[i] = float(fila[i])
        
        print(f"Datos: {fila}")
        print()
        fila.sort()
        print(f"1.Ordenar los datos(de menor a mayor): {fila}")
        print()
        print("2.Medidas de Tendencia central")
        media = st.mean(fila) #media 
        print(f"La media es: {media}")
        moda = st.mode(fila) #moda 
        print(f"La mediana es: {moda}")
        mediana = st.median(fila) #mediana
        print(f"La moda es: {mediana}")
        print()
        print("3.Medidas de dispersion")
        varianza = st.variance(fila) #varianza
        print(f"La varianza es: {varianza}")
        des_est = st.stdev(fila) #desviacion estandar
        print(f"La desviacion estandar es: {des_est}")
        rango = fila[len(fila) - 1] - fila[0]  #rango
        print(f"El rango es: {rango}")

if __name__ == "__main__":
    file = 'datos.csv'
    descriptiva_datos(file)