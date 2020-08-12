#include<stdio.h>
#include<stdlib.h>

int main(){
	
	int i = 5; //integer value
	char str1[50]; //character string
	char m[] = "Mishan"; //charachter string
	char a = "Y"; //character
	double d = 15.26455254666; //double
	float f = 10.2536; //floating value
	printf("Hello World\n");
	printf("%d, %d\n", i, 10); //decimal Value
	printf("%f\n", 10.1); //float value
	printf("%c\n", 'r'); //character value
	printf("%lf\n", 10.2548456650); //large float value
	printf("%ld\n", 125469874562); //large decimal value
	printf("%s\n", "The name is Mishan"); //string
	printf("%s\n", m); //string
	printf("%x", 16); //hexadecimal value
    printf("%s", str1);
	printf("Enter name: ");
    scanf("%s", str1);
    printf("%s", str1);
	puts("\nHey There");
	return 0;
}
