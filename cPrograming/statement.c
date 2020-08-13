#include<stdio.h>
#include<stdlib.h>

int main(){
	
	//use of scanf
	int age, weight;
	printf("Please enter your age:\t");
	scanf("%d", &age);
	printf("\n");
	printf("Your age is %d\n", age);


	//if statement
	if (age < 18){
		printf("\nYou are under age.\n");
	}
	if (age == 18){
		printf("\nYou are fit a/c to your age.\n");
	}
	if (age > 18){
		printf("\nYou are an grown man/women.\n");
	}
	
	
	//if else statement
	printf("\n\nEnter your weight: ");
	scanf("%d", &weight);
	printf("\nYour weight is %d\n", weight);
	
	if (weight > 80){
		printf("You are overweight.\n");
	}
	else if (weight == 80){
		printf("Your weight is 80 kg.\n");
	}
	else{
		printf("Your weight is fine.\n");
	}
	
	
	//nested if else statement
	if(age < 18 ){
		printf("\nYour are under 18.");
		if(weight < 80){
			printf("And weight is also less than 60.");
		}
		else{
			printf("And weight is more than 60.");
		}
	}
	
	
	//the ternary conditional operator
	int num1 , num2, ans;
	printf("Enter the first number.\n");
	scanf("%d", &num1);
	printf("Enter the second number.\n");
	scanf("%d", &num2);
	
	ans = ( num1 > num2 /*checking condition*/ ) ? (num1 /*true then get this*/) : (num2 /*if false*/);
   	printf("The greater number is %d", ans); 
	
	
	// switch case
	int ch;
	char g;
	char name[20];
	printf("1. Enter details\n2. Display Detail\nOther Number. Exit Program\n\n");
	printf("Enter your choice:\t");
	scanf("%d", &ch);
	
	switch(ch){
		case 1:
			printf("Enter your name:\t");
			scanf("%s", &name);
			printf("Enter your gender (M or F):\t");
			fflush(stdin);
			scanf("%c", &g);
			break;
		case 2:
			printf("Your name is %s ", name);
			printf("\tAnd your gender is %c", g);
			break;
		default :
			printf("Thank You");
	}
	
	
	//while loop
	int wh = 0;
	while(wh < 10){
		printf("\nValue of wh is %d\n", wh);
		wh++;
	}


	//do while loop
	int ii = 0;
	do
	{
		printf("The value of ii is %d\n", ii);
		ii++;
	}
	while(ii < 10);	


	//for loop
	int j ;
	for (j=1; j<=10; j++){
		printf("Number = %d\n", j);
	}
	
}
