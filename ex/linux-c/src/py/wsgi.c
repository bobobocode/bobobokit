#include "wsgi.h"


PyObject*
convert_environ(Environ r)
{
    PyObject *out = PyDict_New();
    PyDict_SetItemString(out, "path", Py_BuildValue("s", r.path));
    PyDict_SetItemString(out, "trans_file", Py_BuildValue("s", r.trans_file));
    return out;
}
