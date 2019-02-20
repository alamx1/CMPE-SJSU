tempMap: main.o List.o Links.o  
	g++ -g -W -Wall -o tempMap main.o List.o Links.o 

# define how each object file is to be built
main.o: main.cpp Links.h List.h
	g++ -c main.cpp

List.o: List.cpp List.h Links.h
	g++ -c List.cpp 

Links.o: Links.cpp Links.h Node.h
	g++ -c Links.cpp

# clean up
clean:
	rm -f  *.o *~
