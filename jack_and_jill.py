"""first number is max number
    second number is maximum allowed distance 
    third number is number of moves
    
    10 3 5
    4 6 7 9 5"""

def main():
    n = 10
    k = 3
    m = 5

    sequence = []
    longest_seq = []
    for _ in range(3):
        user = input("Enter number: ")
        seen = [int(user)]
        while True:
            user = int(input("Enter number(-1 to stop): "))
            
            if len(seen) > m:
                sequence = seen
                print("Invalid")
                break
            if user in seen:
                sequence = seen
                print("Invalid")
                break
            if abs(user - seen[-1]) > k:
                sequence = seen
                print("Invalid")
                break
            if user == -1:
                sequence = seen
                print("done")
                break
            seen.append(user)
        seen = []

        if len(sequence) > len(longest_seq):
            longest_seq = sequence
    
        
    return f"Longest running valid sequence {longest_seq}"
        

    
if __name__ == "__main__":
   print(main())