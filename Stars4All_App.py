from ast import Del
from datetime import datetime
from os import remove
import CSV_ZENODO
from CSV_ZENODO import Upload_Zenodo
import zipfile
import shutil
import os
import datetime
import Data_Extraction_funtions
from Data_Extraction_funtions import work_flow
from Data_Extraction_funtions import date_automathic
import sys

#Pricipal Funtion, it iniciate all funtions and create all variables, 
# it has the job to download the csv, filter them, create paths to save the data,
#  and send them to the zenodo profile

def Stars4all_app(start, final):       
                                                     
    #This part creates a name out of the start time, so we can use it as title for the csv
    date_time_obj = datetime.datetime.strptime(start , '%Y-%m-%dT%H:%M:%SZ')
    name= date_time_obj.strftime('%Y-%B')                
                                   
    #variables used for uploading the files to zenodo 
    Access_Token = 'p25CSlnib5XnUTzEzgXNphLL4RzUwp23SF4YBhu8jMrq41xO5hboH6roEv1d'          
    Filename_Row = 'stars4all-Row-%s' % name
    Filename_Final = 'stars4all-Final-%s' % name
    Filename_Mensual = 'stars4all-mensual-%s' % name

    #variables needed for the mata_data cration later on
    Title_Row = 'Stars4All_%s_Row' % name                                               
    Title_Final = 'Stars4All_%s_Final' % name
    Title_Mensual = 'Stars4All_%s_Mensual' % name
    Description = 'Tester for Stars4All'
    name = 'Daniel Moreno'
    Affiliation = 'OSOC'
    Type = 'poster'

    #Meta_data for every uploading file at zenodo
    meta_data_Row = {                                                                   
        'metadata': {
                'title': Title_Row,
            'upload_type': Type,
            'description': Description,
            'creators': [{'name': name,
                        'affiliation': Affiliation}] } }

    meta_data_Final = {
        'metadata': {
                'title': Title_Final,
            'upload_type': Type,
            'description': Description,
            'creators': [{'name': name,
                        'affiliation': Affiliation}] } }
    meta_data_Mensual = {
        'metadata': {
                'title': Title_Mensual,
            'upload_type': Type,
            'description': Description,
            'creators': [{'name': name,
                        'affiliation': Affiliation}] } }

    #Declaration of the funtions that will be needed

    #This funtion Creates files so we can store the CSVs there and have a more clean Disk
    #thi will help later to create zip files

    def Create_Files():
        os.mkdir("/home/osoc22/Final")
        os.mkdir("/home/osoc22/Raw")

    #This funtion transform the files created before to zip, so we can send them to zanodo more easelly

    def File_Zip(Filename):
        shutil.make_archive("/home/osoc22/Star4All-FinalData-%s" % Filename, ".zip", "/home/osoc22/Final")
        shutil.make_archive("/home/osoc22/Star4All-RawData-%s" % Filename, ".zip", "/home/osoc22/Raw")

    #This funtion incorporate all the callings to the zenodo api to upload the files

    def UPload_files():
        Upload_Zenodo(Access_Token, meta_data_Row, path_row, Filename_Row)
        Upload_Zenodo(Access_Token, meta_data_Final, path_final, Filename_Final)
        Upload_Zenodo(Access_Token, meta_data_Mensual, path_mensual, Filename_Mensual)

    #Funtion that allows to delete the files and zip that we created before, 
    # this helps clean the computer and not stack unecessary data

    def Delete_files(name):
        remove("/home/osoc22/Star4All-RawData-%s.zip" % name)
        remove("/home/osoc22/Star4All-FinalData-%s.zip" % name)
        shutil.rmtree("/home/osoc22/Final")
        shutil.rmtree("/home/osoc22/Raw")
        remove("/home/osoc22/%s.csv" % name)

    #Calling of the funtion that creates the files for the CSV
    Create_Files()                       

    #calling of the funtion that downloads the data from the data_base, and send it to the paths
    work_flow(start, final,"/home/osoc22/Final" ,"/home/osoc22/Raw")

    #Calling of the funtion that transform the files to zips                                                                                
    File_Zip(name)                                             

    #creation of the path to the zips created before
    path_row = "/home/osoc22/Star4All-RawData-%s.zip" % name        
    path_final = "/home/osoc22/Star4All-FinalData-%s.zip" % name

    #Creation of the path for the mensual CSV
    path_mensual = "/home/osoc22"  

    #Calling of the funtion that uploads the files to the zenodo account
    UPload_files()                                                     

    #calling of the funtion that daletes the files and the zips
    Delete_files(name)  

    #End of the funtion                                                                                                 


#This part allows us to choose if we want to Call the funtion automatic or manual, 
# in case it doesnt work automatic

if(len(sys.argv) == 2):
    Stars4all_app(sys.argv[0], sys.argv[1])
else:
    final_automatic , start_automatic = date_automathic()
    Stars4all_app(start_automatic, final_automatic)


