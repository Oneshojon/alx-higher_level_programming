#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists
 * @p: Pointer to a Python object (should be a list)
 */
void print_python_list_info(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *element;

	size = PyList_Size(p);
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		element = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(element)->tp_name);
	}
}
