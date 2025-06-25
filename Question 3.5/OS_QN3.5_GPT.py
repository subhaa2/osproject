from collections import deque

# Ask for number of page frames
while True:
    try:
        page_frames = int(input("Enter number of page frames (3–6): "))
        if 3 <= page_frames <= 6:  # Check if the number of page frames is between 3 and 6
            break
        else:
            print("Please enter a number between 3 and 6.")  # If not, ask again
    except ValueError:
        print("Invalid input. Please enter an integer.")

# Ask for the reference string
while True:
    reference_input = input("Enter a reference string (15–25 integers separated by spaces): ")
    reference = reference_input.strip().split()  # Split the input into a list of integers
    if 15 <= len(reference) <= 25:  # Check if the reference string has 15 to 25 integers
        try:
            reference = list(map(int, reference))
            break
        except ValueError:  # If not, ask again 
            print("Make sure all inputs are integers.")
    else:
        print("Reference string must have between 15 and 25 numbers.")

memory = deque()  # Queue to represent pages in memory
page_faults = 0

print("\n--- FIFO Page Replacement Simulation ---\n") # Print the simulation header

def draw_memory(memory, page_frames): # Function to draw the memory
    print("Memory State:")
    for i in range(page_frames): # Loop through each page frame
        if i < len(memory): # If the page frame is in memory
            val = str(memory[i]) # Add
        else: # If the page frame is not in memory
            val = " " # Add a space
        print(f"+-----+") # Print the top border
        print(f"| {val.center(3)} |") # Print the page frame
    print(f"+-----+" * (1 if page_frames == 1 else 1)) # Print the bottom border
    print()

for i, page in enumerate(reference):
    print(f"Reference {i+1}: Page {page}")  # Print the current reference string

    if page in memory:
        print(f"-> Page {page} is already in memory (HIT)")  # If the page is in memory, print a hit
    else:
        page_faults += 1  # Increment the page faults counter
        if len(memory) < page_frames:
            memory.append(page)
            print(f"-> Page {page} added to memory (Page Fault)")
        else:
            removed = memory.popleft()  # Remove the first page from memory
            memory.append(page)
            print(f"-> Memory full. Removed Page {removed}, added Page {page} (Page Fault)")

    print(f"Current Memory: {list(memory)}") # Print the current memory state
    draw_memory(memory, page_frames) # Draw the memory state
    print()

print("Final Memory State:", list(memory)) # Print the final memory state
print(f"Total Page Faults: {page_faults}") # Print the total page faults
