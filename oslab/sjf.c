#include <stdio.h>


int main(int argc, char argv[])
{
	int n, temp, arrival_time[10], pid[10], burst_time[10], completion_time[10], turnaround_time[10], waiting_time[10];
	int total, position;
	float average_waiting_time, average_turnaround_time;

	printf("Enter the total number of processes: ");
	scanf("%d", &n);

	for(int i=0; i<n; i++){
		printf("Enter arrival Time and burst Time: ");
		scanf("%d %d", &arrival_time[i], &burst_time[i]);
		pid[i] = i+1;
	}

	
	for(int i=0; i<n; i++)
	{
		position = i;
		for(int j=i+1; j<n; j++){
			
			if(arrival_time[j] < arrival_time[position]){
				position=j;
			}
			temp = burst_time[i];
			burst_time[i] = burst_time[position];
			burst_time[position] = temp;

			temp = arrival_time[i];
			arrival_time[i] = arrival_time[position];
			arrival_time[position] = temp;

			temp = pid[i];
			pid[i] = pid[position];
			pid[position] = temp;
			}
	}	

	for(int i=0; i<n; i++){
		if(arrival_time[i] == arrival_time[i+1])
		{
			if(burst_time[i] > burst_time[i+1])
			{
				temp = burst_time[i];
			burst_time[i] = burst_time[i+1];
			burst_time[i+1] = temp;

			temp = arrival_time[i];
			arrival_time[i] = arrival_time[i+1];
			arrival_time[i+1] = temp;

			temp = pid[i];
			pid[i] = pid[i+1];
			pid[i+1] = temp;
			}
		}
	}

 waiting_time[0] = 0;            
 
    for(int i=1;i<n;i++)
    {
        waiting_time[i]=0;
        for(int j=0;j<i;j++)
            waiting_time[i] += burst_time[j];
 
        total += waiting_time[i];
    }
 
    average_waiting_time=(float)total/n;     
    total = 0;
 
    printf("\nProcess\t    Burst Time    \tWaiting Time\tTurnaround Time \tArrival Time");
    for(int i=0;i<n;i++)
    {
        turnaround_time[i]=burst_time[i]+waiting_time[i];   
        total += turnaround_time[i];
        printf("\np%d\t\t  %d\t\t    %d\t\t\t%d	  \t\t%d",pid[i],burst_time[i],waiting_time[i],turnaround_time[i], arrival_time[i]);
    }
    average_turnaround_time=(float)total/n;   
    printf("\nAverage Turnaround Time = %.2f",average_turnaround_time);
    printf("\nAverage Waiting Time = %.2f \n",average_waiting_time);
}