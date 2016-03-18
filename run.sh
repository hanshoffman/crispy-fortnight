#!/bin/sh

echo "Starting implant"
`which python` implant.py &> log.txt &
echo "Sleeping for 1 second"
sleep 1
implant=$(pidof python)
echo "Starting controller"
`which python` controller.py
kill -9 $implant
