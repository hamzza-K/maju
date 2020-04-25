#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>

int array[100];
void *function (void *n)
{
   int * thr = (int *)n;
   int a = 0;
   int b = 1;
   int c = 0;

   for(int i=1; i<*thr ;i++){
       c = a + b;
       a = b;
       b = c;
       array[i-1] = c;
      }
}

int main(int argc, char *argv[]){
   
   int a = atoi(argv[1]);
   printf("The number is %d\n", a);
   // scanf("%d", &a);

   pthread_t thread;
   
   pthread_create(&thread, NULL, function, &a); 
   pthread_join(thread,NULL); 
     
   printf("fibonacci series: %d %d ", 0, 1);          
   for(int i = 0;i<a-2;i++){
      printf("%d ", array[i]);

   }
   printf("\n");

   return EXIT_SUCCESS;
}