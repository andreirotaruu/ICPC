# Problem D of the 2025 ICPC Regional Contest

def main():
    n, k = map(int, input().split())

    intervals = []

    for _ in range(n):
        start, end = map(int, input().split())
        intervals.append((start, end))


    
    answer = 0
    for i in range(24):
        active_users = 0
        for interval in intervals:
            start = interval[0]
            end = interval[1]

            if start <= i < end:
                active_user+=1

        if active_users >= k:
            answer+=1

    print(answer)

if __name__ == '__main__':
    main()