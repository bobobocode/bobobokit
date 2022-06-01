#ifndef WSGI_H
#define WSGI_H

#include <stdio.h>
#include <Python.h>

typedef struct {
    char *path;
    char *trans_file;
} Environ;

PyObject* convert_environ(Environ r);

#endif
