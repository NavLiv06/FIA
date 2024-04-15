%Enfermedades
antecedentes_familiares(A):- A>0.

tabaco(B):- B>0.

contextura(C,D):- Z is (C / (D*D)) , (Z<18.5 ; Z>24.9).

alcohol(E):- E>0.

indigestion(F):- F>0.

alimentacion(G):- G =< 4.

fiebre(H):- H>36.

nauseas(I):- I>0.

dolorC(J):- J>0.


bronquitis(A,B,C,D,X):- antecedentes_familiares(A) , tabaco(B) , contextura(C,D) , X is 1.
tos(A,H,C,D,X):- antecedentes_familiares(A) , fiebre(H), contextura(C,D) , X is 2.
asma(A,I,H,X):- antecedentes_familiares(A) , nauseas(I), fiebre(H) , X is 3.

bulimia(G,I,C,D,X):- alimentacion(G), nauseas(I), contextura(C,D) , X is 4.
anorexia(G,F,C,D,X):- alimentacion(G), indigestion(F), contextura(C,D) , X is 5.
cirrosis(E,B,G,X):- alcohol(E), tabaco(B), alimentacion(G) , X is 6.

gripa(C,D,H,J,X):- contextura(C,D), fiebre(H), dolorC(J) , X is 7.
dolorEstomacal(E,F,G,X):- alcohol(E), indigestion(F), alimentacion(G) , X is 8.
lesion(J,I,H,X):- dolorC(J), nauseas(I), fiebre(H) , X is 9.

nombre_enfermedad(1,'bronquitis').
nombre_enfermedad(2,'tos').
nombre_enfermedad(3,'asma').
nombre_enfermedad(4,'bulimia').
nombre_enfermedad(5,'anorexia').
nombre_enfermedad(6,'cirrosis').
nombre_enfermedad(7,'gripa').
nombre_enfermedad(8,'dolor estomacal').
nombre_enfermedad(9,'lesion').

%Tratamiento
tratamiento('bronquitis', 'beber liquidos en abundancia.').
tratamiento('tos', 'Toma abundantes liquidos, sobre todo tibios.').
tratamiento('asma', 'Medicamentos de accion rapida.').

tratamiento('bulimia', 'Terapia con un especialista calificado').
tratamiento('anorexia', 'Amor propio.').
tratamiento('cirrosis', 'Antidepresivos, que te anexen.').

tratamiento('gripa', 'Paracetamol.').
tratamiento('dolor estomacal', 'Pepto Bismol.').
tratamiento('lesion', 'Curita :).').

enfermedad(A,B,C,D,E,F,G,H,I,J,X):- bronquitis(A,B,C,D,X) ;
                                    tos(A,H,C,D,X) ;
                                    asma(A,I,H,X) ;
                                    bulimia(G,I,C,D,X) ;
                                    anorexia(G,F,C,D,X) ;
                                    cirrosis(E,B,G,X) ;
                                    gripa(C,D,H,J,X) ;
                                    dolorEstomacal(E,F,G,X) ;
                                    lesion(J,I,H,X).

diagnostico(A,B,C,D,E,F,G,H,I,J,Enfermedad,Tratamiento):- enfermedad(A,B,C,D,E,F,G,H,I,J,X) ,
                                                          nombre_enfermedad(X,Enfermedad) ,
                                                          tratamiento(Enfermedad,Tratamiento).



%write(escribe_) , read(X) , diagnostico(X,Y,Z).
