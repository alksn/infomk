

from bottle import Bottle, run, template, request, route, post, default_app, static_file

import json
import time, datetime
import sqlite3

#import sys
#sys.path.append('./')
#import page_query


infomk = Bottle()

path_db = './mybase.db'
path_page = './infomk.tpl'
path_info = './info.tpl'
# '/home/alksn/mysite/page.tpl'
path_src = 'dist'
# '/home/alksn/mysite/dist/'


@infomk.route('/dist/:path#.+#')      # regular expression between ## (old syntax)
def static(path):
    return static_file(path, root=path_src)


@infomk.route('/')
def hello():

    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    rows = c.execute('select name, clid_opp from opp').fetchall()
    conn.close()
    return template('{}'.format(path_page), rows=rows, table=[], name='', stat={}, debug=[])


@infomk.route('/', method='post')
def hello():
    #oppname = request.forms.get('oppname')
    #oppname = oppname.encode('iso8859-1').decode('utf8')
    datestart = request.forms.get('datestart')
    dateend = request.forms.get('dateend')
    r_from = request.forms.get('r_from')        # round from
    r_num = request.forms.get('r_num')          # row numbers
    r_f = request.forms.get('r_f')              # row fatality
    v_num = request.forms.get('v_num')
    r_limit = request.forms.get('r_limit')
    min_sfr = request.forms.get('min_sfr')


    if r_f == '':
        return ('Отсутствует количество фаталити. Проверьте правильность заполнения параметров!')

    try:
        if datestart != '':
            foo = datetime.datetime.strptime(datestart, '%Y-%m-%d')
        if dateend != '':
            foo = datetime.datetime.strptime(datestart, '%Y-%m-%d')
        if r_from != '':
            foo = int(r_from)
        if r_num != '':
            foo = int(r_num)
        if v_num != '':
            foo = int(v_num)
        if r_limit != '':
            foo = int(r_limit)
        if min_sfr != '':
            foo = float(min_sfr)

        foo = int(r_f)
    except:
        return ('Ошибка преобразования. Проверьте правильность заполнения параметров!')


    if datestart == '':
        datestart = datetime.datetime.min.strftime('%Y-%m-%d')
        datestart = '2016-07-01'

    if dateend == '':
        dateend = datetime.datetime.now()
        dateend = dateend + datetime.timedelta(days=1)
        dateend = datetime.datetime.strftime(dateend, '%Y-%m-%d')

    if r_from == '':
        r_from = '1'

    if v_num != '':
        if int(v_num) <= 0:
            return ('Число строк по вертикали должно быть не меньше 1')




    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    dateend = dateend - datetime.timedelta(seconds=1)                   # for sql requests
    dateend = datetime.datetime.strftime(dateend, '%Y-%m-%d %H:%M')     # add time into string

    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    datestart = datetime.datetime.strftime(datestart, '%Y-%m-%d %H:%M')


    table = []
    debug = []

    conn = sqlite3.connect(path_db)
    c = conn.cursor()



    qm = ('select g.id, g.dateStart, n1.name || \' - \' || n2.name names, g.clid_opp1, g.clid_opp2, g.result, g.sfr, '
            '('
            'select sum(rg1.isF) from ('
            'select * from vgames where clid_opp1 = g.clid_opp1 and clid_opp2 = g.clid_opp2 ')
                                                    
    for i in range(1, int(r_from)):
        qm += 'and w{0} = g.w{0} '.format(i)

    qm += (''
            'and id != g.id '
            'and dateStart <= g.dateStart '
            'order by dateStart desc ')

    if r_num != '':
        qm += 'limit ' + r_num

    qm += (''
            ') g1, rounds rg1 '
            'where '
            'rg1.game = g1.id ')

    if v_num == '':
        qm += 'and rg1.num <= g.n '
    else:
        qm += 'and rg1.num <= ' + str(int(r_from) + int(v_num) - 1) + ' '       # включая 1 столбец r_from

    qm += (''
            'and rg1.num >= ' + r_from + ' '
            
            ') sumF '
                                         

            'from vgames g, opp n1, opp n2 ' 
            
            'where 1 '
            'and g.clid_opp1 = n1.clid_opp ' 
            'and g.clid_opp2 = n2.clid_opp '
            
            'and g.dateStart >= datetime(\'' + datestart + '\') '
            'and g.dateStart <= datetime(\'' + dateend + '\') ' 
            
            'and sumF >= ' + r_f + ' '
            ' ')

    if min_sfr != '':
        qm += 'and sfr >= ' + min_sfr + ' '

    qm += (''
            'order by g.dateStart desc, names '
            ' ')

    if r_limit != '':
        qm += ' limit ' + r_limit



    table_qm = c.execute(qm).fetchall()

    for row_qm in table_qm:

        game = {}
        game['id'] = str(row_qm[0])
        game['time'] = str(row_qm[1])
        game['time1'] = int(datetime.datetime.strptime(row_qm[1], '%Y-%m-%d %H:%M').timestamp())
        game['name'] = str(row_qm[2])
        game['opp1'] = str(row_qm[3])
        game['opp2'] = str(row_qm[4])
        game['result'] = str(row_qm[5])
        game['sfr'] = str(row_qm[6])
        game['sumF'] = str(row_qm[7])



        game['renter'] = '-'




        qr = ('select min(r.num) from rounds r '
              'where r.game = ' + game['id'] + ' '
              'and r.num >= ' + r_from + ' ')
        if v_num != '':
            qr += 'and r.num <= ' + str(int(r_from) + int(v_num) - 1) + ' '     # включая 1 столбец r_from

        qr += 'and r.isF = 1 '

        table_qr = c.execute(qr).fetchone()

        if table_qr[0] != None:
            game['is_win'] = 1
            game['rname'] = 'выигрыш'
            game['renter'] = table_qr[0]
        else:
            game['is_win'] = 0
            game['rname'] = 'проигрыш'



        table.append(game)

    conn.close()

    stat = {}
    stat['time2'] = int(datetime.datetime.strptime(datestart, '%Y-%m-%d %H:%M').timestamp())
    stat['total'] = 0
    stat['win'] = 0
    stat['avg_sfr'] = 0
    for row in table:
        stat['total'] = stat['total'] + 1
        if row['is_win']:
            stat['win'] = stat['win'] + 1

        stat['avg_sfr'] = stat['avg_sfr'] + float(row['sfr'])

    if len(table) > 0:
        stat['avg_sfr'] = round((stat['avg_sfr'] / len(table)), 3)
    else:
        stat['avg_sfr'] = 0



    stat['datestart'] = request.forms.get('datestart')
    stat['dateend'] = request.forms.get('dateend')
    stat['r_from'] = r_from
    stat['r_num'] = r_num
    stat['r_f'] = r_f
    stat['v_num'] = v_num
    stat['r_limit'] = r_limit
    stat['min_sfr'] = min_sfr


    return template('{}'.format(path_page), rows={}, table=table, name="", stat=stat, debug=debug)
    # '/home/alksn/mysite/page.tpl'



#application = default_app()
#run(host='localhost', port=8080, debug=True)
