#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define CONTENT_LENGTH getenv("CONTENT_LENGTH")
FILE *file;
char line[300];//so it remembers the username when coming bak to check if password is correct
int checkCorrect(char *input){
   char attribute[strlen(input)];
   int i, userInterval = 0;
   if(input[0] == '\n')printf("it is null");
   for (i=0; i < strlen(input); i++){
      if(input[i] != '='){
         attribute[i] = input[i];
      }
      else break;
   }
   attribute[i] = '\0';
   i++;
   int j = 0;
   printf("Attribute: %s<br />", attribute);
   if(strcmp(attribute, "uName") == 0){//check username
      for(; input[i] != '\0'; i++){
         attribute[j] = input[i];
         j++;
      }
      attribute[j] = '\0';//to get the value of uName
      fgets(line, 299, file);
      while(!feof(file)){
         if(userInterval%4 == 0){
            j=0;
            while(line[j] != '\n'){
               j++;
            }
            line[j] = '\0';
            if(strcmp(attribute, line) == 0){
               return 1;//username found 
            }
         }
         userInterval++;
         fgets(line, 299, file);
      }   
      return 0;
   }
   else if(strcmp(attribute, "pWord") == 0){
      for(; input[i] != '\0'; i++){
         attribute[j] = input[i];
         j++;
      }
      attribute[j] = '\0';//to get the value of uName
      fgets(line, 299, file);//to get the password for that specific user
      printf("password on file: %s and password to check: %s<br />", line, attribute);
      j=0;
      while(line[j] != '\n'){
         j++;
      }
      line[j] = '\0';
      if(strcmp(attribute, line) == 0){
         return 1;//password correct
      }
   }
}

int main(){
   int n;
   file = fopen("users.txt","rt");
   char *token, *inputString = NULL;
   printf("Content-Type:text/html\n\n");
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
               if(checkCorrect(token)){
                  token = strtok(NULL, "&");
               }
               else{ printf("username does not exist"); return 1;}//username does not exist
            }
            printf("Password is correct");
            return 0;//password is right to the username
         }
      }
   }
   printf("</body>");
   printf("</html>");
   return 0;
}
