#!/bin/sh

dir_rtfsc=~/code/rtfsc

gitclone(){
    if [ -d $2 ]; then
        echo $2 exists.
    else
        git clone $1 $2
    fi
}


## System
gitclone https://github.com/loveveryday/linux0.11.git $dir_rtfsc/sys/linux0.11
gitclone https://github.com/redis/redis.git $dir_rtfsc/sys/redis

## Tool
gitclone https://github.com/vim/vim.git $dir_rtfsc/tool/vim
gitclone https://github.com/honza/vim-snippets.git $dir_rtfsc/tool/vim-snippets

## Nginx
gitclone https://github.com/nginx/nginx.git $dir_rtfsc/ngx/nginx
gitclone https://github.com/arut/nginx-python-module.git $dir_rtfsc/ngx/nginx-python-module
gitclone https://github.com/rryqszq4/ngx_python.git $dir_rtfsc/ngx/ngx_python
gitclone https://github.com/openresty/test-nginx.git $dir_rtfsc/ngx/test-nginx
gitclone https://github.com/openresty/openresty.git $dir_rtfsc/ngx/openresty
gitclone https://github.com/orlabs/orange.git $dir_rtfsc/ngx/orange
gitclone https://github.com/openresty/lua-nginx-module.git $dir_rtfsc/ngx/lua-nginx-module
gitclone https://github.com/webcpp/hi-nginx.git $dir_rtfsc/ngx/hi-nginx
gitclone https://github.com/GrahamDumpleton/mod_wsgi.git $dir_rtfsc/ngx/mod_wsgi

## Python
gitclone https://github.com/python/cpython.git $dir_rtfsc/python/cpython
gitclone https://github.com/andymccurdy/redis-py.git $dir_rtfsc/python/redis-py
gitclone https://github.com/kachayev/fn.py.git $dir_rtfsc/python/fn
gitclone https://github.com/tornadoweb/tornado.git $dir_rtfsc/python/tornado
gitclone https://github.com/pallets/flask.git $dir_rtfsc/python/flask
gitclone https://github.com/django/django.git $dir_rtfsc/python/django
gitclone https://github.com/cyberdelia/flask-mysql.git $dir_rtfsc/python/flask-mysql
gitclone https://github.com/bottlepy/bottle.git $dir_rtfsc/python/bottle
gitclone https://github.com/mahmoud/clastic.git $dir_rtfsc/python/clastic
gitclone https://github.com/WebwareForPython/DBUtils.git $dir_rtfsc/python/DBUtils
gitclone https://github.com/PyMySQL/PyMySQL.git $dir_rtfsc/python/PyMySQL
gitclone https://github.com/kennethreitz/requests.git $dir_rtfsc/python/requests
gitclone https://github.com/scrapy/scrapy.git $dir_rtfsc/python/scrapy
gitclone https://github.com/ageitgey/face_recognition.git $dir_rtfsc/python/face_recognition
gitclone https://github.com/johnbywater/eventsourcing.git $dir_rtfsc/python/eventsourcing
gitclone https://github.com/patrickporto/kant $dir_rtfsc/python/kant
gitclone https://github.com/sqlalchemy/sqlalchemy.git $dir_rtfsc/python/sqlalchemy
gitclone https://github.com/squeaky-pl/japronto.git $dir_rtfsc/python/japronto
gitclone https://github.com/omnilib/aiosqlite.git $dir_rtfsc/python/aiosqlite
gitclone https://github.com/locustio/locust.git $dir_rtfsc/python/locust
gitclone https://github.com/Zaeb0s/epoll-socket-server.git $dir_rtfsc/python/epoll-socket-server
gitclone https://github.com/pallets/werkzeug.git $dir_rtfsc/python/werkzeug

## JavaScript
gitclone https://github.com/madrobby/zepto.git $dir_rtfsc/javascript/zepto
gitclone https://github.com/mui-org/material-ui.git $dir_rtfsc/javascript/material-ui

## Blockchain
gitclone https://github.com/ethereum/go-ethereum.git $dir_rtfsc/blockchain/go-ethereum
gitclone https://github.com/ethereum/py-evm.git $dir_rtfsc/blockchain/py-evm

## Spring
gitclone https://github.com/spring-projects/spring-boot.git $dir_rtfsc/spring/spring-boot
gitclone https://github.com/spring-projects/spring-framework.git $dir_rtfsc/spring/spring-framework
gitclone https://github.com/spring-projects/spring-data-redis.git $dir_rtfsc/spring/spring-data-redis
gitclone https://github.com/spring-projects/spring-batch.git $dir_rtfsc/spring/spring-batch
gitclone https://github.com/spring-projects/spring-data-jpa.git $dir_rtfsc/spring/spring-data-jpa
gitclone https://github.com/spring-projects/spring-integration.git $dir_rtfsc/spring/spring-integration

## Java
gitclone https://github.com/google/guava.git $dir_rtfsc/java/guava
gitclone https://github.com/openjdk/jdk.git $dir_rtfsc/java/openjdk
gitclone https://github.com/reactor/reactor-core.git $dir_rtfsc/java/reactor-core
gitclone https://github.com/netty/netty.git $dir_rtfsc/java/netty
gitclone https://github.com/apache/commons-pool.git $dir_rtfsc/java/commons-pool
gitclone https://github.com/apache/commons-lang.git $dir_rtfsc/java/commons-lang
gitclone https://github.com/apache/commons-io.git $dir_rtfsc/java/commons-io
gitclone https://github.com/apache/commons-net.git $dir_rtfsc/java/commons-net
gitclone https://github.com/Netflix/zuul.git $dir_rtfsc/java/zuul
gitclone https://github.com/quartz-scheduler/quartz.git $dir_rtfsc/java/quartz
gitclone https://github.com/xetorthio/jedis.git $dir_rtfsc/java/jedis

## Example
gitclone https://github.com/veltzer/demos-linux.git $dir_rtfsc/example/demos-linux
gitclone https://github.com/chronolaw/ngx_cpp_dev.git $dir_rtfsc/example/ngx_cpp_dev

gitclone https://github.com/1hbb/react-native-instagram-clone.git $dir_rtfsc/example/react-native/react-native-instagram-clone
gitclone https://github.com/yrjwcharm/react-native-wxpay.git $dir_rtfsc/example/react-native-wxpay
gitclone https://github.com/forrest23/ReactNativeComponents.git $dir_rtfsc/example/ReactNativeComponents

gitclone https://github.com/zhang1217/sticky-notes.git $dir_rtfsc/example/sticky-notes
gitclone https://github.com/SimHub/simhub-electron-calendar.git $dir_rtfsc/example/simhub-electron-calendar
gitclone https://github.com/zimudec/vue-tuicalendar-bootstrap-example.git $dir_rtfsc/example/vue-tuicalendar-bootstrap-example

gitclone https://github.com/iamcco/markdown-preview.vim.git $dir_rtfsc/example/markdown-preview

## Book
gitclone https://github.com/PacktPublishing/Functional-Python-Programming-Second-Edition.git $dir_rtfsc/book/Functional-Python-Programming-Second-Edition
gitclone https://github.com/dabeaz/python-cookbook.git $dir_rtfsc/book/python-cookbook
gitclone https://github.com/jerry-git/learn-python3.git $dir_rtfsc/book/learn-python3

## x-plan
gitclone https://github.com/QuantumLiu/AIMakeup.git $dir_rtfsc/xplan/AIMakeup
