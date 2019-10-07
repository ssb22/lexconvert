#!/bin/bash
git pull --no-edit
wget -N http://ssb22.user.srcf.net/gradint/lexconvert.py
git commit -am "Update lexconvert" && git push
