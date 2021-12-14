import statistics as st

def a(arr):
    sum=0;
    for x in arr:
        sum=sum+x
    return sum/len(arr)



def disp(arr):
    sum=0
    mean = a(arr)
    for x in arr:
        sum=sum+(x-mean)**2
    return sum/(len(arr)-1)



print(a([4,5,7,4]))
print(st.mean([4,5,7,4]))

print(disp([4,5,7,4]))
print(st.variance([4,5,7,4]))
