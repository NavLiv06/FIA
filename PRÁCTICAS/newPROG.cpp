#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DIG 3 /*Numero maximo de digitos*/
#define MIN_NUM 50 /*Numero minimo del intervalo*/
#define MAX_NUM 200 /*Numero maximo del intervalo*/

typedef struct listNode{
	int number;
	struct listNode *next;
}node;

typedef node *list;

/*Elige un numero aleatoriamente*/
/*Devuelve el numero aleatorio y separa los digitos en un arreglo*/
int randomDigit(int *num, int max, int min){
	srand (time(NULL));
	
	/*Genera el numero aleatorio*/
	int x = rand() % (max - min + 1) + min;
	
	/*Separar en digitos*/
	num[0] = x / 100;
	num[1] = (x % 100)/10;
	num[2] = x % 10;
	
	return x;
}

int emptyList(list lista){
   return (lista == NULL);
}

void insertNode(list *num, int n){
	list aux = (struct listNode *)malloc(sizeof(listNode)); //Crear un nuevo nodo.
	aux->number = n; //Asignar el valor al nodo.
	aux->next = *num; //Apuntar el nodo al nodo que apuntaba la lista.
	*num=aux; //Hacer que la lista apunte al nodo nuevo.
	//printf("Se agrego el %d a la lista\n",n); //Escribir en pantalla que se agregó el valor a la lista.
}/* inserta el valor n al frente de la lista */

 void deleteNode(list &num, int n){
   list node, prev;
   node = num;
   int flg = 0;

   if(num!=NULL)
   {
      while(node != NULL)
      {
         if(node->number == n)
         {
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
      //printf(" Lista vacia..!\n");
      printf("-");

   if(flg == 0 )
      //printf("No se encontro el registro\n");
      printf("-");
}

 void printList(list lista)
{
   list node = lista;
   
   if(emptyList(node)) printf("Lista vacia\n");
   else{
   		while(node) {
			printf("%d -> ", node->number);
    		node = node->next;
			}
    	printf("\n");
	}
}

void findNum(int min, int max, int *square){ /*int *squares, int *n, int max, int min*/
	int min2 = min, max2 = max;
	/*Se añaden todos los numeros a probar a una lista*/
	int size = MAX_NUM - MIN_NUM + 1;
	list num = (list) malloc(size * sizeof(list));
	num = NULL;
	
	for(int index = 0; index < size; index++){
		insertNode(&num, index + MIN_NUM);
	}
	
	
	//deleteNode(num, 150);
	//printList(num);
	
	/*Pruebas
	insertNode(num, 10);
	insertNode(num, 14);
	insertNode(num, 18);
	insertNode(num, 6);
	
	deleteNode(*num, 10);
	deleteNode(*num, 6);
	
	printList(*num);
	*/
	
	/*Se repite hasta que la lista este vacia*/
	while(!emptyList(num) && max2 > 0){
		/*Toma el numero aleatorio*/
		/*Puntero para separar el numero en digitos*/
		int *n;
		n = (int *) malloc(MAX_DIG * sizeof(int));
		
		int x = randomDigit(n, max2, min2);
		printf("X: %d  ", x);
		
		/*Verifica si cumple con la condicion, si lo hace lo imprime*/
		
		int add = 0;
		int digit;
		for(int i=0; i < MAX_DIG; i++){
			/*Suma de cuadrados*/
			digit = n[i];
			add = add + square[digit];
		}
		
		printf("Add: %d\n", add);
		//printf("Num: %d", n[MAX_NUM - mid]);
		if(x == add) printf("Cumple el numero %d\n", x);
		else{ /*Si no cumple se elimina de la lista*/
			deleteNode(num, x);
			printf("No cumple el numero %d\n", x);
			max2 = max2 - 1;
		}
		//printList(num);
	}
	/*Verifica si cumple con la condicion, si lo hace lo añade a una estructura de datos*/
	
	/*Si no cumple se elimina de la lista*/
	
	
}
/*Verifica si cumple con la condicion, si lo hace lo añade a una estructura de datos*/

/*Si no cumple se elimina de la lista*/
/*Se modifican los limites de numeros aleatorios, el parametro menos 1*/

int main(void){
	/*Calcular el cuadrado de numeros del 0 al 9*/
	int square[10];
	for(int i=0; i<10; i++){
		square[i] = pow(i,2);
	}
	findNum(50,200,square);
	return 0;
}
