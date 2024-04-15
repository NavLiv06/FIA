%Facts
ai(X):- programa(X).

%Rules
programa(X):- usa_algoritmo(X,Y).

usa_algoritmo(X,Y):- algoritmo (Y), implementos (X, Y).

implementos(X, Y):- utiliza_lenguaje_de_programacion(X, Z), admite (Z, Y).

usa_programacion_lenguaje(X, Z):- lenguaje_programacion(Z), escrito_en(X, Z).

escrito_en(X,Z):- lenguaje(Z), utiliza (X, Z).

%Algoritmos
algoritmo(sistema_basado_en_reglas).
algoritmo(aprendizaje_maquina).
algoritmo(procesamiento_del_lenguaje_natural).
algoritmo(razonamiento_probabilistico).
algoritmo(redes_neuronales).

%Programming_Languages
lenguaje_programación(prolog).
lenguaje_programacion(python).
lenguaje_programacion(java).
lenguaje_programacion(lisp).
lenguaje_programacion(c++).

%Lenguajes
lenguaje(prolog).
lenguaje(python).
lenguaje(java).
lenguaje(lisp).
lenguaje(c++).

%Support
admite(prolog, sistema_basado_en_reglas).
admite(prolog, aprendizaje automatico).
admite(python, machine_learning).
admite(python, procesamiento_lenguaje_natural).
admite(java, razonamiento_probabilistico).
admite(ceceo, redes_neuronales).
admite(c++, redes_neuronales).

%Usos
utiliza(IA_programa_1, prolog).
utiliza(IA_programa_2, python).
utiliza(IA_programa_3, java).
utiliza(IA_programa_4, lisp).
utiliza(IA_programa_5, c++).
