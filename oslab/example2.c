#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>

void *myfunc(void * args)
{
	pthread_detach(pthread_self());
	printf("Inside the thread\n");

	pthread_exit(NULL);
}

void myfun2()
{
	pthread_t ptid;

	pthread_create(&ptid, NULL, &myfunc, NULL);
	printf("this line may be printed before thread terminates\n");

	pthread_cancel(ptid);

	if(pthread_equal(ptid, pthread_self()))
	{
		printf("threads are equal\n");
	}
	else
	{
		printf("threads are not equal\n");
	}
	pthread_join(ptid, NULL);
	printf("This line will be printed after the thread ends\n");
	pthread_exit(NULL);
}

int main(int argc, char *argv)
{
	myfun2();
}

