#!/bin/bash
# ------------------ Bash file for Redis ------------------
# Install Ubuntu in Microsoft Store

# Install Remote - WSL in Visual Studio

# Config Ubuntu in cmd
wslconfig /setdefault Ubuntu

# Install Redis in Visual Studio
## Open WSL terminal
sudo apt-get install redis

# Starting server
redis-server --port 6380

# Testing server
redis-cli ping

# Printing bash file
cat BashRedis.sh

# Redis installeren voor Python
pip install redis