# include<stdlib.h>
# include<stdio.h>
# include<string.h>
#define CONTENT_LENGTH getenv("CONTENT_LENGTH")


int main(){


//interfacing using Post
//Receives hidden type Username value from dashboard.py

   int n;
   char *inputString = NULL;
   char user[n];

   if(CONTENT_LENGTH != NULL){
      n = atoi(CONTENT_LENGTH);
      if((inputString = malloc(sizeof(char) * (n+1))) != NULL){
         if((fread(inputString, sizeof(char), n, stdin)) == n){
            strcpy(user, inputString);
            
            printf("str length: %d and string is: %s.<br />",n, user);
  
         }
	  }
	}
	
	//Starts building SeeFriends html webpage
	
	
	printf("Content-Type:text/html\n\n");

	printf ("<html><head><br/>");
	printf ("<title>Friends:</title>");
	printf ("</head><body><h1>See Friends:</h1><br/>");
	
	printf("<form action='profile.py' method='post'>");
	printf("<fieldset><legend><b>Your Froup:</b></legend>");
	printf("<input type='hidden' name='user' value='%s'/>", user);
	
	

	
	
	FILE *friends = fopen("friends.txt", "rt");
	
	char friendList[100];
	char *word;
	
	
	//For each line in friends.txt, tokenizes first word in each line (aka current username), and checks if it 
	// is same as username currently logged into website (user variable)
	
	while (!feof(friends)){
		fgets(friendList, 100, friends);
		
		word=strtok(friendList, " ");
			
			
			
		// When row with matching leading username is found, remaining friend usernames in row are tokenized
		//and added to the checkbox list of the user's friends.
			
		if (strcmp(word, user)==0){
			
			word = strtok( NULL, " ");
			while( word != NULL){
				
				
				printf("<input type='checkbox' name='friendName' value='%s'>'%s'</br", word , word );
				word = strtok( NULL, " ");

			}
				
		break;	
			
		}
	}
	
	printf("</fieldset></form>");
	printf("</body></html>");
	

	return 0;
}


