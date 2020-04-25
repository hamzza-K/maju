#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<unistd.h>


int total_amount = 5000;
pthread_mutex_t lock = PTHREAD_MUTEX_INITIALIZER;

void *deposit (void *x)
{
    int *d = (int *) x;
    printf("\nTotal amount: %d\n", total_amount);
    printf("\nDeposit amount: %d\n", *d);
    
    for(int i = 0 ; i < *d ; i++)
    {
        pthread_mutex_lock (&lock);
        total_amount = total_amount + 1;
        pthread_mutex_unlock (&lock);
        
    }
}

void *withdraw (void *x)
{
    int *w = (int *) x;

    printf("\nWithdraw amount: %d\n", *w);

    for(int j = 0 ; j < *w ; j++)
    {
        pthread_mutex_lock (&lock);
        total_amount= total_amount - 1;
        pthread_mutex_unlock (&lock);
    }
    
}




int main(int argc, char *argv[])
{
    pthread_t thread1;
    pthread_t thread2;

    int dept, with;
    printf("Enter the deposit amount: ");
    scanf("%d", &dept);
    printf("Enter the withdraw amount: ");
    scanf("%d", &with);
    

    pthread_create(&thread1, NULL, deposit, &dept);
    pthread_create(&thread2, NULL, withdraw, &with);
    pthread_join(thread1, NULL);    
    pthread_join(thread2, NULL);
    printf("\nTotal amount after deposit and withdraw %d\n", total_amount);

    return EXIT_SUCCESS;
}