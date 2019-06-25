#!/bin/bash
git pull --no-edit
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/lexconvert.py
git commit -am "Update lexconvert" && git push
