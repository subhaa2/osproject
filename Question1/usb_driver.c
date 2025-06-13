#include <linux/init.h>
#include <linux/module.h>
#include <linux/fs.h>
#include <linux/uaccess.h>  // for copy_to_user, copy_from_user
#include <linux/cdev.h>

#define DEVICE_NAME "mychardev"
#define CLASS_NAME "mycharclass"
#define BUFFER_SIZE 1024

MODULE_LICENSE("GPL");
MODULE_AUTHOR("Your Name");
MODULE_DESCRIPTION("A simple Linux char driver for USB flash interaction");
MODULE_VERSION("1.0");

static int major_number;
static char kernel_buffer[BUFFER_SIZE] = {0};
static struct class* char_class = NULL;
static struct device* char_device = NULL;
static struct cdev my_cdev;

// Called when the device is opened
static int dev_open(struct inode *inodep, struct file *filep) {
    printk(KERN_INFO "mychardev: Device opened\n");
    return 0;
}

// Called when data is sent from user-space
static ssize_t dev_write(struct file *filep, const char __user *buffer, size_t len, loff_t *offset) {
    if (len > BUFFER_SIZE) len = BUFFER_SIZE;

    if (copy_from_user(kernel_buffer, buffer, len) != 0)
        return -EFAULT;

    printk(KERN_INFO "mychardev: Received from user: %s\n", kernel_buffer);
    return len;
}

// Called when user-space reads from device
static ssize_t dev_read(struct file *filep, char __user *buffer, size_t len, loff_t *offset) {
    const char *message = "Hello World from the kernel space";
    size_t msg_len = strlen(message);

    if (*offset >= msg_len)
        return 0;

    if (len > msg_len - *offset)
        len = msg_len - *offset;

    if (copy_to_user(buffer, message + *offset, len) != 0)
        return -EFAULT;

    *offset += len;
    printk(KERN_INFO "mychardev: Sent to user: %s\n", message);
    return len;
}

// Called when the device is closed
static int dev_release(struct inode *inodep, struct file *filep) {
    printk(KERN_INFO "mychardev: Device closed\n");
    return 0;
}

// File operations structure
static struct file_operations fops = {
    .open = dev_open,
    .write = dev_write,
    .read = dev_read,
    .release = dev_release,
};

// Module init function
static int __init mychar_init(void) {
    printk(KERN_INFO "mychardev: Initializing...\n");

    // Allocate major number
    major_number = register_chrdev(0, DEVICE_NAME, &fops);
    if (major_number < 0) {
        printk(KERN_ALERT "mychardev: Failed to register a major number\n");
        return major_number;
    }

    // Create device class
    char_class = class_create(THIS_MODULE, CLASS_NAME);
    if (IS_ERR(char_class)) {
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "mychardev: Failed to register device class\n");
        return PTR_ERR(char_class);
    }

    // Create the device
    char_device = device_create(char_class, NULL, MKDEV(major_number, 0), NULL, DEVICE_NAME);
    if (IS_ERR(char_device)) {
        class_destroy(char_class);
        unregister_chrdev(major_number, DEVICE_NAME);
        printk(KERN_ALERT "mychardev: Failed to create the device\n");
        return PTR_ERR(char_device);
    }

    // Initialize and add the cdev structure
    cdev_init(&my_cdev, &fops);
    my_cdev.owner = THIS_MODULE;
    cdev_add(&my_cdev, MKDEV(major_number, 0), 1);

    printk(KERN_INFO "mychardev: Device created successfully\n");
    return 0;
}

// Module exit function
static void __exit mychar_exit(void) {
    cdev_del(&my_cdev);
    device_destroy(char_class, MKDEV(major_number, 0));
    class_unregister(char_class);
    class_destroy(char_class);
    unregister_chrdev(major_number, DEVICE_NAME);
    printk(KERN_INFO "mychardev: Goodbye from the module!\n");
}

module_init(mychar_init);
module_exit(mychar_exit);
