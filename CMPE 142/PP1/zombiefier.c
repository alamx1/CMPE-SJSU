#include <sys/types.h>
#include <sys/wait.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void recursiveFork(pid_t pid, int counter){
  if(counter > 0){
    printf("To fork %d more times\n",counter);
    pid = fork();
    
    if(pid < 0){//fork failed
      printf("Fork Failed");
    } else if (pid > 0) {//parent
      counter--;
      recursiveFork(pid,counter);
    } else if(pid == 0){//if child
      exit(0);
    }
  }
}

void funct(int signum){
  printf("Signal: %d\n",signum);
  wait(NULL);
}

int main(int argc, char **argv){
  if(argc < 3)
    printf("Not enough arguments passed");
  else{
    int n = atoi(argv[2]);
    printf("%d \n", n);
    pid_t pid;
    
    while(n > 0){
      pid = fork();
      n--;
      
      if(pid < 0){
	printf("Fork Failed\n");
	exit(1);
      } else if (pid > 0){
	printf("Zombie pid: %d\n",pid);
	sleep(1);
	//wait(0);
      } else if (pid == 0){
	//signal(SIGCONT,funct);
	exit(0);
      }
    }
    kill(getpid(),SIGSTOP);
    //recursiveFork(pid,n);
    //signal(SIGCONT,funct);
  }
  return 0;
}
