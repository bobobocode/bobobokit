#!/usr/bin/env python3

# BoBoBo

import csv
import pymysql
import sys
from datetime import datetime, date

from boboboscript.common.args import parse_args
from boboboscript.common.ini import get_conf


def trans(args):
    conf = get_conf(args.ini, "mysql")
    conn = pymysql.connect(host=conf('host'), port=conf('port'), db=conf(
        'db'), user=conf('user'), password=conf('password'))

    fields_full = conf('fields').split(',')
    fields = list(map(lambda e: e.split(':')[0], conf('fields').split(',')))

    sql = 'replace into ' + conf('table_name') + \
        ' (' + ','.join(fields) + ') values ('

    hs = []
    for i in range(len(fields)):
        hs.append('%s')

    sql = sql + ','.join(hs) + ')'

    input_file = args.params[0]
    file_reader = csv.reader(open(input_file, 'r'), delimiter=',')
    header = next(file_reader)

    with conn.cursor() as cursor:
        for row in file_reader:
            data = []
            for i in range(len(fields_full)):
                ff = fields_full[i].split(':')
                if len(ff) > 1:
                    if ff[1] == 'date':
                        a_date = datetime.date(datetime.strptime(
                            str(row[i]), '%m/%d/%Y'))
                        a_date = a_date.strftime('%Y-%m-%d')
                        data.append(a_date)
                else:
                    data.append(str(row[i]).lstrip('$')
                                .replace(',', '').strip())

            data = tuple(data)
            print("Execute sql: " + sql)
            print("with data: " + str(data))
            cursor.execute(sql, data)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    args = parse_args(
        sys.argv, "trans_mysql_csv.py -c <config file> -p <output file>")
    trans(args)
