

from bottle import Bottle, run, template, request, route, post, default_app, static_file

import json
import time, datetime
import sqlite3

#import sys
#sys.path.append('./')
#import page_query


infomk2 = Bottle()

path_db = './mybase.db'
path_page = './infomk2.tpl'
path_info = './info.tpl'
path_qm = './text_qm.txt'
# '/home/alksn/mysite/page.tpl'
path_src = 'dist'
# '/home/alksn/mysite/dist/'



@infomk2.route('/dist/:path#.+#')      # regular expression between ## (old syntax)
def static(path):
    return static_file(path, root=path_src)


@infomk2.route('/')
def hello():

    conn = sqlite3.connect(path_db)
    c = conn.cursor()
    rows = c.execute('select name, clid_opp from opp').fetchall()
    conn.close()
    return template('{}'.format(path_page), rows=rows, table=[], name='', stat={}, debug=[])


@infomk2.route('/', method='post')
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
    p_col = request.forms.get('p_col')
    p_grid = request.forms.get('p_grid')


    #if r_f == '':
    #    return ('Отсутствует количество фаталити. Проверьте правильность заполнения параметров!')

    try:
        if datestart != '':
            foo = datetime.datetime.strptime(datestart, '%Y-%m-%d')
        if dateend != '':
            foo = datetime.datetime.strptime(dateend, '%Y-%m-%d')
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
        if p_col != '':
            foo = float(p_col)
        if p_grid != '':
            foo = float(p_grid)
        if r_f != '':
            foo = float(r_f)
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


    if p_col == '':
        p_col = '50'

    if p_col != '':
        if float(p_col) < 50:
            return ('Процент побед по счету не может быть меньше 50')


    dateend = datetime.datetime.strptime(dateend, '%Y-%m-%d')
    dateend = dateend - datetime.timedelta(seconds=1)                   # for sql requests
    dateend = datetime.datetime.strftime(dateend, '%Y-%m-%d %H:%M')     # add time into string

    datestart = datetime.datetime.strptime(datestart, '%Y-%m-%d')
    datestart = datetime.datetime.strftime(datestart, '%Y-%m-%d %H:%M')


    table = []
    debug = []

    conn = sqlite3.connect(path_db)
    c = conn.cursor()




    # select * vgames where
    wg = (''
           ' clid_opp1 = g.clid_opp1 and clid_opp2 = g.clid_opp2 '
           ' ')

    for i in range(1, int(r_from)):
        wg += 'and w{0} = g.w{0} '.format(i)

    wg += (''
            'and id != g.id '
            'and dateStart <= g.dateStart '
            'order by dateStart desc ')

    if r_num != '':
        wg += 'limit ' + r_num


    # rounds rg1 where
    wr = (''
           'rg1.game = g1.id '
           ' ')

    if v_num == '':
        wr += 'and rg1.num <= g.n '
    else:
        wr += 'and rg1.num <= ' + str(int(r_from) + int(v_num) - 1) + ' '       # включая 1 столбец r_from

    wr += (''
            'and rg1.num >= ' + r_from + ' ')





    qm = (''
           'select g.id, g.dateStart, n1.name || \' - \' || n2.name names, g.clid_opp1, g.clid_opp2, g.result, g.sfr '
           '')

    '''
    qm += (''
            ','
            '('
            'select sum(rg1.isF) from ('
            'select * from vgames where ' + wg)
    qm += (''
            ') g1, rounds rg1 '
            'where ' + wr)
    qm += (''      
            ') sumF ')
    '''
    qm += ', null sumF'

    qm += (''
            ','
            '('
            'SELECT case '
            'when stw > 0 then (select sum(c1)*100.0/(sum(c1)+sum(c2)) from (select '
            '(select count(rg1.id) from rounds rg1 where ' + wr + ' and rg1.winner = g.clid_opp1) c1, '
            '(select count(rg1.id) from rounds rg1 where ' + wr + ' and rg1.winner = g.clid_opp2) c2 '
            'from ('
            'select id from vgames where ' + wg + ' '
            ') g1 )) '
            ''
            'when stw < 0 then (select sum(c2)*100.0/(sum(c1)+sum(c2)) from (select '
            '(select count(rg1.id) from rounds rg1 where ' + wr + ' and rg1.winner = g.clid_opp1) c1, '
            '(select count(rg1.id) from rounds rg1 where ' + wr + ' and rg1.winner = g.clid_opp2) c2 '
            'from ('
            'select id from vgames where ' + wg + ' '
            ') g1 )) '
            ''
            'else null end '
            'FROM (select sum(tw) stw from ('
            'select tw from vtwgames where ' + wg + ' '
            '))) percentgrid '
            ','
            '('
            'select case '
            'when stw > 0 then percent1 '
            'when stw < 0 then percent2 '
            'else 50 end '
            'from '
            '(select (sum(s1) - sum(s2)) stw, sum(s1)*100.0/sum(ctw) percent1, sum(s2)*100.0/sum(ctw) percent2 from '
            '(select count(tw) ctw, case when tw > 0 then count(tw) else 0 end s1, case when tw < 0 then count(tw) else 0 end s2 from ('
            'select tw from vtwgames where ' + wg + ' '
            ') group by tw))) percentcol '
            ''
            ','
            '('
            'select case '
            'when stw > 0 then g.clid_opp1 '
            'when stw < 0 then g.clid_opp2 '
            'else -1 end '
            'from '
            '(select (sum(s1) - sum(s2)) stw, sum(s1)*100.0/sum(ctw) percent1, sum(s2)*100.0/sum(ctw) percent2 from '
            '(select count(tw) ctw, case when tw > 0 then count(tw) else 0 end s1, case when tw < 0 then count(tw) else 0 end s2 from ('
            'select tw from vtwgames where ' + wg + ' '
            ') group by tw))) percentcol_winner '
            ''
            ','
            '('
            'select case '
            'when stw > 0 then g.sp1 '
            'when stw < 0 then g.sp2 '
            'else -1 end '
            'from '
            '(select (sum(s1) - sum(s2)) stw, sum(s1)*100.0/sum(ctw) percent1, sum(s2)*100.0/sum(ctw) percent2 from '
            '(select count(tw) ctw, case when tw > 0 then count(tw) else 0 end s1, case when tw < 0 then count(tw) else 0 end s2 from ('
            'select tw from vtwgames where ' + wg + ' '
            ') group by tw))) percentcol_sfr '
            ''
            ''
            ''
            ''
            ''
            ''
            '')


    qm += (''
            'from vgames g, opp n1, opp n2 '             
            'where 1 '
            'and g.clid_opp1 = n1.clid_opp ' 
            'and g.clid_opp2 = n2.clid_opp '            
            'and g.dateStart >= datetime(\'' + datestart + '\') '
            'and g.dateStart <= datetime(\'' + dateend + '\') '
            '/*and percentgrid is not null /*исключаем игры с id 1 и 2*/ '
            'and g.result != \'0:0\' /*исключаем незавершненные игры в т.ч. id 1 и 2*/ '
            ' ')

    if r_f != '':
        qm += 'and sumF >= ' + r_f + ' '

    if p_col != '':
        qm += 'and percentcol > ' + p_col + ' '

    if p_grid != '':
        qm += 'and percentgrid >= ' + p_grid + ' '

    if min_sfr != '':
        #qm += 'and sfr >= ' + min_sfr + ' '
        qm += 'and percentcol_sfr >= ' + min_sfr + ' '

    qm += (''
            'order by g.dateStart desc, names '
            ' ')

    if r_limit != '':
        qm += ' limit ' + r_limit


    #'''
    with open(path_qm, 'w') as file:
        file.write(qm)
    #'''

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
        game['percentgrid'] = str(row_qm[8])
        game['percentcol'] = str(row_qm[9])
        game['percentcol_winner'] = str(row_qm[10])
        game['percentcol_sfr'] = str(row_qm[11])


        # fatality entry
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


        # percent colomn entry
        game['renter_pcol'] = '-'

        qr = ('select min(r.num) from rounds r '
              'where r.game = ' + game['id'] + ' '
              'and r.num >= ' + r_from + ' ')
        if v_num != '':
            qr += 'and r.num <= ' + str(int(r_from) + int(v_num) - 1) + ' '     # включая 1 столбец r_from

        qr += 'and r.winner = ' + game['percentcol_winner']

        table_qr = c.execute(qr).fetchone()

        if table_qr[0] != None:
            game['is_win_pcol'] = 1
            game['rname_pcol'] = 'выигрыш'
            game['renter_pcol'] = table_qr[0]
        else:
            game['is_win_pcol'] = 0
            game['rname_pcol'] = 'проигрыш'



        table.append(game)

    conn.close()

    stat = {}
    stat['time2'] = int(datetime.datetime.strptime(datestart, '%Y-%m-%d %H:%M').timestamp())
    stat['total'] = 0
    stat['win'] = 0
    stat['avg_sfr'] = 0                 # средний коэффициент sfr
    stat['avg_psfr'] = 0                # средний коэффициент, зависит от процента побед по счёту

    stat['win_pcol'] = 0
    stat['avg_pcol'] = 0                # средний процент по счету
    stat['avg_pgrid'] = 0               # средний процент по сетке

    for row in table:
        stat['total'] = stat['total'] + 1
        if row['is_win']:
            stat['win'] = stat['win'] + 1
        if row['is_win_pcol']:
            stat['win_pcol'] = stat['win_pcol'] + 1

        stat['avg_sfr'] = stat['avg_sfr'] + float(row['sfr'])
        stat['avg_psfr'] = stat['avg_psfr'] + float(row['percentcol_sfr'])
        stat['avg_pcol'] = stat['avg_pcol'] + float(row['percentcol'])
        stat['avg_pgrid'] = stat['avg_pgrid'] + float(row['percentgrid'])

    if len(table) > 0:
        #stat['avg_sfr'] = round((stat['avg_sfr'] / len(table)), 3)
        stat['avg_sfr'] = round((stat['avg_psfr'] / len(table)), 3) # for infomk2 only, for univesal solution change this and add changes into .tpl
        stat['avg_pcol'] = round((stat['avg_pcol'] / len(table)), 2)
        stat['avg_pgrid'] = round((stat['avg_pgrid'] / len(table)), 2)


    #else:
        #stat['avg_sfr'] = 0



    stat['datestart'] = request.forms.get('datestart')
    stat['dateend'] = request.forms.get('dateend')
    stat['r_from'] = r_from
    stat['r_num'] = r_num
    stat['r_f'] = r_f
    stat['v_num'] = v_num
    stat['r_limit'] = r_limit
    stat['min_sfr'] = min_sfr
    stat['p_col'] = p_col
    stat['p_grid'] = p_grid


    return template('{}'.format(path_page), rows={}, table=table, name="", stat=stat, debug=debug)
    # '/home/alksn/mysite/page.tpl'



#application = default_app()
#infomk2.run(host='localhost', port=8080, debug=True)
