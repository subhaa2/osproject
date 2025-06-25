from collections import deque

def get_valid_page_frames(): # returns a list of valid page frames
    while True: # loop until we get a valid page frame
        try:
            pf = int(input("Enter number of page frames (3–6): "))
            if 3 <= pf <= 6:
                return pf
            else:
                print("Please enter a number between 3 and 6.")
        except ValueError: # if the input is not an integer, ask again    
            print("Invalid input. Please enter an integer.")

def get_valid_reference_string(): # returns a list of valid reference string
    while True: # loop until we get a valid reference string
        try:
            ref = list(map(int, input("Enter 15–25 page numbers separated by spaces: ").split()))
            if 15 <= len(ref) <= 25:
                return ref
            else:
                print("Reference string must have 15 to 25 numbers.")
        except ValueError:
            print("All inputs must be valid integers.")

def simulate_fifo():
    print("\n--- FIFO Page Replacement Simulation ---")
    page_frames = get_valid_page_frames() # get the number of page frames
    reference = get_valid_reference_string() # get the reference string

    memory = deque() # initialize the memory as a queue
    page_fault_count = 0 # initialize the page fault count

    print(f"\n{'Step':<6}{'Page':<6}{'Action':<35}{'Memory State'}") # print the header
    print("-" * 70) # print a separator line

    for i, page in enumerate(reference): # iterate over the reference string
        if page in memory: # if the page is already in memory
            action_msg = f"Page {page} HIT" # print a hit message
        else:
            page_fault_count += 1 # increment the page fault count
            if len(memory) < page_frames: 
                memory.append(page) # if memory isnt full, add the page to the memory
                action_msg = f"Page {page} FAULT - Appended" 
            else:
                removed = memory.popleft()
                memory.append(page)
                action_msg = f"Page {page} FAULT - Removed {removed}, Added" #if memory is full, pop oldest and add

        print(f"{i+1:<6}{page:<6}{action_msg:<35}{list(memory)}")

    fault_rate = (page_fault_count / len(reference)) * 100 # calculate the page fault rate
    print("\nFinal Memory State:", list(memory))
    print(f"Total Page Faults: {page_fault_count}")
    print(f"Page Fault Rate: {fault_rate:.2f}%")

# Run simulation loop
while True: # loop until user chooses to exit
    simulate_fifo()
    again = input("\nWould you like to run another simulation? (y/n): ").strip().lower() # ask user if they want to run another simulation
    if again != 'y':
        print("Goodbye!")
        break





                          
                      
