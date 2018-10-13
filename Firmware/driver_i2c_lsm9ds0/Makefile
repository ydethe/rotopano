HDR = $(wildcard *.h)
SWG_ITF = $(wildcard *.i)
SWG_SRC = $(SWG_ITF:.i=_wrap.cxx)
SRC = $(wildcard *.cpp)
OBJ = $(SRC:.cpp=.o) $(SWG_SRC:.cxx=.o)
MAIN_OBJ = main.o

PY_CONF = /home/pi/.berryconda/bin/python3-config

INC := $(shell $(PY_CONF) --includes)
CFLAGS := -fPIC $(shell $(PY_CONF) --cflags)
LDFLAGS := $(shell $(PY_CONF) --ldflags)

EXE = test.exe
DLL = _imu_driver.so

ifdef verbose
Q=
else
Q=@
endif

default: $(EXE) $(DLL)

test: test_exe test_py

test_py: $(DLL)
	$(Q)echo $(OBJ)
	$(Q)echo Lancement du test
	$(Q)python test.py 1000
	
test_exe: $(EXE)
	$(Q)echo $(OBJ)
	$(Q)echo Lancement du test
	$(Q)./$<
	
$(DLL): $(OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ $(LDFLAGS) -shared -o $@ $^ -lpigpio -lpthread -lRTIMULib
	
$(EXE): $(OBJ) $(MAIN_OBJ)
	$(Q)echo Edition de liens...
	$(Q)g++ $(LDFLAGS) -o $@ $^ -lpigpio -lpthread -lRTIMULib

%_wrap.cxx: %.i
	$(Q)echo Génération de $@
	$(Q)swig -c++ -python $<

%.o: %.cpp $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ $(INC) $(CFLAGS) -c $< -o $@

%.o: %.c++ $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ $(INC) $(CFLAGS) -c $< -o $@

%.o: %.cxx $(HDR)
	$(Q)echo Compilation de $<
	$(Q)g++ $(INC) $(CFLAGS) -c $< -o $@
   
clean:
	$(Q)rm -rf $(OBJ) $(EXE) $(DLL) $(SWG_SRC) __pycache__
	
	
