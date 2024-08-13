# Created by: Tomas Contreras, student from BYU Idaho

import csv

def main():

    archivo_csv = 'ventas.csv'

    try:
        year = int(input("Ingrese el año a consultar: "))

    except ValueError: #Obliga al usuario a usar un año valido
        print("Por favor, ingrese un año válido.")
        return

    try:
        quantity = int(input("Ingrese la cantidad: "))

    except ValueError: #De esta manera obliga al usuario a ingresar un numero valido
        print("Por favor, ingrese un número válido.")
        return
    
    best_rank = top_rank(archivo_csv, year, quantity)

    if best_rank:
        for i, juego in enumerate(best_rank, start=1):
            print(f"{juego['Name']}")
    else:
        print("No se encontraron datos.")#En caso de numero invalido

def top_rank(archivo_csv, rank_year, quantity):
    videojuegos = []

    # Leer el archivo CSV
    with open(archivo_csv, mode='r', newline='') as file:
        reader = csv.DictReader(file)

        for row in reader:
            try: #funciones para saltar linea en caso de que no se encuentre INT, si existe un STR lo salta
                if int(row["Year"]) == rank_year:
                    total_sales = (float(row['NA_Sales']) + float(row['EU_Sales']) + 
                                   float(row['JP_Sales']) + float(row['Other_Sales']))
                    row['Total_Sales'] = total_sales
                    videojuegos.append(row)
            except ValueError: #En caso encontrar STR (N/A), lo salta
                
                continue

    # Ordenar por ventas totales (de mayor a menor)
    videojuegos.sort(key=lambda x: x['Total_Sales'], reverse=True)

    top_videogames = videojuegos[:quantity]

    return top_videogames

if __name__ == "__main__":
    main()