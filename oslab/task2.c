#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>


void *function (void * n)
{
   int thread = *(int *) n;
  
   int i,j;
    printf("Prime numbers are: \n");    
    for(i=2;i<=thread;i++)
    {
        int a=0;
        for(j=1;j<=i;j++)
        {
            if(i%j==0)
            {
                a++;
            }
        }
       if(a==2)
        {
            printf("%d \n",i);
        }
    }
}

int main(int argc, char *argv[])
{
   

   printf("The argument is %s: \n", argv[1]);
   int n = atoi(argv[1]);


   pthread_t t;

   pthread_create(&t, NULL, function, &n); 
    pthread_join(t,NULL); 
   
   return EXIT_SUCCESS;
     
}
