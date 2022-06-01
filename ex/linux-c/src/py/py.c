// BoBoBo

#include "py.h"


/*
 * Should set PYTHONPATH first.
 */
int
py_init()
{
    Py_Initialize();
    if (!Py_IsInitialized()) {
        return 1;
    }
    PyRun_SimpleString("print('Python Interpreter Ready')\n");
}

int
py_end()
{
    return Py_FinalizeEx();
}

PyObject*
get_py_module(const char *module_name)
{
    return PyImport_ImportModule(module_name);
}

PyObject*
get_py_func(PyObject *py_module, const char *func_name)
{
    return PyObject_GetAttrString(py_module, func_name);
}

void
py_exec_func(PyObject *py_module, const char *func_name)
{
    PyObject *py_func = get_py_func(py_module, func_name);
    PyObject_CallNoArgs(py_func);
}


PyObject*
py_call_func(PyObject *py_module, const char *func_name, PyObject *arg)
{
    PyObject *py_func = get_py_func(py_module, func_name);

    PyObject *tuple_py = PyTuple_New(1);
    PyTuple_SetItem(tuple_py, 0, arg);

    PyObject_Call(py_func, tuple_py, NULL);
}
