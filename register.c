#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define CONTENT_LENGTH getenv("CONTENT_LENGTH")
int main(void){
   int n;
   char *token = NULL;
   char *inputString = NULL;
   printf("Content-Type:text/html\n\n");//to print to browser
   printf("<html>");
   printf("<body>");
   if(CONTENT_LENGTH != NULL){
      n = atoi(CONTENT_LENGTH);
      char manString[n];
      if((inputString = malloc(sizeof(char) * (n+1))) != NULL){
         if((fread(inputString, sizeof(char), n, stdin)) == n){
            strcpy(manString, inputString);
            printf("str length: %d and string is: %s.<br />",n, manString);
            token = strtok(manString, "&");
            while(token != NULL){
               printf("token: %s<br />", token);
               token = strtok(NULL, "&");
            }
         }
      }
   }
   printf("</body>");
   printf("</html>");
   return 0;
}
