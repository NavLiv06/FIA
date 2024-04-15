%Sumatoria
sumatoria(X,N,0):- X>N, !.
sumatoria(X,N,R):- X1 is X+1,
                    sumatoria(X1,N,R1),
                    R is X + R1.
                    

