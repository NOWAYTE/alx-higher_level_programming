#include<Python.h>
#include<stdio.h>
#include<listobject.h>
#include<object.h>
/**
 * print_python_list_info - A c function that print some basic
 * information about python lists
 * *p: pointer 
 *
 * Return: does not have a return type
 *
 */

void print_python_list_info(Pyobject *p)
{
	Py_ssize_t s, i, x;


	PyObject t;

	if(!PyList_check(p))
		return;

	s = PyList_Size(p);

	x = ((PyListobject *)p)->x;
	printf("[*] %d\n", s);
	printf("[*] %d\n", x);

	for (i = 0; i < s; i++)
	{
		t = PyList_GetItem(p, i);

		printf("%ld: %s\n", i, Py_TYPES(t)->tp_name);

	}

}
