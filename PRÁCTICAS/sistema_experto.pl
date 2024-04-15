%Respiratorias
antecedentes_familiares(1,'nunca').
antecedentes_familiares(2,'a veces').
antecedentes_familiares(3,'siempre').

tabaco(0,'nada').
tabaco(1,'poco').
tabaco(2,'mucho').
tabaco(3,'excesivo').

contextura(1, 'beso').
contextura(2, 'normal').
contextura(3, 'delgado').


%TA
alcohol(0,'nada').
alcohol(1,'poco').
alcohol(2,'mucho').
alcohol(3,'excesivo').

indigestion(0, 'nunca').
indigestion(1, 'una vez').
indigestion(2, 'muchas veces').
indigestion(3, 'siempre').

alimentacion(1,'vegetales').
alimentacion(2,'frutas').
alimentacion(3,'pescados y encurtidos').

%Malestar
fiebre(1, 'nada').
fiebre(2, 'leve').
fiebre(3, 'media').
fiebre(4, 'elevada').

nauseas(1, 'no').
nauseas(2, 'si').

dolorC(1, 'no').
dolorC(2, 'cabeza').
dolorC(3, 'brazos y piernas').
dolorC(4, 'pecho').
write(escribe_), read(X), cita(A,X), preguntas(A,B).

%Categoria de cita
cita(1, 'R'). %Respiratoria
cita(2, 'TA'). %Transtornos alimenticios
cita(3, 'M'). % Malestar general

%Preguntas por categoria
preguntas(1,'antecedentes_familiares').
preguntas(1,'tabaco').
preguntas(1,'contextura').

preguntas(2, 'alcohol').
preguntas(2, 'indigestion').
preguntas(2, 'alimentacion').

preguntas(3, 'fiebre').
preguntas(3, 'nauseas').
preguntas(3, 'dolor corporal').


%Tratamiento
tratamiento('Bronquitis', 'beber líquidos en abundancia.').
tratamiento('Tos', 'Toma abundantes líquidos sobre todo tibios.').
tratamiento('Asma', 'Medicamentos de acción rápida.').

tratamiento('Bulimia', 'Terapia con un especialista calificado').
tratamiento('Anorexia', 'Amor propio.').
tratamiento('Cirrosis', 'Antidepresivos, que te anexen.').

tratamiento('Gripa', 'Paracetamol.').
tratamiento('Dolor estomacal', 'Vepto Bismol.').
tratamiento('Lesion', 'Curita :).').


diagnostico(X, Y, Z):- enfermedad(X, Y) , tratamiento(Y, Z).
%write(escribe_), read(X),diagnostico(X, Y,Z).

enfermedad(X, Y):- dolor(Z,X), Z is 1, Y = 'si'.
