def merge(left,right):
    result=[]
    n=len(left)
    m=len(right)
    i,j=0,0
    while i<n and j<m:
        if left[i]<right[j]:
            result.append(left[i])
            i+=1
        else :
            result.append(right[j])
            j+=1
     
        while i<n:
                result.append(left[i])
                i+=1
        
        while j<m:
                result.append(right[j])
                j+= 1
        return result
def merge_sort(arr):
    if len(arr)<=1:
        return arr

    mid=len(arr)//2
    left_side=arr[:mid]
    rigth_side=arr[mid:]  
    left_side=merge_sort(left_side)
    right_side=merge_sort(rigth_side)
    return merge(left_side,right_side)
arr=[1,5,7,1,4,6,6,8]
print(merge_sort(arr))






    
        

