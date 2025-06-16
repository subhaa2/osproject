#!/bin/bash

echo "[1] Compiling kernel module..."
make clean && make

if [ $? -ne 0 ]; then
    echo "Compilation failed"
    exit 1
fi

echo "[2] Removing existing module (if loaded)..."
sudo rmmod usb_driver 2>/dev/null

echo "[3] Inserting kernel module..."
sudo insmod usb_driver.ko || echo "Module already inserted or failed"

echo "[4] Creating device node (if needed)..."
# Get major number from dmesg
MAJOR=$(dmesg | grep "mychardev: Device created successfully" -A 5 | grep "mychardev" | tail -n1 | grep -oE "[0-9]+" | head -n1)
if [ -z "$MAJOR" ]; then
    echo "Could not detect major number automatically. You may need to check 'dmesg' manually."
    MAJOR=240 
fi

sudo mknod -m 666 /dev/mychardev c $MAJOR 0 2>/dev/null

echo "[5] Compiling user program..."
gcc -o user_prog user_prog.c

if [ $? -ne 0 ]; then
    echo "User app compilation failed"
    sudo rmmod usb_driver
    exit 1
fi

echo "[6] Running user-space program..."
sudo ./user_prog

echo "[7] Kernel messages:"
dmesg | tail -n 20

echo "[8] Removing module..."
sudo rmmod usb_driver
