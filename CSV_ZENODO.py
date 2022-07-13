from fileinput import close
from importlib.metadata import files, metadata
from importlib.resources import path
from logging import FileHandler, exception
from urllib import request
from wsgiref import headers
import requests
import json
import os
import logging

#This funtion is used to produce a usefull metadata array needed for the Upload_zenodo funtion
#able to edit at the will of the user.

def Metadata_builder(Title, Description, name, Affiliation, type):
    Data = {
        metadata:{
            'title' : Title,
            'upload_type' : type,
            'description' : Description,
            'creators' : [{'name' : name, 'affiliation' : Affiliation}]
        }
    }
    return Data


#This funtion has the objetive to upload any file to an account at the zenodo repertory, using 
# the folowing funtions we are able to access the API and create a publication, editing it 
# who ever we want, and after that publishing it.


def Upload_Zenodo(Token, Meta_Data, Path, Filename):

    


    # Variables introduced by user.

    ACCESS_TOKEN = Token    # Access key to zenodo profile
    path = Path             # Direction to file position
    data_new = Meta_Data    # Information needed for the documentation
    filename = Filename
    headers = {"Content-Type": "application/json"}
    logging.basicConfig( filename = 'C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\Loggers\\%s.txt' % filename, encoding='utf-8', level=logging.DEBUG, format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    r = requests.get('https://zenodo.org/api/deposit/depositions', params={'access_token': ACCESS_TOKEN})
    print(r.status_code)
    logging.info("API has been connected, Status 200")


    #Funtion Empy_File() has the objetive to test the API 
    # so we will be able to send usefull information next time.

    def Empty_File():

        r = requests.post('https://zenodo.org/api/deposit/depositions',
            params={'access_token': ACCESS_TOKEN},
            json={},
            headers=headers)
        
        if(r.status_code == 201):
            print(r.status_code)
            logging.info("Empty file created, Status 201")
            return r
        else:
            logging.info("Error at creating empty file")
            raise exception("There has been an error at accessing to the Id")
    
    #funtion Create_file is designed to upload the file selected 
    # to zenodo, at the access_token account

    def Create_file(Name):

        with open(path, "rb") as fp:
            r = requests.put(
                "%s/%s" % (bucket_url, Name),
                data=fp,
                params={'access_token': ACCESS_TOKEN}
            )
        if(r.status_code == 200):
            print(r.status_code)
            logging.info("File created, Status 200")
        else:
            logging.info("Error at creating File")
            raise exception("There has been an error at creating the file")
        
    #The funtion Edit_File allow us to edit the file 
    # and introduce any information we need.

    def Edit_File(Id, data):
        r = requests.put('https://zenodo.org/api/deposit/depositions/%s' % Id,
        params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
        headers=headers)
        if(r.status_code == 200):
            print(r.status_code)
            logging.info("Filed edited, Status 200")
        else:
            logging.info("Error at editing file")
            raise exception("There has been an error at editing the file")

    
    #And finally the funtion Publish_File publish 
    # the file stored at the users account.
    
    def Publish_File(Id):
        r = requests.post('https://zenodo.org/api/deposit/depositions/%s/actions/publish' % Id,
                      params={'access_token': ACCESS_TOKEN} )
        if(r.status_code == 202):
            print(r.status_code)
            logging.info("File publised, Status 202")
        else:
            logging.info("Error at publising file")
            raise exception("There has been an error at publising the file")

    
    #Execution of the funtions.
    try:

        p = Empty_File()

        deposition_id = p.json()['id']              #Identificator that allow us to access the file at our Zenodo account.   

        bucket_url = p.json()["links"]["bucket"]    #URL used to access the API file receptor.

        Create_file(filename)                       #We create the file
 
        Edit_File(deposition_id, data_new)          #we edit the file

        Publish_File(deposition_id)                #we publish the file

        logging.info("File upload to Zenodo successfully")

    except:
        print("The Scrip used to upload the file to Zenodo has failed")
        logging.info("Error at uploding to zenodo")

    close()
    #End of the funtion.