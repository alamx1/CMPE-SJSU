#include <stdio.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <semaphore.h>
#include <fcntl.h>
#include <string.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <sys/socket.h>

static sem_t mutex;

int main(int argc,char **argv) {
  int p=0,c=0,m=0,q=0,depth=0,u=0,s=0,e=0;
  const int SIZE = 4096;
  const char *name = "OS";
  char *mssg = NULL;

  sem_init(&mutex,1,1);
  if(argc == 1){
    printf("Invalid input, please enter at least one argument into the command line\n");
  } else {
    for(int i = 1; i < argc; i++){
      //printf("i: %d String: %s\n",i,argv[i]);
      if(argv[i][0] == '-') {
	if (argv[i][1] == 'p') {//program will run as producer
	  //printf("Run as producer\n");
	  if(c) printf("Error: Already set as consumer\n");
	  else p = 1;
	} else if (argv[i][1] == 'c') {//program will act as consumer
	  //printf("Run as consumer\n");
	  if(p) printf("Error: Already set as producer\n");
	  else c = 1;
	} else if (argv[i][1] == 'm') {//indicates next item is the message to be produced
	  m = 1;
	  //printf("Message coming up\n");
	  mssg = argv[i+1];
	  //mssg = temp;
	  //printf("Message: %s\n",mssg);
	} else if (argv[i][1] == 'q') {
	  q = 1;
	  //printf("Read -q\n");
	  //depth = *argv[i+1]-48;
	  depth = (int)*argv[i+1];
	  //printf("Depth: %d\n",depth);
	} else if (argv[i][1] == 'u') {
	  if (s) printf("Error: Already set to use semaphores\n");
	  else u = 1;
	  //printf("Read -u\n");
	} else if (argv[i][1] == 's') {
	  if (u) printf("Error: Already set to use unix sockets\n");
	  else s = 1;
	  //printf("Read -s\n");
	} else if (argv[i][1] == 'e') {
	  e = 1;
	  //printf("Read -e\n");
	} else {
	  printf("Invalid argument[s]\n");
	} 
      }  
      //else move on
    }
  }
  //if (mssg)  printf("%s\n",mssg);
  printf("p: %d c: %d m: %d q: %d u: %d s: %d e: %d\n",p,c,m,q,u,s,e); 

  if(s){//Using Shared Memory
    printf("Begin shared memory\n");
    int shm_fd;
    void *ptr;

    if(p){//producer
      printf("Act as producer\n");
      sem_wait(&mutex);
      shm_fd = shm_open(name, O_CREAT | 2, 0666);
      ftruncate(shm_fd, SIZE);
      ptr = mmap(0, SIZE, PROT_WRITE, MAP_SHARED, shm_fd, 0);
      sprintf(ptr,"%s",mssg);
      ptr += strlen(mssg);
      if(e) printf("%s\n",mssg);
      sem_post(&mutex);
    } else if(c){//consumer
      sem_wait(&mutex);
      shm_fd = shm_open(name, O_RDONLY, 0666);
      ptr = mmap(0, SIZE, PROT_READ, MAP_SHARED, shm_fd, 0);
      if(e) printf("%s\n",(char *)ptr);
      shm_unlink(name);
      sem_post(&mutex);
    } else 
      printf("Error: no form of IPC\n");
  } else if(u) {//Using Sockets
    int sockets[2];
    char buf[256];
    printf("Begin unix sockets\n");

    if (socketpair(AF_UNIX, SOCK_STREAM, 0, sockets) < 0) {
      perror("opening stream socket pair");
      exit(1);
    }
    if(p){//Producer
      printf("Acting as producer\n");
      close(sockets[1]);
      printf("%d\n",write(sockets[0], mssg, sizeof(mssg)) < 0);
      //perror("writing stream message");
      printf("Here\n");
      if(e) printf("here %s\n", mssg);
      close(sockets[0]);
    } else if(c){//Consumer
      close(sockets[0]);
      if (read(sockets[1], buf, sizeof(buf)) < 0)
	perror("reading stream message");
      printf("%s\n", buf);
      close(sockets[1]);
    } else
      printf("Error: no form of IPC\n");
  } else
    printf("Error: No form of IPC\n");
  return 0;
}
