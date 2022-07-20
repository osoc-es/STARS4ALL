import calendar
from datetime import datetime

import ephem
import pandas as pd

import math

from typing import List




def data_to_date(time: str) -> tuple:
    date_string = ""
    for char in time:
        if len(date_string) < 19:
            if char == "T":
                date_string = date_string + " "
            else:
                date_string: str = date_string + char
    date_obj = datetime.fromisoformat(date_string)
    date = (date_obj.year, date_obj.month, date_obj.day, date_obj.hour, date_obj.minute, date_obj.second, 0)
    return date


def moon_position(lat, lon, fecha):
    home = ephem.Observer()
    home.lat, home.lon = lat, lon
    home.date = datetime(fecha[0], fecha[1], fecha[2], fecha[3], fecha[4], fecha[5])
    moon = ephem.Moon()
    moon.compute(home)
    return str(moon.alt)

def sunpos(when, location, refraction):
    year, month, day, hour, minute, second, timezone = when
    latitude, longitude = location
    rad, deg = math.radians, math.degrees
    sin, cos, tan = math.sin, math.cos, math.tan
    asin, atan2 = math.asin, math.atan2
    rlat = rad(latitude)
    rlon = rad(longitude)
    greenwichtime = hour - timezone + minute / 60 + second / 3600
    daynum = (367 * year- 7 * (year + (month + 9) // 12) // 4+ 275 * month // 9+ day- 730531.5+ greenwichtime / 24)
    mean_long = daynum * 0.01720279239 + 4.894967873
    mean_anom = daynum * 0.01720197034 + 6.240040768
    eclip_long = (mean_long + 0.03342305518 * sin(mean_anom) + 0.0003490658504 * sin(2 * mean_anom))
    obliquity = 0.4090877234 - 0.000000006981317008 * daynum
    rasc = atan2(cos(obliquity) * sin(eclip_long), cos(eclip_long))
    decl = asin(sin(obliquity) * sin(eclip_long))
    sidereal = 4.894961213 + 6.300388099 * daynum + rlon
    hour_ang = sidereal - rasc
    elevation = asin(sin(decl) * sin(rlat) + cos(decl) * cos(rlat) * cos(hour_ang))
    elevation = into_range(deg(elevation), -180, 180)
    if refraction:
        targ = rad((elevation + (10.3 / (elevation + 5.11))))
        elevation += (1.02 / tan(targ)) / 60
    return (round(elevation, 2))

def into_range(x, range_min, range_max):
    shiftedx = x - range_min
    delta = range_max - range_min
    return (((shiftedx % delta) + delta) % delta) + range_min

def despejado(tamb, tsky):
    return 100 - 3 * (tamb - tsky) < 40


def clear_sky(dataframe, i):
    return despejado(dataframe['tamb'][i], dataframe['tsky'][i])


def sun_elevation(dataframe, i):
    return sunpos(data_to_date(dataframe['tstamp'][i]), (dataframe['latitude'][i], dataframe['longitude'][i]), False)


def moon_altitude(dataframe, i):
    return moon_position(dataframe['latitude'][i], dataframe['longitude'][i], data_to_date(dataframe['tstamp'][i]))


def month(dataframe):
    middle = len(dataframe) / 2
    year = data_to_date(dataframe["tstamp"][middle])[0]
    month = data_to_date(dataframe["tstamp"][middle])[1]
    return calendar.month_abbr[month] + "_" + str(year)


def filtrado(dataframe, PATH):
    lista: List[int] = []

    for i in range(len(dataframe)):
        if dataframe['name'][i] is None or dataframe['tamb'][i] is None or dataframe['tsky'][i] is None or dataframe['mag'][i] is None or dataframe['mag'][i] is None or dataframe['tstamp'][i] is None or dataframe['latitude'][i] is None or dataframe['longitude'][i] is None:
            lista.append(i)
        elif sun_elevation(dataframe, i) > -18 or moon_altitude(dataframe, i)[0] != "-" or not clear_sky(dataframe, i):
            lista.append(i)

    dataframe_nuevo = dataframe.drop(lista)
    print(len(dataframe_nuevo))
    dataframe_nuevo.to_csv(f"{PATH}Stars4all-filter{month(dataframe)}.csv", index=False)

def stars4all_filtrado(file, PATH):
    dataframe = pd.read_csv(file, delimiter=",")
    filtrado(dataframe, PATH)

