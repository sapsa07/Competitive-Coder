/*
If we declare a variable v of type int, v will actually store a value. v is equal to zero now.
However, each variable, apart from value, also has its address (or, simply put, where it is located in the memory). 
The address can be retrieved by putting an ampersand (&) before the variable name.

If you print the address of a variable on the screen,
it will look like a totally random number (moreover, it can be different from run to run).

Now, what is a pointer? Instead of storing a value, a pointer will y store the address of a variable.

Int *y = &v;

*/
#include<stdio.h>

int main(){
	int v = 0;
	printf("&v :%d\n",&v);
	
	int *y = &v;
	printf("*y :%d\n",*y);
	
	return 0;
}
