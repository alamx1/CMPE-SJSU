#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <sstream>

#include "List.h"
#include "Links.h"

using namespace std;

bool List::isTop(){

}

bool List::isLeft(){

}

bool List::isRight(){
}

bool List::isBottom(){
}

void List::createGraph(){
  for(int i = 0; i < vertices.size(); i++){
    //    if(isTop());
    //    else if(isRight());
    //    else if(isLeft());
    //    else if(isBottom());
    //    else ;
  }
}

List::List(int size,vector<vector< int> > map){//Assumes input is aquare matrix
  //rowLength = sqrt(size);
  this->size = size;
  this->map = map;
  for(int i = 0; i < size; i++){
    Links temp;
    vertices.push_back(temp);
  }
}

void List::printList(){
  cout << "Adjecnecy List\n";
  for(int i = 0; i < vertices.size(); i++){
    cout << i << ": ";
    vertices[i].printLinkedList();
  }
  cout << endl;
}

void List::addConnection(int src, int dest){
  vertices[src].addTailNode(dest,dest-src);
}

