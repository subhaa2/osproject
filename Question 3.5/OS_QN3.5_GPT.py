from collections import deque

def fifo_page_replacement():
    # Ask for number of page frames
    while True:
        try:
            page_frames = int(input("Enter number of page frames (3–6): "))
            if 3 <= page_frames <= 6:
                break
            else:
                print("Please enter a number between 3 and 6.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

    # Ask for the reference string
    while True:
        reference_input = input("Enter a reference string (15–25 integers separated by spaces): ")
        reference = reference_input.strip().split()
        if 15 <= len(reference) <= 25:
            try:
                reference = list(map(int, reference))
                break
            except ValueError:
                print("Make sure all inputs are integers.")
        else:
            print("Reference string must have between 15 and 25 numbers.")

    memory = deque()  # Queue to represent pages in memory
    page_faults = 0

    print("\n--- FIFO Page Replacement Simulation ---\n")

    for i, page in enumerate(reference):
        print(f"Reference {i+1}: Page {page}")

        if page in memory:
            print(f"-> Page {page} is already in memory (HIT)")
        else:
            page_faults += 1
            if len(memory) < page_frames:
                memory.append(page)
                print(f"-> Page {page} added to memory (Page Fault)")
            else:
                removed = memory.popleft()
                memory.append(page)
                print(f"-> Memory full. Removed Page {removed}, added Page {page} (Page Fault)")

        print(f"Current Memory: {list(memory)}\n")

    print("Final Memory State:", list(memory))
    print(f"Total Page Faults: {page_faults}")

# Run the function
fifo_page_replacement()
