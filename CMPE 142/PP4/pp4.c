#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <pthread.h>

pthread_cond_t cv1 = PTHREAD_COND_INITIALIZER, cv2 = PTHREAD_COND_INITIALIZER;
pthread_mutex_t m1 = PTHREAD_MUTEX_INITIALIZER, m2 = PTHREAD_MUTEX_INITIALIZER;

void *child2(){
  //pthread_mutex_lock(&m1);
  while(1){
    pthread_cond_wait(&cv2,&m2);
    printf("thread 2: pong! thread 1 ping received\n");
    sleep(1);
    printf("thread 2: ping thread 1\n");
    pthread_cond_signal(&cv1);
  }
  //pthread_mutex_unlock(&m2);
}

void *child1(){
  //pthread_mutex_lock(&m1);
  while(1){
    printf("thread 1: ping thread 2\n");
    sleep(1);
    pthread_cond_signal(&cv2);
    pthread_cond_wait(&cv1,&m1);
    printf("thread 1: pong! thread 2 ping received\n");
    sleep(1);
  }
  //pthread_mutex_unlock(&m1);
}


int main(){    
  pthread_t t1, t2;

  pthread_create(&t1,0,child1,NULL);
  pthread_create(&t2,0,child2,NULL);
  
  pthread_join(t1,NULL);
  pthread_join(t2,NULL);
  
  return 0;
}
