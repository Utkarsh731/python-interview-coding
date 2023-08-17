# Check if any 2 elements in the array sum to the given sum

def check_pair(arr, total):
    output = []  # Initialize empty list to store pairs
    seen = set()  # Initialize an empty set to store elements

    for num in arr:
        if total - num in seen:  # Check if complement of current element is in seen
            pair = (num, total-num)  # Create a tuple of current element and its complement
            output.append(pair)  # Append the tuple to output
        seen.add(num)  # Add current element to seen

    return output

print(check_pair([1, 4, 45, 6, 10, 8], 16))  # [(6, 10)]
print(check_pair([0, -1, 2, -3, 1], -2))  # [(-3, 1)]

```
#[1, 4, 45, 6, 10, 8], 16
def check_pair(array, total):
    pairs = []
    array.sort()
    for i in range(0,len(array)-1):
        for j in range(i+1, len(array)):
            if array[i]+array[j] == total:
                pair = (array[i], array[j])
                pairs.append(pair)
            elif array[i]+array[j]>total:
                break
    return pairs
print(check_pair([0, -1, 2, -3, 1], -2))
                
                
```
