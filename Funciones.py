
# Función para recodificar valores
def recodificar_data(data, variable, lista_valores, lista_recod):
    '''
    Esta función recibe el dataframe y listas con los valores a recodificar.

            Parameters:
                    a (DataFrame): DataFrame donde se realizará la recodificación.
                    b (str): Nombre de la variable donde se modificarán los datos.
                    c (list): Lista con una lista de valores a modificar agrupados según el nuevo criterio.
                    d (list): Lista con los nuevos valores. 
                    ** Ambas listas deben tener la misma cantidad de agrupaciones/categorias **

            Returns:
                    No returns
    '''
    for index, recod in enumerate(lista_recod):
        for key, value in data[variable].items():
            if value in lista_valores[index]:
                data[variable][key] = recod 


# Función para renombrar una columna
def rename_column(data, variable, newvar):
    '''
    Esta función recibe el dataframe y los nombres a modificar.

            Parameters:
                    a (DataFrame): DataFrame donde se realizará la modificación.
                    b (str): Nombre de la variable a modificar.
                    c (str): Nuevo nombre de la variable.

            Returns:
                    No returns
    '''
    data.rename(columns = {f'{variable}':f'{newvar}'}, inplace = True)
