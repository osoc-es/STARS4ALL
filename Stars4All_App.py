from ast import Del
from os import remove
import CSV_ZENODO
from CSV_ZENODO import Upload_Zenodo
from Date_Creater import current_date_format
import zipfile
import shutil
import os
import Funciones_extración_datos


Time = current_date_format()

Access_Token = 'p25CSlnib5XnUTzEzgXNphLL4RzUwp23SF4YBhu8jMrq41xO5hboH6roEv1d'
Filename_Row = 'stars4all-Row-%s' % Time
Filename_Final = 'stars4all-Final-%s' % Time
Title_Row = 'Stars4ll_Tester_Row'
Title_Final = 'Stars4ll_Tester_Final'
Description = 'Tester for Stars4All'
name = 'Daniel Moreno'
Affiliation = 'OSOC'
Type = 'poster'
testeo = "test"

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
path_row = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s.zip" % testeo
path_final = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s.zip" % testeo

def Create_Files():
    os.mkdir("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    os.mkdir("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")

def File_Zip(Filename):
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")
def UPload_files():
    Upload_Zenodo(Access_Token, meta_data_Row, path_row, Filename_Row)
    Upload_Zenodo(Access_Token, meta_data_Final, path_final, Filename_Final)

def Delete_files():
    remove("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-RowData-%s.zip" % testeo)
    remove("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV_Zip\\Star4All-FinalData-%s.zip" % testeo)
    shutil.rmtree("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Final")
    shutil.rmtree("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")

Create_Files()

work_flow(inicio, final, "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\CSV\\Row")

File_Zip(testeo)

UPload_files()

Delete_files()

