#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DIG 3 /*Numero maximo de digitos*/
#define MIN_NUM 50 /*Numero minimo del intervalo*/
#define MAX_NUM 200 /*Numero maximo del intervalo*/

void random(int *randomNum){
	
	/*Generador congruencial Xn = 5xn-1 + 1 mod 9*/
	/*Consideraciones: n=1, Xn=6, Un=0.6666, Xn-1=1*/
	int index = 0;
	int x = 1;
	srand (time(NULL));
	int numRand = rand() % (MAX_NUM - MIN_NUM + 1) + MIN_NUM;
	
	while(index < (MAX_NUM - MIN_NUM) + 1){
		x = (numRand *(x) + 1) % 10000;
		randomNum[index] = x;
		printf("%d\n", x);
		index = index + 1;
	}
	
	/*Genera el numero aleatorio*/
	//int x = rand() % (max - min + 1) + min;
	
	/*Separar en digitos*/
	/*num[0] = x / 100;
	num[1] = (x % 100)/10;
	num[2] = x % 10;*/
}

int randomDigit(int *randomNum, int index, int *num){
	num[0] = randomNum[index] / 100;
	num[1] = (randomNum[index] % 100)/10;
	num[2] = randomNum[index] % 10;
	
	for(int i=0;i < MAX_DIG;i++){
		printf("[%d] ", num[i]);
	}
	printf("\n");
	
	return randomNum[index];
}

int main(void){
	/*Se añaden todos los numeros a probar a una lista*/
	int size = MAX_NUM - MIN_NUM + 1;
	int *randomNum = (int *) malloc(size * sizeof(int));
	
	int *n;
	n = (int *) malloc(MAX_DIG * sizeof(int));
	
	int index = 1;
	while(index < size){
		random(randomNum);
		int x = randomDigit(randomNum, index, n);
		index = index + 1;
	}
	
	//printf("X: %d", x);
	return 0;
}
