from ast import Del
from datetime import date
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


final , inicio = date_automathic()
date_time_obj = datetime.strptime(inicio , '%Y-%m-%dT%H:%M:%SZ')
name= date_time_obj.strftime('%Y-%B')#Esto te debuelve el año y el mes de la fecha de inicio que le pasas a la funcion

Access_Token = 'p25CSlnib5XnUTzEzgXNphLL4RzUwp23SF4YBhu8jMrq41xO5hboH6roEv1d'
Filename_Row = 'stars4all-Row-%s' % name
Filename_Final = 'stars4all-Final-%s' % name
Filename_Mensual = 'stars4all-mensual-%s' % name
Title_Row = 'Stars4All_%s_Row' % name
Title_Final = 'Stars4All_%s_Final' % name
Title_Mensual = 'Stars4All_%s_Mensual' % name
Description = 'Tester for Stars4All'
name = 'Daniel Moreno'
Affiliation = 'OSOC'
Type = 'poster'
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

path_row = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s.zip" % name
path_final = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s.zip" % name
path_mensual = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV" 

def Create_Files():
    os.mkdir("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    os.mkdir("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")

def File_Zip(Filename):
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")
def UPload_files():
    Upload_Zenodo(Access_Token, meta_data_Row, path_row, Filename_Row)
    Upload_Zenodo(Access_Token, meta_data_Final, path_final, Filename_Final)
    Upload_Zenodo(Access_Token, meta_data_Mensual, path_mensual, Filename_Mensual)

def Delete_files(name):
    remove("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s.zip" % name)
    remove("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s.zip" % name)
    shutil.rmtree("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    shutil.rmtree("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")
    remove("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\%s.csv" % name)


Create_Files()

work_flow(inicio, final,"C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV"  ,"C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")

File_Zip(name)

UPload_files()

Delete_files(name) 

