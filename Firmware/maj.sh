#! /bin/sh


cd ~/Downloads/RTIMULib2/Linux/python
CC="ccache gcc" python setup.py install 
cd -
python Fusion.py
