//----TO PRINT CORRESPONDANT 'EXCEL' COLUMN NAME BY GIVEN INPUT NUMBER------
#include<stdio.h>
#include<string.h>
int main()
{
char st[10];
int i=0,rem,n;

printf("\n Enter Number :\n");
scanf("%d",&n);
 while(n>0)
  {
   rem=n%26;
   if(rem==0){
     st[i++]='Z';
     n=(n/26);
             }
   else{
    st[i++]=(rem-1)+'A';
    n=n/26;
       }
  }
st[i]='\0';
printf("\n EXCEL COLUMN : ");
  for(i=strlen(st);i>=0;i--)
    printf("%c",st[i]);
printf("\n");
return 0;
}
