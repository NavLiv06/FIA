% Torres de Hanoi
torresHanoi(0,A,B,C).
torresHanoi(D,A,B,C):-D > 0,
                      D1 is D-1,
                      torresHanoi(D1,A,C,B),
                      write("Se mueve el disco de la torre "),
                      write(A),
                      write(" a la torre "),
                      write(B),
                      nl,
                      torresHanoi(D1,C,B,A).
                      

