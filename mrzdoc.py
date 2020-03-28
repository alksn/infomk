
from bottle import Bottle, run, template, request, route, post, default_app, static_file

import json
import time, datetime
import sqlite3

from mrz.generator.mrvb import MRVBCodeGenerator
from mrz.generator.td1 import TD1CodeGenerator
from mrz.generator.td2 import TD2CodeGenerator
from mrz.generator.td3 import TD3CodeGenerator


mrzdoc = Bottle()

path_page = './mrzdoc.tpl'

# '/home/alksn/mysite/page.tpl'
path_src = 'dist'
# '/home/alksn/mysite/dist/'


@mrzdoc.route('/dist/:path#.+#')      # regular expression between ## (old syntax)
def static(path):
    return static_file(path, root=path_src)


@mrzdoc.route('/')
def hello():


    return template(path_page, stat={})


@mrzdoc.route('/', method='post')
def hello():
    #oppname = request.forms.get('oppname')
    #oppname = oppname.encode('iso8859-1').decode('utf8')

    stat = {}

    document_type = request.forms.get('document_type')
    country_code = request.forms.get('country_code')
    surname = request.forms.get('surname')
    given_names = request.forms.get('given_names')
    document_number = request.forms.get('document_number')
    nationality = request.forms.get('nationality')
    birth_date = request.forms.get('birth_date')
    sex = request.forms.get('sex')
    expiry_date = request.forms.get('expiry_date')
    optional_data1 = request.forms.get('optional_data1')

    if optional_data1 is None:
        optional_data1 = ''

    stat['document_type'] = document_type
    stat['country_code'] = country_code
    stat['surname'] = surname
    stat['given_names'] = given_names
    stat['document_number'] = document_number
    stat['nationality'] = nationality
    stat['birth_date'] = birth_date
    stat['sex'] = sex
    stat['expiry_date'] = expiry_date
    stat['optional_data1'] = optional_data1

    for key in stat:
        if key == 'optional_data1':
            continue

        if stat[key] == '':
            return 'Заполните поля формы'

    try:    
        str1=TD3CodeGenerator(
        document_type,
        country_code,
        surname,
        given_names,
        document_number,
        nationality,
        birth_date,
        sex,
        expiry_date,
        optional_data1)
    except Exception as e:
        str1=''
        stat['error']=str(e)
  

    str2 = TD3CodeGenerator("P",                   # Document type   Normally 'P' for passport
    "QATAR",               # Country         3 letters code or country name
    "AL-KAABI",            # Surname(s)
    "ALI HAMAD ABDULLAH",  # Given Names     Special characters will be transliterated
    "00000000",            # Passport number Special characters will be transliterated
    "QAT",                 # Nationality     3 letter code or country name
    "710307",              # Birth date      YYMMDD
    "M",                   # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "110725",              # Expiry date     YYMMDD
    "12345458902")         # Id number       Non-mandatory field in some countries


    str3=TD3CodeGenerator("P",           # Document type
    "Utopia",      # Country
    "Eriksson",    # Surname(s)
    "Anna María",  # Given name(s)
    "L898902C3",   # Passport number
    "UTO",         # Nationality
    "740812",      # Birth date
    "F",           # Genre
    "120415",      # Expiry date
    "ZE184226B")   # Id number


    str4=TD3CodeGenerator("P",          # Document type   Normally 'P' for passport
    "JPN",        # Country         3 letters code or country name
    "GAIMU",      # Surname(s)      Special characters will be transliterated
    "SAKURA",     # Given name(s)   Special characters will be transliterated
    "XS1234567",  # Passport number
    "Japan",      # Nationality     3 letter code or country name
    "790220",     # Birth date      YYMMDD
    "F",          # Genre           Male: 'M', Female: 'F' or Undefined 'X'
    "160320")     # Expiry date     YYMMDD


    stat['result']=str1


    #return template('<pre>{{str1}}</pre>', str1=str2)
    #return "Hello World!"
    return template(path_page, stat=stat)


#mrzdoc.run(host='localhost', port=8080, debug=True)







