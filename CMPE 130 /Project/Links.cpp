#include <iostream>

#include "Links.h"

using namespace std;

Links::Links(){
  front = NULL;
  tail = NULL;
}

Links::~Links(){
  Node *temp = 0;
  while(front){
    temp = front;
    front = temp->next;
    delete temp;
  }
}

void Links::addTailNode(int vrtx, int wght){
  Node *temp = new Node(vrtx,wght);
  if(front){
    if(front->next){
      tail->next = temp;
      tail = temp;
    } else {
      tail = temp;
      front->next = temp;
    }
  } else {
    front = temp;
    tail = temp;
  }
}

void Links::printLinkedList(){
  Node *temp = front;
  if(!front)
    cout << "Empty list.\n";
  while(temp){
    cout << "-> (vertex: " << temp->vertex << ", weight: " << temp->weight << ") ";
    temp = temp->next;
  }
  cout << endl;
}
