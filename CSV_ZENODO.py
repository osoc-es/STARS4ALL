from importlib.metadata import files
from importlib.resources import path
from urllib import request
from wsgiref import headers
import requests
import json


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



        
    r = requests.get('https://sandbox.zenodo.org/api/deposit/depositions', params={'access_token': ACCESS_TOKEN})
    print(r.status_code)


    #Funtion Empy_File() has the objetive to test the API 
    # so we will be able to send usefull information next time.

    def Empty_File():

        r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions',
            params={'access_token': ACCESS_TOKEN},
            json={},
            headers=headers)
        print(r.status_code)
        print(r.json())
        return r
    
    #funtion Create_file is designed to upload the file selected 
    # to zenodo, at the access_token account

    def Create_file(Name):

        with open(path, "rb") as fp:
            r = requests.put(
                "%s/%s" % (bucket_url, Name),
                data=fp,
                params={'access_token': ACCESS_TOKEN}
            )
        print(r.json())
        print(r.status_code)


    #The funtion Open_File() helps us adapt the funtion to edit it
    # so we will be able to introduce information.

    def Open_File(Id):
        files = {'file': open(path, 'rb')}
        r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/%s/files' % Id ,params={'access_token': ACCESS_TOKEN}, data=data_new,files=files)
        print(r.status_code)


    #The funtion Edit_File allow us to edit the file 
    # and introduce any information we need.

    def Edit_File(Id, data):
        r = requests.put('https://sandbox.zenodo.org/api/deposit/depositions/%s' % Id,
        params={'access_token': ACCESS_TOKEN}, data=json.dumps(data),
        headers=headers)
        print(r.status_code)

    
    #And finally the funtion Publish_File publish 
    # the file stored at the users account.
    
    def Publish_File(Id):
        r = requests.post('https://sandbox.zenodo.org/api/deposit/depositions/%s/actions/publish' % Id,
                      params={'access_token': ACCESS_TOKEN} )
        print(r.status_code)

    
    #Execution of the funtions.

    p = Empty_File()

    deposition_id = p.json()['id']              #Identificator that allow us to access the file at our Zenodo account.              
    bucket_url = p.json()["links"]["bucket"]    #URL used to access the API file receptor.

    Create_file(filename)
    Open_File(deposition_id)
    Edit_File(deposition_id, data_new)
    Publish_File(deposition_id)

    #End of the funtion.



    

