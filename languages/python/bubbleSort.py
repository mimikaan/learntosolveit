'''Time is a list with numeric value
    we are sorting the list in this code using bubble sort'''
time = [66,57,54,53,64,52,59]
for i in range(len(times)):
    for j in range(len(times)-i-1):
        if times[j] > times[j+1]:
            times[j],times[j+1] = times[j+1],times[j]
print(times)
