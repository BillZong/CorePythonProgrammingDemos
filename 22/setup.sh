#!/bin/sh

python setup.py build && sudo python setup.py install --record log

# cat ./log | xargs sudo rm -rf && rm -rf build && rm log
