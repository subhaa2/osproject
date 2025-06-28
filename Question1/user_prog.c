#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <fcntl.h>      // open()
#include <unistd.h>     // read(), write(), close()
#include <errno.h>
#include <time.h>

#define DEVICE_PATH "/dev/mychardev"
#define BUFFER_SIZE 1024

int main() {
    int fd;
    char read_buffer[BUFFER_SIZE];
    const char *user_message = "Hello from user space";
    time_t current_time;

    // Get the current time
    time(&current_time);
    printf("[User] Time before sending: %s", ctime(&current_time));

    // Open the device file
    fd = open(DEVICE_PATH, O_RDWR);
    if (fd < 0) {
        perror("Failed to open the device");
        return errno;
    }

    printf("[+] Device opened successfully.\n");

    // Write to the device
    ssize_t bytes_written = write(fd, user_message, strlen(user_message));
    if (bytes_written < 0) {
        perror("Failed to write to the device");
        close(fd);
        return errno;
    }
    printf("[+] Wrote to the device: \"%s\"\n", user_message);

    // Read from the device
    ssize_t bytes_read = read(fd, read_buffer, BUFFER_SIZE - 1);
    if (bytes_read < 0) {
        perror("Failed to read from the device");
        close(fd);
        return errno;
    }

    read_buffer[bytes_read] = '\0';  // Null-terminate the string

    // Get the current time after reading
    time(&current_time);
    printf("[User] Time after reading: %s", ctime(&current_time));

    printf("[+] Read from the device: \"%s\"\n", read_buffer);

    // Close the device file
    close(fd);
    printf("[+] Device closed.\n");

    return 0;
}
