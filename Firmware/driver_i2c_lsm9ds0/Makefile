Q=@

HDR = $(wildcard *.h)
SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o)

default: test.exe
	
test: test.exe
	$(Q)echo Lancement du test
	$(Q)/usr/bin/sudo ./$<

test.exe: $(OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ -o $@ $^ -lpigpio -lpthread

%.o: %.cpp $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ -c $< -o $@
   
clean:
	$(Q)rm -rf $(OBJ) test.exe
	
	