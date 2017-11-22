#!/bin/bash
# fool servers, got Minas help to figure out the Origin part
curl -sL -X 'PUT' -d 'user_id=98' -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
