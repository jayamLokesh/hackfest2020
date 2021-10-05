a = int(input())
arr = list(input().split())
arr = list(map(int, arr)) 
len_of_arr = len(arr)
mean = sum(arr)/len(arr)
print(mean)

#adding it just for the name sake of the t shirt

arr_med = sorted(arr)
len_of_arr_med = len(arr_med)
if len_of_arr_med%2 ==0:
    index  = len_of_arr_med//2
    median = (arr_med[index] + arr_med[index-1] )/2
else :
    index = len_of_arr_med//3
    median = arr_med[index+1]

print(median)    

arr_count = {}

for i in arr:
    if i in arr_count:
        arr_count[i] +=1 
    else:
        arr_count[i] = 1 
        
#for i , j in arr_count.items():
   # print(str(i) +  "-->" +  str(j))

mode = 0
for i in arr_count:
    if arr_count[i] > mode:
        mode = i
    else :
        mode = mode
        
max_value = max(list(arr_count.values()))
mode_val = [num for num, freq in arr_count.items() if freq == max_value]
#print(mode_val)
        
#if arr_count.values() == 1:
   # print("True")
    #mode = min(arr_count)
    #print(mode)
    
#print(mode)
if len(mode_val) == len(arr):
   #print("No mode in the list")
   print(min(arr))
else:
    print(mode_val)
