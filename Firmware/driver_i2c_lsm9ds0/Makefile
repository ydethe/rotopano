HDR = $(wildcard *.h)
SWG_ITF = $(wildcard *.i)
SWG_SRC = $(SWG_ITF:.i=_wrap.cxx)
SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o) $(SWG_SRC:.cxx=.o)

PY_CONF = /home/pi/.berryconda/bin/python3-config

INC := $(shell $(PY_CONF) --includes)
CFLAGS := -fPIC $(shell $(PY_CONF) --cflags)
LDFLAGS := -shared $(shell $(PY_CONF) --ldflags)

EXE = test.exe

ifdef verbose
Q=
else
Q=@
endif


default: $(EXE)

test: $(EXE)
	$(Q)echo $(OBJ)
	$(Q)echo Lancement du test
	$(Q)sudo ./$<
	
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
	
	
