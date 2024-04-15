#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>

#define MAX_DIG 3 /*Numero maximo de digitos*/
#define MIN_NUM 0 /*Numero minimo del intervalo*/
#define MAX_NUM 200/*Numero maximo del intervalo*/

/*Estructura para guardar los numeros del intervalo*/
typedef struct queue{
	int nodeNumber;
	int parentNode;
	int level;
	char operation;
	struct queue *next;
}queueNode;

typedef queueNode *node;

/*Funcion para verificar si la lista esta vacia*/
int emptyQueue(node queue){
   return (queue == NULL);
}

/*Funcion para insertar un nuevo nodo a la lista*/
void insertNode(node *nodo, int number, int parent, int level, char mov){
	node aux = (struct queue *)malloc(sizeof(queue));
	aux->nodeNumber = number;
	aux->parentNode = parent;
	aux->level = level;
	aux->operation = mov;
	aux->next = *nodo;
	*num=aux;
}

/*Funcion para eliminar un nodo de la lista*/
void deleteNode(node &num, int n){
   node nodo, prev;
   nodo = num;
   int flg = 0;

   if(num!=NULL){
      while(nodo != NULL){
         if(nodo->nodeNumber == n){
            flg=1;
            //printf("Registro Eliminado\n");
            if(nodo == num)
               num = num->next;
            else
               prev->next= nodo->next;
         
            delete(nodo);
            return;
         }
         prev = nodo;
         node = nodo->next;
      }
   }
   else
      printf(" Lista vacia\n");

   if(flg == 0 )
      //printf("No se encontro el registro\n");
      printf("-");
}

/*Funcion para imprimir la lista*/
void printQueue(node queue){
   node nodo = queue;
   
   if(emptyQueue(nodo)) printf("Lista vacia\n");
   else{
   		while(nodo) {
			printf("[%d] ", nodo->nodeNumber);
    		nodo = nodo->next;
			}
    	printf("\n");
	}
}

void BFS_Search(int[] puzzle, int[] goal){
	int seen[] = puzzle;
}
