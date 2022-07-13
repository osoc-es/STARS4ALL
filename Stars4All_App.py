import CSV_ZENODO
from CSV_ZENODO import Upload_Zenodo
from Date_Creater import current_date_format
import zipfile
import shutil


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

path_row = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV_Zip\\Stars4All-RowData-%s" % testeo
path_final = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV_Zip\\Stars4All-FinalData-%s" % testeo

def File_Zip(Filename):
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV_Zip\\Stars4All-FinalData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV\\Final")
    shutil.make_archive("C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV_Zip\\Stars4All-RowData-%s" % Filename, "zip", "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Testeos\\CSV\\Row")
def UPload_files():
    Upload_Zenodo(Access_Token, meta_data_Row, path_row, Filename_Row)
    Upload_Zenodo(Access_Token, meta_data_Final, path_final, Filename_Final)
File_Zip(testeo)

UPload_files()
