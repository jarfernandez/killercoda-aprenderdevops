#!/bin/bash

curl -s http://localhost -o req1.txt
ERROR=$?
curl -s http://localhost -o req2.txt
diff req1.txt req2.txt > /dev/null
DIFF=$?
if [ $ERROR -eq 0 ] && [ $DIFF -eq 1 ]; then
  exit 0
else
  exit 1
fi