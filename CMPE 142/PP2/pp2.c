#include <stdio.h>
#include <unistd.h>
#include <signal.h>
#include <stdbool.h>

bool sigint = false;

void SIGINT_handler(int);

void SIGUSR1_handler(int);

int main(){
  int i = 1, j = 1;
  while(1){
    signal(SIGUSR1,SIGUSR1_handler);
    signal(SIGINT,SIGINT_handler);
    if(sigint){
      //printf("SIGINT: %d\tInfinite Printing Loop: %d\n",sigint,i);
      printf("Infinite Loop Iteration: %d\n",i);
      i++;
      sleep(2);
    } else {
      //printf("SIGINT: %d\tInfinite Empty Loop: %d\n",sigint,j);
      //j++;
      i++;
      sleep(2);
    } 
  }
  return 0;
}
  
void SIGINT_handler(int sig){
  signal(sig, SIG_IGN);
  if(sigint)
    sigint = false;
  else
    sigint = true;
}

void SIGUSR1_handler(int sig){
  signal(sig,SIG_IGN);
  printf("GRACEFULLY terminating PP2\n");
  exit(0);
}

