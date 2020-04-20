#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>



void *entry_point(void *value)
{
	printf("Hello from the second thread!\n");
	int *num = (int *) value;
	printf("the value is %d", *num);
		return NULL;
}

int main(int argc, char **argv) {
	pthread_t thread;

	printf("Hello from the first thread!\n");

	int num = 123;

	pthread_create(&thread, NULL, entry_point, &num);

	pthread_join(thread, NULL);

	return EXIT_SUCCESS;
}