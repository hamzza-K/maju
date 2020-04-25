
#include <pthread.h> 
#include <stdio.h> 
#include<stdlib.h>
#define total 3
#define length 7

int counter = 0;
int sum = 0;
float average;
void *function(void *n)
{

int * thr = (int *) n;


    if(counter == 0){
       printf("thread %d\n", counter+1);
        for(int i = 0;i<length;i++){
             sum = sum + thr[i];
             average = sum/7;
           }
       printf("average : %f",average);
       counter++;
    }else if(counter == 1){
     printf("\n--------  thread %d --------\n", counter+1);
          int min = thr[0];
  
          for(int j = 0;j<length;j++){
             if(min > thr[j]){

                min = thr[j];

               }
          }
       printf("minimum : %d", min);
    
       counter++;
    }else if(counter == 2){
           printf("\n--------  thread %d --------\n", counter+1);
           int max = thr[0];
  
          for(int j = 0;j<7;j++){
             if(max < thr[j]){

                max = thr[j];

               }
          }
       printf("maximum: %d\n", max);        

 
           counter++;
    }
  
    
    

}

int main(int args, char *argv[])
{
   
   int arr[length];
   pthread_t threads[total]; 

   
   printf("::enter a sequence of integers:: \n");
   for(int i = 0;i<length;i++){
    printf("-> ");
      scanf("%d", &arr[i]);
 
   }
  
   for (int t=0; t <total; t++)
    {
       pthread_create (&threads[t], NULL, function,arr);
       pthread_join (threads[t], NULL);
     }

     return EXIT_SUCCESS;
   
}