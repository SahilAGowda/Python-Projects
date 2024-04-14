#Have a function that take list as a parameter and target variable 
# we will variable such as middle,start end,steps
# we can use Recursion or while Loop 
# increase the steps each time the split is done 

def binary_search(list,element):
    middle=0
    start=0;
    end=len(list)
    steps=0
    while(start<=end):
        print("Step",steps,":",list[start:end+1]) # display the List from start to end 
        steps=steps+1;
        middle=(start+end)//2
        
        if element==list[middle]:
            return middle
        if element < list[middle]: # 1,2,3,4,5 ===>element be 2 so end will 3 and list will be 1,2,3
            end=middle-1
        if element >list[middle]:
            start=middle+1
            
    return -1

my_list=[1,2,3,4,5,6,7,8,9]
target=4
binary_search(my_list,target)