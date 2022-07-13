import CSV_ZENODO
from CSV_ZENODO import Upload_Zenodo
from Date_Creater import current_date_format



Time = current_date_format()

Access_Token = 'p25CSlnib5XnUTzEzgXNphLL4RzUwp23SF4YBhu8jMrq41xO5hboH6roEv1d'
Filename = 'stars4all-%s' % Time
Path = "C:\\Users\\Daniel Moreno\\Desktop\\Osoc-2022\\Star4All\\%s.csv" % Filename
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