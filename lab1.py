
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if len(int_list) < 1:
      return None
   max = 0
   for i in range(len(int_list)-1):
      if int_list[i+1] > int_list[max]:
         max = i+1
   return int_list[max]
print(max_list_iter(int_list= [1,5,8,9,11,12,2,3]))

def reverse_rec(int_list,spot=0):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
  
   if int_list is None:
      raise ValueError
   elif spot == len(int_list):
      return int_list
   else:
      last = int_list[-1]  # get last item of list
      int_list = int_list[:-1]  # cutoff last digit
      int_list.insert(spot,last)   # STEP 2 insert this in front

      return reverse_rec(int_list, spot + 1)   # check if condition met

print(reverse_rec(int_list=[1,2,3,4,5]))
def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list is None:
      raise ValueError

   elif low <= high:
      mid_point = low + ((high - low) // 2)
      if int_list[mid_point] == target:
         return mid_point

      if target > int_list[mid_point]:  # HIGH
         low =  mid_point + 1
         return bin_search(target, low, high, int_list)

      else:  # LOW
         high =  mid_point - 1
         return bin_search(target, low, high, int_list)

   return None
print(bin_search(target=2,low=0,high=9,int_list=[1,2,3,4,5,6,7,8,9,10]))
