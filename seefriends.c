#include<stdlib.h>
#include<stdio.h>
#include<string.h>
#define CONTENT_LENGTH getenv("CONTENT_LENGTH")


int main(){

  printf("Content-Type:text/html\n\n");

  printf ("<html><head><br/>");
  printf ("<title>Friends</title>");
  printf ("<link rel='stylesheet' href='dashboard.css' type='text/css'>");
  printf ("</head><body>");
  printf ("<div id='square'><h1><center>See Friends</center></h1><br /></div>");

  //interfacing using Post
  //Receives hidden type Username value from dashboard.py

   int n;
   char *inputString = NULL;
   n = atoi(CONTENT_LENGTH);
   char user[n];
   if(CONTENT_LENGTH != NULL){
      if((inputString = malloc(sizeof(char) * (n+1))) != NULL){
         if((fread(inputString, sizeof(char), n, stdin)) == n){
            strcpy(user, inputString);
            char *token = strtok(user, "&");
            //printf("str length: %d and string is: %s.<br />",n, user);
  
         }
      }
    }
	
	//Starts building SeeFriends html webpage
	char currentUser[20];
	int i =0, j=0;
	int startRead = 0;	
	for (i = 0; i < strlen(user)-1; i++){
	   if (user[i] == '+'){
	      if (startRead == 0) {i++; startRead = 1;}
	   }
	   if (startRead){
	      currentUser[j] = user[i];
	      j++;
	   }
	}
	currentUser[j] = '\0';
	printf("<form action='profile.py' method='post'>");
	printf("<fieldset><legend><b>Your Froup:</b></legend>");
	
	

	
	
	FILE *friends = fopen("/home/2014/rfrati2/public_html/friends.txt", "rt");
	
	char friendList[100];
	char *word;
	
	int foundUser = 0;
	//For each line in friends.txt, tokenizes first word in each line (aka current username), and checks if it 
	// is same as username currently logged into website (user variable)
	printf("<form action=\"profile.py\" method=\"post\">");
	fgets(friendList, 100, friends);
	while (!feof(friends)){
		word=strtok(friendList, " ");
		// When row with matching leading username is found, remaining friend usernames in row are tokenized
		//and added to the checkbox list of the user's friends.
		//printf("compare word: (%s) with user: (%s); %d<br />", word, currentUser, strcmp(word, currentUser));	
		if (strcmp(word, currentUser)==0){
			foundUser = 1;
			word = strtok( NULL, " ");
			while( word != NULL){
				
				printf("<input type='radio' name='friendName' value='%s'>%s<br />", word , word );
				word = strtok( NULL, " ");
			}
				
			break;	
			
		}
	      fgets(friendList, 100, friends);
	}
	if(foundUser){
		printf("<input type=\"hidden\" name=\"user\" value=\"%s\">", currentUser);
		printf("<input type=\"submit\" value=\"Check'em Out!\">");
	}
	else{
		printf("Please make some friends before you check out a profile!");
	}
	printf("</fieldset></form>");
	printf("<form action='dashboard.py' method='post'>");
	printf("<input type=\"hidden\" name=\"currentUser\" value=\"%s\">", currentUser);
        printf("<input type=\"submit\" value=\"Back to Dashboard!\">");
	printf("</form>");
	printf("</body></html>");
	

	return 0;
}


