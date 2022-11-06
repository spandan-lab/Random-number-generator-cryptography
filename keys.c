#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#define KEYSIZE 16

void main(){
	char key[KEYSIZE];
	FILE *fl;
	fl = fopen("keys.txt","w");
	for(time_t time=1524013729; time<1524020929; time++)
	{
		srand(time);
		
		for(int i=0; i<KEYSIZE; i++)
		{
			key[i] = rand()%256;
			fprintf(fl,"%.2x", (unsigned char) key[i]);
		}
		fprintf(fl,"\n");

	}
}
