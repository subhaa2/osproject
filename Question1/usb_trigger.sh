#!/bin/bash


export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

LOGFILE="/tmp/usb_trigger.log"
exec > "$LOGFILE" 2>&1
echo "==== USB Device Detected ===="

cd /home/subhashini/osproject2 || exit 1

echo "[1] Compiling kernel module..."
/usr/bin/make clean && /usr/bin/make
if [ $? -ne 0 ]; then
    echo "Compilation failed"
    exit 1
fi

echo "[2] Removing existing kernel module (if any)..."
/usr/sbin/rmmod usb_driver 2>/dev/null

echo "[3] Inserting kernel module..."
/usr/sbin/insmod usb_driver.ko || echo "Insert failed"

echo "[4] Creating device node..."
MAJOR=$(grep mychardev /proc/devices | awk '{print $1}')
if [ -z "$MAJOR" ]; then
    echo "Major number not found, using default 240"
    MAJOR=240
fi
/usr/bin/mknod -m 666 /dev/mychardev c $MAJOR 0

echo "[5] Compiling user-space program..."
/usr/bin/gcc -o user_prog user_prog.c
if [ $? -ne 0 ]; then
    echo "User program compilation failed"
/usr/sbin/rmmod usb_driver
    exit 1
fi

echo "[6] Running user-space program..."
./user_prog

echo "[7] Kernel messages:"
/usr/bin/dmesg | tail -n 20

echo "[8] Cleaning up..."
/usr/sbin/rmmod usb_driver

echo "==== Script Completed ===="
