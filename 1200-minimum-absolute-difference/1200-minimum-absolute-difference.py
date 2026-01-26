class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        n=len(arr)
        if n< 3: return arr
        arr.sort()
        lst=[[arr[0],arr[1]]]
        minnu= arr[1]-arr[0]
        for i in range(2,n):
            d= abs(arr[i]-arr[i-1])
            if d== minnu:
                lst.append([arr[i-1],arr[i]])
            elif d< minnu:
                minnu=d
                lst=[[arr[i-1],arr[i]]]
        return lst