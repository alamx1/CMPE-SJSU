#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <sys/wait.h>
#include <semaphore.h>

#define MSG_LEN 80
#define READ_END 0
#define WRITE_END 1

//sem_t mutex;

int main(){  
  int fd[2];
  char recvd_msg[MSG_LEN];

  pipe(fd); //Creating a pipe fd[0] is for reading and fd[1] is for writing  	    
  pid_t pid = fork();

  //sem_init(&mutex, 1, 1); 

  if (pid < 0){//Fork failed
    printf("Fork error!\n");
    exit(2);
  } else if (pid > 0 ){//pid is parent
    //Begin Critical Section
    //sem_wait(&mutex);
    
    //compose the message to pass
    char mssg[] = "I am your Daddy! and my name is";
    int count = sprintf(mssg, "%s %ld", mssg, (long)getpid());
    //printf("%s\n",mssg);
    
    //writing the message into the pipe
    write(fd[WRITE_END],mssg,strlen(mssg));
    close(fd[WRITE_END]);
    
    //End Critical Section
    //sem_post(&mutex);

    //Move to Child Process   
    wait(0);

    //Begin Critical Section
    //sem_wait(&mutex);
    
    //Reading the message from the pipe
    read(fd[READ_END],recvd_msg,MSG_LEN);
    printf("%s\n",recvd_msg);
    close(fd[READ_END]);    
    
    //End Critical Section
    //sem_post(&mutex);

  } else {//pid is child
    //Begin Critical Section 
    //sem_wait(&mutex);
    
    //compose the message to pass
    char mssg[] = "Daddy, my name is ";
    int count = sprintf(mssg, "%s %ld", mssg, (long)getpid());
    //printf("child message: %s\n",mssg);

    //Reading the message from the pipe
    read(fd[READ_END],recvd_msg,MSG_LEN);
    close(fd[READ_END]);
    printf("%s\n",recvd_msg);

    //writing the message into the pipe
    write(fd[WRITE_END],mssg,strlen(mssg));
    close(fd[WRITE_END]);

    //End Critical Section
    //sem_post(&mutex);
  }
  return 0;
}
