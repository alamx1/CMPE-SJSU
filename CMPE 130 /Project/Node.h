#ifndef NODE_H
#define NODE_H

#include <iostream>

class Node{
  friend class List;
  friend class Links;
 public:
  Node() {vertex = 0; weight = 0; next = NULL;}
  Node(int vrtx, int wght) {vertex = vrtx; weight = wght; next = NULL;} 
 private:
  int vertex;
  int weight;
  Node *next;
};

#endif 
