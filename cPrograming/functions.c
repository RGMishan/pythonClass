#include<stdio.h>
#include<stdlib.h>

//int sum(); //prototyping the function when we called it after main
//int Add();

//simple function
void sum(){
	printf("The sum is %d", 10+15);	
}

// function with parameter
void Add(int num1, int num2){
	int add;
	add = num1 + num2;
	printf("Addition = %d\n", add);	
}
// function with paramater dynamic value
void Sub(int numm1, int numm2){
	int sub;
	sub = numm1 - numm2;
	printf("Subtraction = %d\n", sub);
}
//function with reutrn type
int Product(int number1, int number2){
	return(number1 * number2);
}
int Divide(int numbeer1, int numbeer2){
	return(numbeer1 / numbeer2);
}


//Main Fnction
int main(){
	int one , two, prod;
	printf("Enter number 1:\t");
	scanf("%d", &one);
	printf("\nEnter number 2:\t");
	scanf("%d", &two);
	
	sum(); //can be called multiple time
	printf("\n");
	Add(5,10);
	Add(15,20);
	Sub(one, two);
	prod = Product(one,two);
	printf("The product of %d and %d is %d", one, two, prod);
	//calling function if print statment with other values
	printf("\nThe sum of product and subtraction result is %d", Product(one,two)+Divide(one,two));
}



