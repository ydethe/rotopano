Q=@

SRC= $(wildcard *.cpp)
OBJ= $(SRC:.cpp=.o)

default: test.exe
	
test: test.exe
	$(Q)echo Lancement du test
	$(Q)./$<

test.exe: $(OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ -o $@ $^ -lwiringPi

%.o: %.cpp
	$(Q)echo Compilation de $<
	$(Q)g++ -c -I. $< -o $@
   
clean:
	$(Q)rm -rf $(OBJ) test.exe
	
	