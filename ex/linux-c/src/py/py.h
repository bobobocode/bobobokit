// BoBoBo

#ifndef PY_H
#define PY_H

#include <Python.h>

int py_init();
int py_end();

PyObject* get_py_module(const char *module_name);
PyObject* get_py_func(PyObject *py_module, const char *func_name);
void py_exec_func(PyObject *py_module, const char *func_name);
PyObject* py_call_func(PyObject *py_module, const char *func_name, PyObject *arg);

#endif
