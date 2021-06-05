# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 17:42:05 2021

@author: DGE
"""
import pandas as pd
import numpy as np

def connDB():
    import mysql.connector as mysql
    db = mysql.connect(
        host='localhost',
        user = 'root',
        password = '',
        port = 8888,
        db = 'test'
    )
    return db

def table(name, cursor):
    cursor.execute('select * from ' + str(name))
    datas = cursor.fetchall()
    for row in datas:
        print (row)

def creat(data,name):
    import sqlalchemy
    connection = sqlalchemy.create_engine("mysql+pymysql://root:@localhost:8888/test",encoding="utf-8", echo=False)
    data.to_sql(name=name, con=connection,if_exists='replace')  # append, fail
    return connection

def to_radar(df):
    df['mode'] = df['隨機模式']
    df['number'] = df['編號'].astype(str) 
    df['target'] = df['燈號位置'].astype(str) 
    df['reaction'] = df['反應時間']
    df['start_to_light'] = df['起點到燈號位置時間']
    df['light_to_start'] = df['燈號回起點位置實測時間']
    df.drop(columns=['紀錄時間','隨機模式','編號','燈號位置','反應時間','起點到燈號位置時間','燈號回起點位置實測時間'], axis=1, inplace=True)
    del df['mode']

def add_radar(target, color, ax, angles, df_r):
    condition = df_r['target'] == target
    df_ar = df_r.loc[condition]      #number = numberr and target = input
    #print(df_ar)
    df_ar = df_ar.groupby(['target']).mean()
    #print(df_ar)
    values = df_ar.loc[target].values.tolist()
    #print(values[1])
    values += values[:1]
    #print(values)
    # Draw the outline of our data.
    ax.plot(angles, values, color=color, linewidth=1, label=target)
    ax.fill(angles, values, color=color, alpha=0.25)

def radar(table, df_r, numberr ):   #table = title name
    import matplotlib.pyplot as plt 
    condition = df_r['number'] == numberr   #number = numberr
    df_r = df_r.loc[condition]
    df_gr = df_r.groupby(['number','target']).mean() 
    print(df_gr)
    count = df_gr.groupby(['number']).size()
    #print(count[0])
    if count[0] != 6:
        print('ERROR!')
        print('\r\n')
        return
    else:
        print('\r\n')
        label = ['reaction','start_to_light','light_to_start']  #draw data col
        num = len(label)
        angles = np.linspace(0, 2 * np.pi, num, endpoint=False).tolist()
        angles += angles[:1]
        label += label[:1]
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
        add_radar('1', '#FF2D2D', ax, angles, df_r)
        add_radar('2', '#FF8040', ax, angles, df_r)
        add_radar('3', '#FFD306', ax, angles, df_r)
        add_radar('4', '#00DB00', ax, angles, df_r)
        add_radar('5', '#66B3FF', ax, angles, df_r)
        add_radar('6', '#B15BFF', ax, angles, df_r)
        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        #print(np.degrees(angles))
        ax.set_thetagrids(np.degrees(angles), label)
        for label, angle in zip(ax.get_xticklabels(), angles):
            if angle in (0, np.pi):
                label.set_horizontalalignment('center')
            elif 0 < angle < np.pi:
                label.set_horizontalalignment('left')
            else:
                label.set_horizontalalignment('right')
        ax.set_ylim(0, 2)
        ax.set_rlabel_position(180 / num)
        ax.tick_params(colors='#000000')
        ax.tick_params(axis='y', labelsize=5)
        ax.grid(color='#FAFAFA')
        ax.spines['polar'].set_color('#333333')
        ax.set_facecolor('#FAFAFA')
        ax.set_title(str(table), y=1.08)
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
        plt.savefig(fname=str(table)+'.png', bbox_inches='tight', dpi=150)

def main():
    df = pd.read_csv("game1.csv")
    #df = pd.read_excel("game1.xlsx")
    df.dropna(axis=1, inplace=True)
    print(df)
    conn = creat(df,'badminton')   #create table
    #db = connDB()
    #cursor = db.cursor()
    #table('badminton', cursor)     #print table
    print('\r\n')
    df_sql = pd.read_sql('SELECT * FROM badminton', con=conn)   #select table to pandas
    del df_sql['index']
    to_radar(df_sql)  #dataframe translate to english
    radar('Player0', df_sql, '0')  #draw radar from dataframe (condition)
    radar('Player11', df_sql, '11')
    radar('Player16', df_sql, '16')
    radar('Player17', df_sql, '17')
    radar('Player20', df_sql, '20')
    radar('Player25', df_sql, '25')
    radar('Player29', df_sql, '29')
    #db.close()

if __name__ == "__main__":
    main()
