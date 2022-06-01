#!/usr/bin/env python3

# BoBoBo

import sqlite3

db_name = 'biz.db'
gl_conn = None


def init(keep_conn=False):
    global db_name
    global gl_conn
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    cur.execute(
        "create table if not exists t_test(name, created numeric default(datetime('now', 'localtime')))")
    con.commit()
    if keep_conn:
        gl_conn = con
    else:
        con.close()


def write_biz(params, new_conn=True):
    if new_conn:
        global db_name
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.executemany("insert into t_test (name) values (?)", params)
        con.commit()
        con.close()
    else:
        global gl_conn
        con = gl_conn
        cur = con.cursor()
        cur.executemany("insert into t_test (name) values (?)", params)
        con.commit()


def read_biz(param, new_conn=True):
    if new_conn:
        global db_name
        con = sqlite3.connect(db_name)
        cur = con.cursor()
        cur.execute(
            "select * from t_test where name=name", {"name": param})
        resp = cur.fetchall()
        con.close()
        return resp
    else:
        global gl_conn
        con = gl_conn
        cur = con.cursor()
        cur.execute(
            "select * from t_test where name=name", {"name": param})
        resp = cur.fetchall()
        return resp


if __name__ == "__main__":
    init()
    write_biz('k1')
    print(read_biz('k'))
