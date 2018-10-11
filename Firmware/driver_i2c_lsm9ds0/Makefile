HDR = $(wildcard *.h)
SWG_ITF = $(wildcard *.i)
SWG_SRC = $(SWG_ITF:.i=_wrap.cxx)
SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o) $(SWG_SRC:.cxx=.o)

INC := $(shell python3-config --includes)
CFLAGS := -fPIC $(shell python3-config --cflags)
LDFLAGS := -shared $(shell python3-config --ldflags)

WK_DIR = rotopano/Firmware/driver_i2c_lsm9ds0
EXE = test.exe

ifndef ssh
TEST_DEP=$(EXE)
endif

ifdef verbose
Q=
else
Q=@
endif

debug:
	$(Q)echo $(INC)

default: $(TEST_DEP)
ifeq ($(TEST_DEP), "")
	$(Q)rsync -rav -e ssh . raspberry:$(WK_DIR)
	$(Q)ssh raspberry "cd $(WK_DIR) && make"
endif

test: $(TEST_DEP)
ifndef TEST_DEP
	$(Q)echo Lancement du test par SSH
	$(Q)rsync -rav -e ssh . raspberry:$(WK_DIR)
	$(Q)ssh raspberry ". ~/.zshrc && cd $(WK_DIR) && make verbose=1 test"
else
	$(Q)echo Lancement du test
	$(Q)sudo ./$<
endif

$(EXE): $(OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ $(LDFLAGS) -o $@ $^ -lpigpio -lpthread

%_wrap.cxx: %.i
	$(Q)echo Génération de $@
	$(Q)swig -c++ -python $<

%.o: %.cpp $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ $(INC) $(CFLAGS) -c $< -o $@

%.o: %.cxx $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ $(INC) $(CFLAGS) -c $< -o $@
   
clean:
	$(Q)rm -rf $(OBJ) $(EXE) $(SWG_SRC)
	
	
