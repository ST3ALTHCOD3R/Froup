#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define CONTENT_LENGTH getenv("CONTENT_LENGTH")

void profile(char *tok){
   char attribute[strlen(tok)];
   int i;
   for (i=0; i < strlen(tok); i++){ 
      if(tok[i] != '='){
         attribute[i] = tok[i];
      }
      else break;
   }
   attribute[i] = '\0';
   i++;
   int j = 0;
   if(strcmp(attribute, "uName") == 0){//check username
      for(; tok[i] != '\0'; i++){
         attribute[j] = tok[i];
         j++;
      }
      attribute[j] = '\0';
      printf("Username: %s<br />", attribute);
      //checkUnique(attribute);
   }
   else if(strcmp(attribute, "pWord") == 0){//password
      for(; tok[i] != '\0'; i++){
         attribute[j] = tok[i];
         j++;
      }
      attribute[j] = '\0';
      printf("Password: %s<br />", attribute);
   } 
   else if(strcmp(attribute, "fName") == 0){//full name
      for(; tok[i] != '\0'; i++){
         if(tok[i] == '+') attribute[j] = ' ';
         else attribute[j] = tok[i];
         j++;
      }
      attribute[j] = '\0';
      printf("Name: %s<br />", attribute);
   }
   else if(strcmp(attribute, "uJob") == 0){//job description
      for(; tok[i] != '\0'; i++){
         if(tok[i] == '+') attribute[j] = ' ';
         else attribute[j] = tok[i];
         j++;
      }
      attribute[j] = '\0';
      printf("Description: %s<br />", attribute);
   }
}

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
               profile(token);
               token = strtok(NULL, "&");
            }
         }
      }
   }
   printf("</body>");
   printf("</html>");
   return 0;
}
