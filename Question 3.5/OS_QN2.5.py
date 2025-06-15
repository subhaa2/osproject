from collections import deque

#to ask for user input: page frames
page_frames=int(input("Enter number of page frames, between 3 and 6:" )) #number of pages that can be in memory at once
while page_frames<3 or page_frames>6:
    page_frames=int(input("Enter the number of page frames you want to simulate, between 3 and 6:" ))

#to ask for user input: reference string
reference= input("Enter a sequence of 15 to 25 page numbers, separated by spaces:") #sequence of page numbers accessed by system
reference=list(map(int,reference.split()))
while len(reference) <15 or len(reference) >25:
    reference= input("Enter reference string:")
    reference=list(map(int,reference.split()))

#dynamic queue
memory = deque()
page_fault_count = 0

#page replacement by FIFO
for i, page in enumerate(reference):
    print(f"reference {i+1}: Page {page}")
    if page in memory:
        print(f"page {page} hit")
    else:
        page_fault_count += 1
        print(f"page {page} caused a page fault")
        if len(memory) < page_frames:
            memory.append(page)
            print(f"Appended {page} to memory")
        else:
            removed_page = memory.popleft()
            memory.append(page)
            print(f"memory is full, removed {removed_page}, and appended {page}")

print("\nFinal memory state:",list(memory))
print("total page faults:", page_fault_count)





                          
                      
