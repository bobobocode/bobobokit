VPATH=src:src/py
CFLAGS=-I/usr/include/python3.9
LDFLAGS=-lpython3.9
GCCPY=gcc ${CFLAGS} ${LDFLAGS}

growing:main.o py.o wsgi.o
	${GCCPY} main.o py.o wsgi.o -o growing 
main.o:main.c py.h wsgi.h
	${GCCPY} -c $< -o main.o
py.o:py.c py.h
	${GCCPY} -c $< -o py.o
wsgi.o:wsgi.c wsgi.h
	${GCCPY} -c $< -o wsgi.o


.PHONY:clean
clean:
	rm -rf *.o
