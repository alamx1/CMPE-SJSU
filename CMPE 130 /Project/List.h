#ifndef LIST_H
#define LIST_H

#include <iostream>
#include <vector>

#include "Links.h"

using namespace std;

class List{
 public:
  List();
  List(int size,vector<vector< int> > map);
  void initGraph();
  void addConnection(int src, int dest);
  void printList();
  void minSpanTree();
  void createGraph();
  bool isTop();
  bool isLeft();
  bool isRight();
  bool isBottom();
 private:
  vector<Links> vertices;
  vector<vector<int> > map;
  int size;
  int rowLength;
};

#endif
