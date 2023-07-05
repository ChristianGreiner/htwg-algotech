import sys
 
def maxCrossingSubarray(nums, left, mid, right):
        leftSum = -sys.maxsize
        total = 0
        for i in range(mid, left - 1, -1):
            total += nums[i]
            if total > leftSum:
                leftSum = total
     
        rightSum = -sys.maxsize
        total = 0
        for i in range(mid + 1, right + 1):
            total += nums[i]
            if total > rightSum:
                rightSum = total
     
        # gibt die Summe der linken und rechten Teilsumme zurück
        return leftSum + rightSum

# Funktion zum Ermitteln der maximalen Teillistensumme mittels Teile-und-Herrsche
def findMaxSum(nums, left=None, right=None):
 
    # Basisgehäuse
    if not nums:
        return 0
 
    if left is None and right is None:
        left, right = 0, len(nums) - 1
 
    # Wenn die Liste 0 oder 1 Element enthält
    if right == left:
        return nums[left]
 
    # Finden Sie das mittlere Element in der Liste
    mid = (left + right) // 2
 
    maxCrossing = maxCrossingSubarray(nums, left, mid, right)
 
    # Finden Sie rekursiv die maximale Unterlistensumme für die linke Seite
    # und rechte Unterliste und maximal nehmen
    maxLeftRight = max(findMaxSum(nums, left, mid), findMaxSum(nums, mid + 1, right))
 
    # gibt das Maximum der drei zurück
    return max(maxLeftRight, maxCrossing)
 
 
if __name__ == '__main__':
 
    nums = [1, -2, -3, 1]
    print('The Maximum sum of the sublist is', findMaxSum(nums))