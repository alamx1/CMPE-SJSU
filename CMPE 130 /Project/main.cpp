#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>

#include "List.h"

using namespace std;

int main(){
  string line;
  ifstream fin;

  fin.open("data.txt");
  if(fin.fail()) cout << "Error reading data text file.\n";
  
  vector<vector<int> > map;
  while(getline(fin,line)){
    //cout << line << endl;
    stringstream ss;
    ss << line;
    vector<int> row;
    int temp;
    while(ss>>temp){
      //cout << temp << endl;
      row.push_back(temp);
      map.push_back(row);
    }
  }
  
  int mapSize = 0;
  if(!map.empty())
    mapSize = map.size() * map[0].size();
  cout << mapSize << endl;

  List temp(mapSize,map);
  temp.printList();
  //temp.createGraph();
  //temp.printList();
}
