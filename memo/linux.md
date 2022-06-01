# Linux Command Memo

## Linux

    uname
    uptime
    who
    df -h
    du -h -d 1 /
    jobs -l
    fg %<number>
    bg %<number>
    date +%s

    firewall-cmd --add-port=20070/tcp --permanent
    firewall-cmd --reload
    firewall-cmd --zone=public --add-port=80/tcp --permanent
    firewall-cmd --query-port=6379/tcp

    ssh-keygen
    ssh -i xxx_rsa user@host
    scp [可选参数] file_source file_target
    printf "%x\n"  3046 
    iconv -s -c -f UTF8 -t GBK src.csv > dec.csv
    tcpdump -X -i lo0 'port 8000'

    setcap cap_net_bind_service=+ep /usr/local/nginx/sbin/nginx

    nohup command > log.out 2>&1 &

## User

    /etc/passwd 第二个字段(加密口令) 可以临时为*或者x, 不可为空
    passwd user

    /etc/shadow 加密方式: 6->sha-512加密, 1->md5加密, 2->Blowfish加密, 5->sha-256加密

    UID 32位无符号整数 建议[500, 32767], 在整个单位保持唯一
    GID 建议500开始分配, 每个用户唯一分组

## Top

    1
    f
    x
    shift + </>
    y

## curl

    curl -d 'jsondata={"uid":"324","valid_flag":1}' "http://127.0.0.1" -X POST -H "header:value" --cookie "k1=1;k2=2"

## SSL

    # 生成私钥
    openssl genrsa -out ${target}.key 1024
    # 生成公钥
    openssl rsa -in ${target}.key -pubout -out ${target}.pem

    # 生成 CA 私钥
    openssl genrsa -out ca.key 1024
    # X.509 Certificate Signing Request (CSR) Management.
    openssl req -new -key ca.key -out ca.csr
    # X.509 Certificate Data Management.
    openssl x509 -req -in ca.csr -signkey ca.key -out ca.crt

    # 服务器端需要向 CA 机构申请签名证书，在申请签名证书之前依然是创建自己的 CSR 文件
    openssl req -new -key ${target}.key -out ${target}.csr
    # 向自己的 CA 机构申请证书，签名过程需要 CA 的证书和私钥参与，最终颁发一个带有 CA 签名的证书
    openssl x509 -req -CA ca.crt -CAkey ca.key -CAcreateserial -in ${target}.csr -out ${target}.crt

## etc

修改/etc/sysctl.conf来更改内核参数。例如，最常用的配置:

    net.core.somaxconn = 100000
    #进程(比如一个worker进程)可以同时打开的最大句柄数，这个参数直接限制最大并发连接数，需根据实际情况配置;
    fs.file-max = 999999

    #设置为1，表示允许将TIME-WAIT状态的socket重新用于新的TCP连接，这对于服务器来说很有意义，因为服务器上总会有大量TIME-WAIT状态的连接;
    net.ipv4.tcp_tw_reuse = 1

    #开启对于TCP时间戳的支持,若该项设置为0，则下面一项设置不起作用
    net.ipv4.tcp_timestamps=1

    #表示开启TCP连接中TIME-WAIT sockets的快速回收
    net.ipv4.tcp_tw_recycle=1

    #当keepalive启用时，TCP发送keepalive消息的频度;默认是2小时，若将其设置得小一些，可以更快地清理无效的连接。
    net.ipv4.tcp_keepalive_time = 600

    #当服务器主动关闭连接时，socket保持在FIN-WAIT-2状态的最大时间;
    net.ipv4.tcp_fin_timeout = 30

    #操作系统允许TIME_WAIT套接字数量的最大值，如果超过这个数字，TIME_WAIT套接字将立刻被清除并打印警告信息;该参数默认为180000，过多的TIME_WAIT套接字会使Web服务器变慢。
    net.ipv4.tcp_max_tw_buckets = 5000

    #在UDP和TCP连接中本地(不包括连接的远端)端口的取值范围;
    net.ipv4.ip_local_port_range = 1024

    #TCP发送缓存(用于TCP发送滑动窗口)的最小值、默认值、最大值;
    net.ipv4.tcp_rmem = 4096 32768 262142
    net.ipv4.tcp_wmem = 4096 32768 262142

    #当网卡接收数据包的速度大于内核处理的速度时，会有一个队列保存这些数据包;这个参数表示该队列的最大值
    net.core.netdev_max_backlog = 8096

    #内核套接字接收缓存区默认的大小
    net.core.rmem_default = 262144

    #内核套接字发送缓存区默认的大小
    net.core.wmem_default = 262144

    #内核套接字接收缓存区的最大大小;
    net.core.rmem_max = 2097152

    #内核套接字发送缓存区的最大大小;注意滑动窗口的大小与套接字缓存区会在一定程度上影响并发连接的数目。每个TCP连接都会为维护TCP滑动窗口而消耗内存，这个窗口会根据服务器的处理速度收缩或扩张。
    #参数wmem_max的设置，需要平衡物理内存的总大小、Nginx并发处理的最大连接数量(由nginx.conf中的worker_processes和worker_connections参数决定)而确定;当然，如果仅仅为了提高并发量使服务器不出现OutOfMemory问题而去降低滑动窗口大小，那么并不合适，因为滑动窗口过小会影响大数据量的传输速度。rmem_default、wmem_default、rmem_max、wmem_max这4个参数的设置需要根据我们的业务特性以及实际的硬件成本来综合考虑。
    net.core.wmem_max = 2097152

    #该参数与性能无关，用于解决TCP的SYN攻击;客户端频繁的连服务器，由于每次连接都在很短的时间内结束，导致很多的TIME_WAIT，以至于用光了可用的端口号，所以新的连接没办法绑定端口，所以要改客户端机器的配置， 在sysctl.conf里加：
    net.ipv4.tcp_syncookies = 0

    #TCP三次握手建立阶段接收SYN请求队列的最大长度，默认为1024，将其设置得大一些可以使出现Nginx繁忙来不及accept新连接的情况时，Linux不至于丢失客户端发起的连接请求;
    net.ipv4.tcp_max_syn_backlog=61000

执行sysctl -p命令，使上述修改生效。

## zsh

```
d .. ...
cd -
z (-l str)
cd /U/b/c

ls -l **/*.sh
kill emacs <tab>
```

## Item2

```
输入打头几个字母，然后输入command+; iterm2将自动列出之前输入过的类似命令。
输入command+shift+h，iterm2将自动列出剪切板的历史记录。
```

## Tmux

```
tmux new -s <session-name>
tmux detach
tmux attach/kill-session/switch -t <session-name>
tmux select-pane (-U/D/L/R)

tmux list-keys
tmux list-commands
tmux info
tmux ls
tmux source-file ~/.tmux.conf
```
