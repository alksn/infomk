

import json
import time, datetime
import sqlite3

#filename = './stat/stat15000-0.json'
filename_opp = './stat/opp.json'
filename_txt = './stat/stat.txt'

conn = sqlite3.connect('./mybase.db')
c = conn.cursor()


# insert opponents
rows = c.execute('select * from opp').fetchone()
if rows is None:

    with open(r'./{}'.format(filename_opp), 'r') as file:
        text = file.read()
        info = json.loads(text)
        rows = info['items']['1252965']['opp']

    for i in range(0, len(rows)):
        clid_opp = rows[i]['clid_opp']
        name = rows[i]['opp'].encode('cp1251')
        print('i={}|id={}|name={}'.format(i, clid_opp, name.decode('utf8')))
        c.execute("insert into opp values (?,?)", (clid_opp, name))



# insert into games

#with open(r'./{}'.format(filename), 'r') as file:
#    text = file.read()
#    info = json.loads(text)

with open('./{}'.format(filename_txt), 'r') as file:
    text = file.read()

lines = text.splitlines()
for indx, line in enumerate(lines):
    info = json.loads(line)     # load is for a file, loads for a string


    for i in range(0, len(info['rows'])):

        print('str={0}|line={1}'.format(indx, i))

        champId = info['rows'][i]['champId']['v'] # only Mortal Kombat X champ, exclude Mortal Kombat 11 (BO3)
        if champId != 1252965:
            continue

        dateStart = info['rows'][i]['dateStart']['v']
        #dateStart = time.strptime(dateStart, '%y-%m-%d %H:%M')  # '19-05-17 22:55'
        clid_opp1 = info['rows'][i]['clid_opp1']['v']
        clid_opp2 = info['rows'][i]['clid_opp2']['v']
        result = info['rows'][i]['result']['v']
        sfr = info['rows'][i]['sfr']['v']
        sp1 = info['rows'][i]['sp1']['v']
        sp2 = info['rows'][i]['sp2']['v']

        if result == ' ':       # 18-07-27 17:40  "r1":{"v":0,"dobiv":"Рї","winner":0,"wt":0}
            continue

        #c.execute("insert into games values (?,?,?,?)", (datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S'),None,0,0))
        c.execute("insert into games values (?,?,?,?,?,?,?,?)", (None, '20' + dateStart, clid_opp1, clid_opp2, result, sfr, sp1, sp2))
        game_id = c.lastrowid

        # добавляем раунды игры
        for j in range(0, 9):

            dobiv = info['rows'][i]['r{}'.format(j+1)]['dobiv'].encode('cp1251').decode('utf8')     # encode-decode cyrillic olny
            winner = info['rows'][i]['r{}'.format(j+1)]['winner']

            if dobiv == 'N':
                continue

            if winner == 1:
                winner = clid_opp1
            else:
                winner = clid_opp2

            if dobiv == 'F':
                isF = 1
            else:
                isF = 0

            c.execute("insert into rounds values (:id, :winner, :dobiv, :game, :isF, :num)",
                      (None, winner, dobiv, game_id, isF, j+1))

        #print("end")
        #break
    #break

conn.commit()
conn.close()








