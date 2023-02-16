import heapq



def minMeetingRoomsHeap(intervals):
    '''
    We use a min heap to keep track of the minimum end time of each interval. We start by sorting the intervals by their start time. Then, we add the end time of the first interval to the heap. For each subsequent interval, we check if its start time is greater than or equal to the minimum end time in the heap. If it is, we remove the minimum end time from the heap. We then add the end time of the current interval to the heap. The size of the heap at the end of this process is the minimum number of conference rooms required.
    '''
    if not intervals:
        return 0

    # sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # initialize the min heap with the first end time
    heap = [intervals[0][1]]

    # iterate over the rest of the intervals
    for i in range(1, len(intervals)):
        # if the current interval start time is greater than or equal to the
        # minimum end time in the heap, remove it from the heap
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        # add the current interval end time to the heap
        heapq.heappush(heap, intervals[i][1])

    # the size of the heap is the minimum number of conference rooms required
    return len(heap)

# Example 1
intervals1 = [[0, 30],[5, 10],[15, 20]]
print(minMeetingRoomsHeap(intervals1)) # Output: 2

# Example 2
intervals2 = [[7,10],[2,4]]
print(minMeetingRoomsHeap(intervals2)) # Output: 1

def minMeetingRoomsArray(intervals):
    '''
In this approach, we first extract the start and end times of all the intervals and sort them separately. Then we initialize two pointers, i and j, to traverse the start and end times, respectively. We also initialize a variable num_rooms to keep track of the minimum number of conference rooms required.

We then iterate over both start and end times simultaneously. If the current start time is greater than or equal to the current end time, it means a conference room is freed up, so we decrement num_rooms and increment j to move to the next end time. Otherwise, we increment num_rooms and move to the next start time by incrementing i.

Finally, we return num_rooms, which will contain the minimum number of conference rooms required to accommodate all the meetings.
    '''
    start_times = sorted([interval[0] for interval in intervals])
    end_times = sorted([interval[1] for interval in intervals])
    n = len(intervals)
    i, j = 0, 0
    num_rooms = 0
    while i < n and j < n:
        if start_times[i] >= end_times[j]:
            num_rooms -= 1
            j += 1
        num_rooms += 1
        i += 1
    return num_rooms


def minMeetingRooms(intervals):
    '''
        In this method, we first sort the intervals by their start times. We then initialize an array occupied_rooms to keep track of the occupied rooms at any given time. We then iterate through each interval and check if there is any room that will be free by the current meeting. If we find such a room, we update the end time of that room to the end time of the current meeting. If all rooms are occupied, we add a new room. Finally, we return the length of the occupied_rooms array, which gives us the minimum number of required rooms.
    '''
    if not intervals:
        return 0

    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])

    # Initialize an array to keep track of occupied rooms
    occupied_rooms = [intervals[0][1]]

    for i in range(1, len(intervals)):
        start_time = intervals[i][0]
        end_time = intervals[i][1]

        # Check if there is any room that will be free by the current meeting
        for j in range(len(occupied_rooms)):
            if occupied_rooms[j] <= start_time:
                occupied_rooms[j] = end_time
                break
        else:
            # If all rooms are occupied, a new room is required
            occupied_rooms.append(end_time)

    # The length of the occupied_rooms array gives the minimum number of required rooms
    return len(occupied_rooms)
