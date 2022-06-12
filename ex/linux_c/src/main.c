#include <sys/wait.h>
#include <sys/epoll.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdio.h>

#include "py/py.h"
#include "py/wsgi.h"

// BoBoBo


int main()
{
    char *c;
    c = "C code is growing.";
    printf("%s\n", c);

    int r = py_init();
    printf("py_init = %i\n", r);

    PyObject *test_funcs_m = get_py_module("t.test_funcs");
    PyObject *test_asyn_m = get_py_module("t.test_eventloop");

    //Execute python function
    py_exec_func(test_funcs_m, "test_print"); 

    //Call python function with dict
    Environ req = {"/t/wsgi_app", "/tmp/trans_file"};
    PyObject *req_pyo = convert_environ(req);
    py_call_func(test_funcs_m, "test_parameter_dict", req_pyo);

    py_exec_func(test_asyn_m, "start_process"); 
    printf("Started python process.\n");

    int epfd = epoll_create(128);
    if (epfd == -1) {
        printf("epoll_create error\n");
        exit(-1);
    }
    struct epoll_event ev;
    ev.data.fd = 0;
    ev.events = EPOLLIN;
    int ret = epoll_ctl(epfd, EPOLL_CTL_ADD, 0, &ev);
    if(-1 == ret){
        printf("Failed to register fd 0.\n");
        exit(-1);
    }else{
        printf("Created epoll.\n");
    }

    char *f1 = "/tmp/growing_c_1";
    ret = mkfifo(f1, 0666);
    if(ret != 0){
        printf("Failed to make fifo f1.\n");
        exit(-1);
    }else{
        printf("Succeed to make fifo f1.\n");
    }


    int fd1 = open(f1, O_RDONLY |O_NONBLOCK);
    if(fd1 < 0){
        printf("Failed to open fd1.\n");
        exit(-1);
    }else{
        printf("Succeed open fd1 readonly");
    }

    ev.data.fd = fd1;
    ev.events = EPOLLIN;
    ret = epoll_ctl(epfd, EPOLL_CTL_ADD, fd1, &ev);
    if(-1 == ret){
        printf("Failed to register fd %i.\n", fd1);
        exit(-1);
    }else{
        printf("Succeed register fd1.");
    }

    char *f2 = "/tmp/growing_c_2";
    ret = mkfifo(f2, 0666);
    if(ret != 0){
        printf("Failed to make fifo f2.\n");
        exit(-1);
    }
    int fd2 = open(f2, O_RDONLY|O_NONBLOCK);
    if(fd2 < 0){
        printf("Failed to open fd2.\n");
        exit(-1);
    }
    ev.data.fd = fd2;
    ev.events = EPOLLIN;
    ret = epoll_ctl(epfd, EPOLL_CTL_ADD, fd2, &ev);
    if(-1 == ret){
        printf("Failed to register fd %i.\n", fd2);
        exit(-1);
    }

    struct epoll_event wait_event;

    Environ req1 = {"/t/biz1", f1};
    PyObject *req_pyo1 = convert_environ(req1);
    Environ req2 = {"/t/biz2", f2};
    PyObject *req_pyo2 = convert_environ(req2);

    py_call_func(test_asyn_m, "do_request", req_pyo1); 
    py_call_func(test_asyn_m, "do_request", req_pyo2); 

    printf("Start epoll wait.\n");
    int count=0;
    while(1){
        ret = epoll_wait(epfd, &wait_event, 128, 5000);
        if (ret == -1) {
            close(epfd);
            perror("epoll_wait error");
        } else if (ret > 0) {
            if((wait_event.data.fd != 0) && (wait_event.events & EPOLLIN == EPOLLIN)){
                char buf[100] = {0};
                read(wait_event.data.fd, buf, sizeof(buf));
                printf("fifo buf = %s\n", buf);
            }
        } else if (ret == 0) {
            printf("time out\n");
        }
        if(0 == count){
            py_call_func(test_asyn_m, "do_request", req_pyo1); 
            py_call_func(test_asyn_m, "do_request", req_pyo2); 
            count++;
        }
    }

    return 0;
}
