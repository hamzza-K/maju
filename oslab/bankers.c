
//Hamzza K

#include <stdio.h>

void algorithm(int processes, int resources, int done[])
{
	int maximum[10][10], need[10][10], allocation[10][10], available[10], sequence[10];
int i, j, counter, count;
count = 0;


printf("\n==========Allocation============");
for(i = 0; i < processes; i++)
{
	printf("\nPID %d: ",i+1);
	for(j = 0; j < resources; j++)
		scanf("%d", &allocation[i][j]);	
}

printf("\n==========Maximum===============");
for(i = 0; i < processes; i++)
{
	printf("\nPID %d: ", i+1);
	for(j = 0; j < resources; j++)
		scanf("%d", &maximum[i][j]);
}
printf("\n=======Available Resources=======\n");
for(i = 0; i < resources; i++)
		scanf("%d", &available[i]);	


	for(i = 0; i < processes; i++)
		for(j = 0; j < resources; j++)
			need[i][j] = maximum[i][j] - allocation[i][j];
		
do
{
	printf("\n Allocation:    \tMaximum:\n");
	for(i = 0; i < processes; i++)
	{
		for( j = 0; j < resources; j++)
			printf("%d  ", allocation[i][j]);
		printf("\t\t");
		for( j = 0; j < resources; j++)
			printf("%d  ", maximum[i][j]);
		printf("\n");
	}

	counter = -1;

	for(i = 0; i < processes; i++)
	{
		if(done[i] == 0)
		{
			counter = i ;
			for(j = 0; j < resources; j++)
			{
				if(available[j] < need[i][j])
				{
					counter = -1;
					break;
				}
			}
		}
		if(counter != -1)
			break;
	}

	if(counter != -1)
	{
		printf("Completed");
		sequence[count] = counter + 1;
		count++;
		for(j = 0; j < resources; j++)
		{
			available[j] += allocation[counter][j];
			allocation[counter][j] = 0;
			maximum[counter][j] = 0;
			done[counter] = 1;
		}
	}
}while(count != processes && counter != -1);

if(count == processes)
{
	printf("\n-------------------\n");
	printf("System is Safe");
	printf("\n-------------------\n");
	printf("\n[ ");
	for( i = 0; i < processes; i++){
			printf("P%d", sequence[i]);
			printf(" | ");
		}
	printf("]\n");
}
else
	printf("\nSystem is Unsafe\n");
}

	
int main(int argc, char argv[])
{
	int i, p, r, done[10];
	// int r = 3;
	printf("# of processes : ");
scanf("%d", &p);

for(i = 0; i< p; i++)
	done[i] = 0;

printf("# of resources : ");
scanf("%d", &r);

	algorithm(p, r, done);
	return 0;
}