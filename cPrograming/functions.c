#include<stdio.h>
#include<stdlib.h>

int sum(); //prototyping the function as we called it after main
int Add();
//Main FUnction
int main(){
	int one , two;
	printf("Enter number 1:\t");
	scanf("%d", &one);
	printf("\nEnter number 2:\t");
	scanf("%d", &two);
	
	sum(); //can be called multiple time
	printf("\n");
	Add(5,10);
	Add(15,20);
	Sub(one, two);
}

//simple function
int sum(){
	printf("The sum is %d", 10+15);	
}

// function with parameter
int Add(int num1, int num2){
	int add;
	add = num1 + num2;
	printf("Addition = %d\n", add);	
}

int Sub(int numm1, int numm2){
	int sub;
	sub = numm1 - numm2;
	printf("Subtraction = %d\n", sub);
}

