import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3

def time_add(time1:data.Time, time2:data.Time) -> data.Time: #sums 2 times
    seconds = time1.second + time2.second
    minutes = time1.minute + time2.minute
    hours = time1.hour + time2.hour
    while seconds >= 60:
        seconds -= 60
        minutes +=1
    while minutes >= 60:
        minutes -=60
        hours +=1
    return data.Time(hours, minutes, seconds)

# Part 4

def is_descending(num_list:list[float], previous = float("inf")) -> bool: #checks if a list of numbers is in descending order
    if not num_list: #if num_list = []
        return True
    if num_list[0] >= previous:
        return False
    return is_descending(num_list[1:], num_list[0])

def is_descending_short(num_list:list[float]) -> bool: #concise version of above function
    return reversed(sorted(num_list)) == num_list

# Part 5

def largest_between(nums:list[int], lower:int, upper:int): #returns index of largest value between 2 indexes in a list
    if lower > upper or upper > len(nums) + 1 or lower < 0:
        return None
    nums_in_range = nums[lower:upper + 1]
    largest = max(nums_in_range)
    for i in range(len(nums_in_range)):
        if nums_in_range[i] == largest:
            return i + lower
    #or return nums.index(largest, lower, upper + 1)

# Part 6

def furthest_from_origin(points:list[data.Point]): #returns index of furthest point from origin from list of points
    if not points: #if points = []
        return None

    def distance(point_1: data.Point, point_2: data.Point) -> float:  # returns distance btwn 2 points
        return (((point_2.x - point_1.x) ** 2) + ((point_2.y - point_1.y) ** 2)) ** 0.5

    origin = data.Point(0, 0)
    distances = [distance(origin, point) for point in points]
    furthest = max(distances)
    for i in range(len(distances)):
        if distances[i] == furthest:
            return i
