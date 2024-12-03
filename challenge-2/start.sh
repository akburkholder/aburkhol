#!/bin/bash

set -e 

socat TCP-LISTEN:5555,fork,reuseaddr EXEC:"python3 /app/check_password.py"
