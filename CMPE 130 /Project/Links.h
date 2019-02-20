#ifndef LINKS_H
#define LINKS_H

#include <iostream>
#include "Node.h"

class Links{ 
 public:
  Links();
  ~Links();
  void addTailNode(int vrtx, int wght);//, Node *nxt);
  void printLinkedList();
 private:
  Node *front; 
  Node *tail;
};

#endif
