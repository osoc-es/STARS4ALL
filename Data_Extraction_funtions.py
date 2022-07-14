from influxdb import InfluxDBClient
import csv
import time
import requests
from zipfile import ZipFile
from datetime import datetime
from dateutil.relativedelta import relativedelta

def date_automathic():
    date = datetime.today()
    date_st= date.strftime('%Y-%m-%dT00:00:00Z')
    past_date = date - relativedelta(months=1)
    past_date_st= past_date.strftime('%Y-%m-%dT00:00:00Z')
    return(date_st, past_date_st)

def work_flow(inicio,fin,path):
   
    def api_extraction(url):

       resp = requests.get(url,verify=False) #Realizamos la petición a la API donde estan los nombres de los fotometro
       posts = resp.json()
       photometers_good_keys={}
       for i in posts:
        photometers_good_keys[i['name']] = i
       return(photometers_good_keys)#Devuelve un diccionario una con los nombres como key , los values son los campos de la Api 
    
    def db_access(hostdb ,portdb,usernamedb,passworddb,database,start,end,name): #Solo te devuelve los datos de un fotometro(user)

        client = InfluxDBClient(host=hostdb, port=portdb, username=usernamedb, password=passworddb ,ssl=True, verify_ssl=True) #Accede a la base de datos mediante un cliente 
        client.switch_database(database)
        data_photometer=[]
        data_photometer = client.query("SELECT * FROM brushEvents WHERE time >= '"+ start +"' AND time <= '"+ end +"' AND \"user\" = '"+ name +"'") # Nos devuelve los datosl fotometros
         #con el nombre de user y metiendo la fecha de inicio y de fin
        data_photometer=list(data_photometer)[0]
        return(data_photometer)  #Devuelve los el apartado fields de los objetos en influxdb

    def csv_generator(data,name,user,dict,path): #Los datos deben ser de un solo fotometro (user) para añadir una cabecera con datos especificos 
        headers =[
      "# Community Standard Skyglow Data Format 1.0",
'# URL: https://www.darksky.org/wp-content/uploads/bsk-pdf-manager/47_SKYGLOW_DEFINITIONS.PDF',
'# Number of header lines: 35',
'# This data is released under the following license: ODbL 1.0 http://opendatacommons.org/licenses/odbl/summary/',
'# Device type: SQM-LE',
'# Instrument ID: Dahlem_tower_le',
#Aquí abajo añadimos a la cabecera la información correspondiente a su usuario en la Api
'# Data supplier: '+ str(dict[user]['tester'])+',https://api.stars4all.eu/photometers'
'# Location name: '+str( dict[user]['info_location']['country'])+'-'+str( dict[user]['info_location']['region'])+'-'+str( dict[user]['info_location']['town'])+'-'+str( dict[user]['info_location']['place']),
'# Position (lat, lon, elev(m)):'+str( dict[user]['info_location']['latitude'])+','+str( dict[user]['info_location']['longitude']) ,
'# Local timezone: ',
'# Time Synchronization: GPS',
'# Moving / Stationary position: STATIONARY',
'# Moving / Fixed look direction: FIXED'
'# Number of channels: 1',
'# Filters per channel: HOYA CM-500',
'# Measurement direction per channel: 0., 0.',
'# Field of view (degrees): 20',
'# Number of fields per line: 6',
'# SQM serial number: 1687',
'# SQM firmware version: 4-3-21',
'# SQM cover offset value: -0.11',
'# SQM readout test ix: i,00000004,00000003,00000021,00001687',
'# SQM readout test rx: r, 18.73m,0000000004Hz,0000130978c,0000000.284s, 031.2C',
'# SQM readout test cx: c,00000019.69m, 0000300.000s, 023.2C,00000008.71m, 029.3C',
'# Comment: ',
'# Comment: ',
'# Comment: ',
'# Comment: ',
'# Comment: ',
'# blank line 30',
'# blank line 31',
'# blank line 32',
'# UTC Date & Time, Local Date & Time, Temperature, Counts, Frequency, MSAS',
'# YYYY-MM-DDTHH:mm:ss.fff;YYYY-MM-DDTHH:mm:ss.fff;Celsius;number;Hz;mag/arcsec^2',
'# END OF HEADER']

        f=  open(path + '\\STARS4ALL'+str(name)+str('.csv'), mode='w') #Creamos el archivo y añadimos las cabeceras
        for i in headers:
            f.write(i +'\n')
        f.close()
        with open(path + '\\STARS4ALL'+str(name)+str('.csv'), mode='w',newline= '') as File: #Añadimos los parametros 
            writer = csv.writer(File)
            writer.writerow(['name , tamb , tsky , mag , tstamp , latitude , longitude'])    
            keys=['name','tamb','tsky','mag','tstamp','latitude','longitude']
        for i in data:
            writer.writerow([i[k]for k in keys]) 

    def csv_generator2(data,name,dict,path): #Los datos deben ser de todos los usuarios(data)

        writer.writerow(['name , tamb , tsky , mag , tstamp , latitude , longitude'])    

        for i in range(len(data)):
            data[i]['latitude']=dict[data[i]['user']]['latitude'] #Añadimos el apartado de latitud correspondiente al fotometro
            data[i]['longitude']=dict[data[i]['user']]['longitude'] #Añadimos el apartado de longitud correspondiente al fotometro

        with open(path + '\\STARS4ALL'+str(name)+str('.csv'), mode='w',newline= '') as File: #Añadimos los parametros 
            writer = csv.writer(File)   
            keys=['name','tamb','tsky','mag','tstamp','latitude','longitude']
            for i in data:
                writer.writerow([i[k]for k in keys])
            writer.close()


    dict= api_extraction('https://api.stars4all.eu/photometers')

    usuarios=[]
    for i in api_extraction('https://api.stars4all.eu/photometers'):
        usuarios.append(i)

    date_time_obj = datetime.strptime(inicio , '%Y-%m-%dT%H:%M:%SZ')
    name= date_time_obj.strftime('%Y-%B')

    for j in usuarios:
        name1= str(name)+str(j)
        csv_generator(b_access(hostdb ,portdb,usernamedb,passworddb,database,inicio,fin,j),name1,j,dict,path)

    f2= open(path + '\\STARS4ALL'+str(name)+str('.csv'), "w") #Creamos el archivo y añadimos las cabeceras
    f2.write('name , tamb , tsky , mag , tstamp , latitude , longitude'+'\n')
    f2.close()
    for j in usuarios:
        csv_generator2(b_access(hostdb ,portdb,usernamedb,passworddb,database,inicio,fin,j),name,dict,path)