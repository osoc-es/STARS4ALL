import CSV_ZENODO
from CSV_ZENODO import Upload_Zenodo


Access_Token = 'p25CSlnib5XnUTzEzgXNphLL4RzUwp23SF4YBhu8jMrq41xO5hboH6roEv1d'
Path = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\stars4all-july-2020.csv"
Filename = 'stars4all-july-2020'
Title = 'Stars4ll_Tester'
Description = 'Tester for Stars4All'
name = 'Daniel Moreno'
Affiliation = 'OSOC'
Type = 'poster'
meta_data = {
     'metadata': {
            'title': Title,
         'upload_type': Type,
        'description': Description,
        'creators': [{'name': name,
                    'affiliation': Affiliation}] } }

def UPload_files():
    Upload_Zenodo(Access_Token, meta_data, Path, Filename)
UPload_files()