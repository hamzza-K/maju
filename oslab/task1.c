#include <pthread.h> 
#include <stdio.h> 
#include <stdlib.h>


#define total 3

int counter = 0;

void *function(void *var)
{

    int * thread = (int *)var;
    int result = 0;
    if(counter == 0){
       printf("=========thread number %d========= \n", counter+1);
       result = (*thread) * (*thread);
       printf("square of the number is: %d\n",result);
       counter++;
    
    }
    if(counter == 1){
     printf("==========thread %d==========\n", counter+1);
     printf("table of the thread number %d\n", *thread);
     for(int k=1; k<= 10; k++){
      printf("%d * %d = %d\n",*thread,k,(*thread)*k);
     }
       counter++;
    }
    if(counter == 2){
           printf("==========thread %d===========\n", counter+1);
           if((*thread) % 2 == 0){
              printf("the thread is even\n");
              }else{

              printf("the thread is odd\n");
            }  
           counter++;
    }
  
    
    

}

int main(int argc, char *argv)
{
   pthread_t thread[total]; 
  
   int input;
   printf("Enter a number: ");
   scanf("%d",&input);
   for (int t=0; t <total; t++)
    {
       pthread_create(&thread[t], NULL, function, &input);
       pthread_join(thread[t], NULL);
     }

     return EXIT_SUCCESS;
   
}
