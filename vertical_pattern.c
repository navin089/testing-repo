#include<stdio.h>
#include<string.h>
int main()
{
int n,i,j;
char name[100];
long int len;
printf("\n Enter name :\n");
scanf("%s",name);
len=strlen(name);
for(i=0;i<len;i++)
{
for(j=0;j<=i;j++)
{
printf(" %c ",name[j]);
}
printf("\n");
}
for(i=len-2;i>=0;i--)
{
for(j=0;j<=i;j++)
{
printf(" %c ",name[j]);
}
printf("\n");
}


return 0;
}
