#include<stdio.h>
#include<pthread.h>
#include<stdlib.h>
#include<semaphore.h>
#include<unistd.h>

int amount = 5000;
sem_t dis;

void *deposit (void *x)
{
    int *d = (int *) x;
    printf("\nTotal amount: %d\n", amount);
    
    sem_wait(&dis);
    for(int i = 0 ; i < *d ; i++)
    {
        amount = amount + 1;
    }
    sleep(1);
    
    printf("deposited: %d\n", *d);
    sem_post(&dis);
}

void *withdraw (void *x)
{

    int *w = (int *) x;
    sem_wait(&dis);
    for(int j = 0 ; j < *w ; j++)
    {
        amount = amount - 1;
    }
    
    sleep(2);    
    printf("withdrawal: %d\n", *w);
    sem_post(&dis);
}

int main(int argc, char *argv[])
{

     int dept, with;
    printf("Enter the deposit amount: ");
    scanf("%d", &dept);
    printf("Enter the withdraw amount: ");
    scanf("%d", &with);
    sem_init(&dis, 0, 1);
    pthread_t thread1;
    pthread_t thread2;
    pthread_create(&thread1, NULL, deposit, &dept);
    sleep(2);
    pthread_create(&thread2, NULL, withdraw, &with);
    pthread_join(thread1, NULL);    
    pthread_join(thread2, NULL);
    printf("\nTotal amount after transactions: %d\n", amount);
    sem_destroy(&dis);

    return EXIT_SUCCESS;


}