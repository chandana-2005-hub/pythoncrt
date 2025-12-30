def insertion_sort(arr):
    for i in range(1,len(arr)):
        start=arr[i]
    j=i-1
    while j>=0 and start<arr[j]:
        arr[j+1]=arr[j]
        j-=1
        arr[j+1]=start
arr=[1,4,6,0]
insertion_sort(arr)
print("sorted array:",arr)