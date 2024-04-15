#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DIG 3 /*Numero maximo de digitos*/
#define MIN_NUM 0 /*Numero minimo del intervalo*/
#define MAX_NUM 200/*Numero maximo del intervalo*/

/*Estructura para guardar los numeros del intervalo*/
typedef struct listNode{
	int number;
	struct listNode *next;
}node;

typedef node *list;

/*Elige un numero aleatoriamente*/
void random(int *randomNum){
	/*Generador congruencial Xn = (numeroRandom)*X_n-1 + 1 mod 200, el numero generado no puede sobrepasar el modulo*/
	/*Consideraciones: n=1, Xn=6, Un=0.6666, Xn-1=1*/
	int index = 0;
	int x = 1;
	
	/*Genera el numero aleatorio*/
	srand (time(NULL));
	int numRand = rand() % (MAX_NUM - MIN_NUM + 1) + MIN_NUM;
	
	/*Guarda los numeros aleatorios en un array dinamico*/
	while(index < (MAX_NUM - MIN_NUM) + 1){
		x = (numRand *(x) + 1) % 200;
		randomNum[index] = x;
		index = index + 1;
	}
	
}

/*Devuelve el numero aleatorio y separa los digitos en un arreglo*/
int randomDigit(int *randomNum, int index, int *num){
	num[0] = randomNum[index] / 100;
	num[1] = (randomNum[index] % 100)/10;
	num[2] = randomNum[index] % 10;
	
	return randomNum[index];
}

/*Funcion para verificar si la lista esta vacia*/
int emptyList(list lista){
   return (lista == NULL);
}

/*Funcion para insertar un nuevo nodo a la lista*/
void insertNode(list *num, int n){
	list aux = (struct listNode *)malloc(sizeof(listNode));
	aux->number = n;
	aux->next = *num;
	*num=aux;
}

/*Funcion para eliminar un nodo de la lista*/
void deleteNode(list &num, int n){
   list node, prev;
   node = num;
   int flg = 0;

   if(num!=NULL){
      while(node != NULL){
         if(node->number == n){
            flg=1;
            //printf("Registro Eliminado\n");
            if(node == num)
               num = num->next;
            else
               prev->next= node->next;
         
            delete(node);
            return;
         }
         prev = node;
         node = node->next;
      }
   }
   else
      printf(" Lista vacia\n");

   if(flg == 0 )
      //printf("No se encontro el registro\n");
      printf("-");
}

/*Funcion para imprimir la lista*/
 void printList(list lista){
   list node = lista;
   
   if(emptyList(node)) printf("Lista vacia\n");
   else{
   		while(node) {
			printf("[%d] ", node->number);
    		node = node->next;
			}
    	printf("\n");
	}
}

/*Funcion para verificar si algun numero en el intervalo es igual a la suma de sus cuadrados*/
void findNum(int min, int max, int *square){
	
	/*Se añaden todos los numeros a probar a una lista*/
	int size = MAX_NUM - MIN_NUM + 1;
	list num = (list) malloc(size * sizeof(list));
	num = NULL;
	
	for(int index = 0; index < size; index++){
		insertNode(&num, index + MIN_NUM);
	}
	
	/*Imprime la lista de numeros*/
	printList(num);
	
	int indexNum = 0;
	/*Se repite hasta que la lista este vacia*/
	while(!emptyList(num) && indexNum < size){
		/*Puntero para separar el numero en digitos*/
		int *n;
		n = (int *) malloc(MAX_DIG * sizeof(int));
		
		/*Puntero para guardar los numeros generados aleatoriamente*/
		int *randomNum = (int *) malloc(size * sizeof(int));
		random(randomNum);
		
		/*Se imprime el valor elegido*/
		int x = randomDigit(randomNum, indexNum, n);
		printf("X: %d  ", x);
		
		/*Se realiza la suma de cuadrados*/
		int add = 0;
		int digit;
		for(int i=0; i < MAX_DIG; i++){
			digit = n[i];
			add = add + square[digit];
		}
		
		/*Se imprime la suma*/
		printf("Add: %d\n", add);
		
		/*Si la suma es igual al numero se imprime un mensaje*/
		if(x == add) printf("Cumple el numero %d\n", x);
		
		else{ /*Si no cumple se elimina de la lista*/
			deleteNode(num, x);
			printf("No cumple el numero %d\n", x);
		}
		
		indexNum++;
	}
	
}

int main(void){

	/*Calcular el cuadrado de numeros del 0 al 9*/
	int square[10];
	for(int i=0; i<10; i++){
		square[i] = pow(i,2);
	}

	findNum(MIN_NUM,MAX_NUM,square);
	return 0;
}
