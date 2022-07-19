
from influxdb import InfluxDBClient
from datetime import datetime


#this funtion has the objetive to transform the analitics recived as list, 
# trnasform it in a json, so we can send it to influxdb

def Json_influxdb(list, database):

    client = InfluxDBClient('localhost', 8086)  #server at the localhost of influxdb
    client.switch_database(database)            #conection  to the database

    for i in list:                              #for loup that sends the data to influx

        json_payload = []   

        data = {"measurement" : "stadistics", 
            'tags': {
                "name" : i["Name"],
                },
            "time": i["time"],
            "fields": {
                "count" : i["count"],
                "mean" : i["mean"],
                "std" : i["std"],
                "min" : i["min"],
                "25%" : i["25%"],
                "50%" : i["50%"],
                "75%" : i["75%"],
                "max" : i["max"]
            }
        }

        json_payload.append(data)

        client.write_points(json_payload)