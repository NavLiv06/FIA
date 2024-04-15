#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DIG 3 /*Numero maximo de digitos*/
#define MIN_NUM 0
#define MAX_NUM 200

int randomDigit(int *num){
	//int x = 153;
	srand (time(NULL));
	int x = rand() % (MAX_NUM - MIN_NUM + 1) + MIN_NUM;
	
	/*Separar en digitos*/
	num[0] = x / 100;
	num[1] = (x % 100)/10;
	num[2] = x % 10;
	
	return x;
}

int main(){
	int square[10];
	/*Calcular el cuadrado de numeros del 0 al 9*/
	for(int i=0; i<10; i++){
		square[i] = pow(i,2);
	}
	
	/*Imprimir el cuadrado de numeros del 0 al 9
	for(int i=0; i<10; i++){
		printf("[%d] ", square[i]);
	}
	*/
	
	int *num;
	
	num = (int  *) malloc(MAX_DIG * sizeof(int));
	
	
	/*Prueba para separar digitos
	randomDigit(num);
	for(int i=0; i<MAX_DIG; i++){
		printf("[%d]", num[i]);
	}
	*/
	
	
	int *n;
	int size = MAX_NUM - MIN_NUM + 1;
	
	n = (int *) malloc(size * sizeof(int));
	
	/*Inicializar array en -1*/
	for(int j=0; j < size; j++){
		n[j] = -1;
	}
	
	for(int j=0; j < size; j++){
		printf("[%d]", num[j]);
	}
	
	int pend = MAX_NUM - MIN_NUM;
	
	while(pend > 0){
		/*Se genera un numero random y se separa en digitos*/
		int x = randomDigit(num);
		
		for(int i=0; i<MAX_DIG; i++){
			printf("[%d]", num[i]);
		}
		printf("\n");
		
		/*Se inicia la suma en 0*/
		int add = 0;
		int digit;
		/*Se hace la suma del cuadrado de los digitos*/
		for(int i=0; i< MAX_DIG; i++){
			/*Suma de cuadrados*/
			digit = num[i];
			add += square[digit];
		}
		
		if(n[x-MIN_NUM] == -1){
			n[x-MIN_NUM] = add;
			if(n[x-MIN_NUM] == x){
				printf("%d\n", n[x-MIN_NUM]);
			}
			//pend = pend - 1;
		}
		pend = pend - 1;
		//printf("\n\n%d\n", add);
		//printf("%d\n", n[x-MIN_NUM]);
	}
	
	for(int i=0; i < (MAX_NUM - MIN_NUM); i++){
		printf("[%d]", num[i]);
	}
	
	
	return 0;
}
