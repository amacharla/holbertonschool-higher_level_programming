#!/bin/bash
# get using special header
curl -s -X POST -d email='hr@holbertonschool.com' -d subject='I will always be here for PLD' "$1"
