Q=@

HDR = $(wildcard *.h)
SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o)

default: test.exe
	
test: test.exe
	$(Q)echo Lancement du test
	$(Q)/usr/bin/sudo ./$<

ssh_test:
	$(Q)echo Lancement du test par SSH
	$(Q)rsync -rav -e ssh . raspberry:rotopano/Firmware/driver_i2c_lsm9ds0
	$(Q)ssh raspberry "cd rotopano/Firmware/driver_i2c_lsm9ds0 && make test"

test.exe: $(OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ -o $@ $^ -lpigpio -lpthread

%.o: %.cpp $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ -c $< -o $@
   
clean:
	$(Q)rm -rf $(OBJ) test.exe
	
	
