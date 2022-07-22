# STARS4ALL DOCUMENTATION

REQUIRMENTS 

Python 3.8.10

pip 20.0.2

ubuntu linux 20.04

windows 10 pro

GETTING STARTED 

We have to install 2 librerys to begin , Influxdb and ephem:

```pip install Influxdb```

```pip install ephem```

The next step is clone our repository of github as we need access to its programs.

```git clone https://github.com/osoc-es/STARS4ALL.git ```

The before command create a directory which name is STARS4ALL , so we have to be inside of them to launch the programs. 

```-cd STARS4ALL```

There are a file which conteins the whole information about the passwords and secret data , this file whose name is variable.conf..
It has five  variables :

-hostdb= xx.xxx.xxx.xxx (ip number)  
-portdb= int (port number)
-usernamedb=" " (empty) 
-passworddb=" " (empty)
-database=str  (database name)
 

For example :
```
hostdb= 192.111.122.111
portdb=100
usernamedb=""
passworddb=""
database=ontology
```

We recommend to use virtual environments Python3.8 to run our programs.

Automaticly the file Stars4All_App.py create the datasets of a the month that begin one month ago and end in the actual date .
To run the engine via command line you just need to execute the following:

```-python3 Stars4All_App.py ```

If you want to crate a datasets of other dates 

```-python3 Stars4All_App.py 'date1' 'date2' ```

The arguments 'date1' and 'date2' are the standar dates that we pass to crate the datasets.

The 'date1' indicates when we begin to recolect data and the 'date2' indicates when we finsh to recolect data.

The format standar date is : 'year-month-dayT-hour-minute-seconds' ( e.g 2020-04-10T08:50:53)
A full example of a this process is :

```-python3 Stars4All_App.py  '2020-04-10T08:50:53'      '2020-05-10T08:50:532'```
