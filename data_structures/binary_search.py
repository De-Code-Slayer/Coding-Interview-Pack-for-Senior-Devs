# In binary search, the idea is to find an Item in a list of length n, where n can be finite for example
# a list of length 10: to find an item in this list with Iteration might take a max of 10 iterations
# but with binary search you can do this in lesser time and maybe without iterations


def example1(lst,find_item):
  print("BINARY SEARCH .........")

  n = 0 
#   initialize the begining and end of the list outside our loop
  begining = 0 
  ending = len(lst) - 1 

  while n <= len(lst):
    n += 1
    print(n)

    # here I want to first sort the list in ascending order
    copy_lst = lst.copy()
    copy_lst.sort()

    # we want to divide the list in the middle
    middle = (ending + begining) // 2
    

    # now we want to check if the middle item is lesser or greater than the item we are searching for or if it is the Item
    # if the middle item is the item we are trying to find viola then we just return it
    if copy_lst[middle] == find_item:
        item = copy_lst[middle]
        return f"the item is in the position {copy_lst.index(item)}"  


    # if the middle item is greater than the item we are tring to find  
    # we want to look at the items to the left of it only and repeat the process
    # we can acheive this by chenging our starting and ending positions
    # we can also delete all the items on the right since we are only using a copy of theand it wont affect our index value
    # however we won't do this 
    
    elif copy_lst[middle] > find_item:
         ending = (middle-1)
        

    # if the middle item is lesser than the item we are tring to find
    # we can do the opposite of what we did before
    elif copy_lst[middle] < find_item:
        begining = (middle+1)
        


    if n > len(copy_lst)-1:
        return"not found"
        
        



lst = [1,7,8,98,10,441,3252,88,4588]
item = 4588
print(example1(lst,item))

