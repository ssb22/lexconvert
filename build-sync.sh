#!/bin/bash
# sync lexconvert to SVN
wget -N http://people.ds.cam.ac.uk/ssb22/gradint/lexconvert.py
svn commit -m "Update lexconvert"
