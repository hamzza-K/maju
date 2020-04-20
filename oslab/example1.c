#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

void *myfunc(void *n)
{
	int *age = (int *) malloc (sizeof(int));
	*age = 6;
	return age;
}

int main(int argc, char *argv)
	{
		pthread_t thread;
		pthread_create(&thread, NULL, myfunc, NULL);
		int *a;
		pthread_join(thread, (void *) &a);
		printf("Age= %d", *a);
	}

