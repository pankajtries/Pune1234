import heapq

def printJobScheduling(arr):
    n = len(arr)

    arr.sort(key=lambda x: x[1])

    result = []
    maxHeap = []

    for i in range(n - 1, -1, -1):
        if i == 0:
            slots_available = arr[i][1]
        else:
            slots_available = arr[i][1] - arr[i - 1][1]

        heapq.heappush(maxHeap, (-arr[i][2], arr[i][1], arr[i][0]))

        while slots_available and maxHeap:
            # get the job with max_profit
            profit, deadline, job_id = heapq.heappop(maxHeap)

            slots_available -= 1

            result.append([job_id, deadline])

    result.sort(key=lambda x: x[1])

    for job in result:
        print(job[0], end=" ")
    print()

# Driver's Code
if __name__ == '__main__':
    num_jobs = int(input("Enter the number of jobs: "))
    arr = []
    print("Enter job details in the format 'job_id deadline profit':")
    for _ in range(num_jobs):
        job_id, deadline, profit = input().split()
        arr.append([job_id, int(deadline), int(profit)])

    print("Following is maximum profit sequence of jobs")

    # Function Call
    printJobScheduling(arr)
"""

Enter the number of jobs: 5
Enter job details in the format 'job_id deadline profit':
a 1 10
b 1 5
c 2 9
d 2 4
e 2 19
Following is maximum profit sequence of jobs
a e 
"""
