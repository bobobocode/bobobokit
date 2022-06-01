# Storage

## sqlite3

    sqlite3 [db file] < [sql script]
    strftime('%s','now')

    select datetime(PARAM1, 'unixepoch', 'localtime') as PARAM from ALGORITHM_CONFIG;

## MySQL

    create user 'testuser'@'127.0.0.1' identified by '123456';
    grant all privileges on db_test.* to 'testuser'@'127.0.0.1';
    flush privileges;

    source  file.sql

    mysqldump -h192.168.32.88 -uliangcheng -p0324LiangCheng2017 -d --all-databases > bainianaolai.sql

    show processlist;
    show variables like 'character_%';
    set @@character_set_connection=utf8;

    pager cat > file

    sudo /usr/local/mysql/support-files/mysql.server start
