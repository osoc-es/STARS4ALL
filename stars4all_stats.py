import datetime

import pandas as pd
import Stars4all

#para recoger estos datos es necesario que el dataframe haya sido filtrado
#para ello se debe pasar antes por el script que se encarga de realizar la función

def datos_mes(dataframe):
    fecha = (Stars4all.data_to_date(dataframe['tstamp'][1])[0], Stars4all.data_to_date(dataframe['tstamp'][1])[1],
             Stars4all.data_to_date(dataframe['tstamp'][1])[2])
    drop = []
    cambio_de_fecha = 0
    mes = []
    fotometro = []
    previous_name = dataframe['name'][1]
    for i in range(len(dataframe)):
        name = dataframe['name'][i]
        if name != previous_name:
            mes.append(fotometro)
            fotometro = []
        nueva = (Stars4all.data_to_date(dataframe['tstamp'][i])[0], Stars4all.data_to_date(dataframe['tstamp'][i])[1],
                 Stars4all.data_to_date(dataframe['tstamp'][i])[2])
        if fecha != nueva:
            fecha = nueva
            for j in range(0, cambio_de_fecha):
                drop.append(j)
            for j in range(i, len(dataframe)):
                drop.append(j)
            df_dia1 = dataframe.drop(drop)
            drop = []
            cambio_de_fecha = i
            fotometro.append(df_dia1)
            # df_dia1 = dataframe
        if i % 10000 == 0:
            print(i)
        previous_name = dataframe['name'][i]
    return mes


def datos_series(dataframe):
    lista_datos = []
    j = 0
    for k in datos_mes(dataframe):
        j += len(k)
        for i in k:
            fecha_fotometro = datetime.date(Stars4all.data_to_date(i['tstamp'][j - 1])[0],
                                            Stars4all.data_to_date(i['tstamp'][j - 1])[1],
                                            Stars4all.data_to_date(i['tstamp'][j - 1])[2])
            nombre_fotometro = dataframe['name'][j - 1]
            serie_estadisticas = i['mag'].describe()
            serie_nombre_fecha = pd.Series([nombre_fotometro, fecha_fotometro], index=['name', 'time'])
            serie_fotometro_dia = pd.concat([serie_nombre_fecha, serie_estadisticas])
            lista_datos.append(serie_fotometro_dia.to_dict())
    return lista_datos

def stats(file):
    dataframe_filtrado = pd.read_csv(file, delimiter=',')
    return datos_series(dataframe_filtrado)


