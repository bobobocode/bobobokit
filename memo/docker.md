# Docker

#### configuration

#### command

    docker export <CONTAINER ID> > my_container.tar
    cat my_container.tar |docker import - image_name:tag

    docker run -v <host dir>:<container dir> -p <container port>:<host port> -it centos:centos6 /bin/bash
    docker run --name gdb --security-opt seccomp=unconfined -v /Users/James/code:/data -it centos:centos6 /bin/bash
    docker run --privileged -ti --name test  docker.io/centos:7  /usr/sbin/init
    docker run --rm -it redis_master:1.0 bash

    docker@xhyve:~$ sudo mkdir /sys/fs/cgroup/systemd
    docker@xhyve:~$ sudo mount -t cgroup -o none,name=systemd cgroup /sys/fs/cgroup/systemd

    docker save -o dockerimg_base_server.tar base_server
    docker load -i quay.io-calico-node-1.tar

    docker images -f "dangling=true"
    docker build -f Redis.Dockerfile -t cluster_redis:1.0 .

    docker volume ls -qf dangling=true | xargs docker volume rm

    docker-machine scp host1:/tmp/a host2:/tmp/b
    docker cp 容器名：要拷贝的文件在容器里面的路径  要拷贝到宿主机的相应路径

    docker-compose -f docker-compose-base.yml -f docker-compose-dev.yml config


#### docker-compose

env_file:
   - env

env文件中引用环境变量必须加{}

容器中会附带宿主机环境变量PATH
