#!/bin/bash


export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# Path to the log file - log standard output (stdout) and standard error (stderr)
LOGFILE="/tmp/usb_trigger.log"
exec > "$LOGFILE" 2>&1
echo "==== USB Device Detected ===="

# =======[ CONFIGURABLE DIRECTORY ]=======
BASE_DIR="/path/to/your/project"  # <-- Change this path during submission
cd "$BASE_DIR" || exit 1
# ========================================

# Check if the kernel module source exists
echo "[1] Compiling kernel module..."
/usr/bin/make clean && /usr/bin/make
if [ $? -ne 0 ]; then
    echo "Compilation failed"
    exit 1
fi

# Remove existing kernel module if it exists
echo "[2] Removing existing kernel module (if any)..."
/usr/sbin/rmmod usb_driver 2>/dev/null

# Insert the kernel module
echo "[3] Inserting kernel module..."
/usr/sbin/insmod usb_driver.ko || echo "Insert failed"

# Create device node if it does not exist with the specified major number ($MAJOR) and a minor number of 0. 
echo "[4] Creating device node..."
MAJOR=$(grep mychardev /proc/devices | awk '{print $1}')
if [ -z "$MAJOR" ]; then
    echo "Major number not found, using default 240"
    MAJOR=240
fi
#-m 666 option sets the permissions of the device node to allow read and write access for everyone.
/usr/bin/mknod -m 666 /dev/mychardev c $MAJOR 0

# Compile the user-space program into an executable
echo "[5] Compiling user-space program..."
/usr/bin/gcc -o user_prog user_prog.c
# if the compilation fails, exit with an error message and remove the kernel module
if [ $? -ne 0 ]; then
    echo "User program compilation failed"
/usr/sbin/rmmod usb_driver
    exit 1
fi

# Run the compiled user-space program
echo "[6] Running user-space program..."
./user_prog

# Display the last 20 lines of the log file
echo "[7] Kernel messages:"
/usr/bin/dmesg | tail -n 20

# Clean up by removing the kernel module
echo "[8] Cleaning up..."
/usr/sbin/rmmod usb_driver

echo "==== Script Completed ===="
