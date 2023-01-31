# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        l = 0
        r = reader.length() - 1
        # [7,7,7,7,10,7,7,7]
        # [6,6,12]
        while l < r:
            mid = (l+r)//2
            # print(l, mid, r)
            
            if (r - l + 1) % 2 == 0:
                result = reader.compareSub(l, mid, mid+1, r)
                
                if result == 1:
                    r = mid
                elif result == -1:
                    l = mid+1
                else: # == 0
                    # Should not happend?
                    print("Hi")
                    
                    if mid - l + 1 > r - mid:
                        l = mid+1
                    else:
                        r = mid
            else:
                result = reader.compareSub(l, mid, mid, r)
                
                if result == 1:
                    r = mid-1
                elif result == -1:
                    l = mid+1
                else: # == 0
                    return mid
            
                
        return l