# Based on this tutorial: https://www.youtube.com/watch?v=s6FhG--P7z0

def canPartition(nums):
    total_sum = sum(nums)
    if total_sum % 2 != 0:
        return False

    target = total_sum // 2

    p = [[False for i in range(target + 1)] for j in range(len(nums))]

        # Fill first column with True

    for i in range(len(nums)):
        p[i][0] = True

        for j in range(1, target + 1):
            if nums[i] > j:
                if i == 0:
                    p[i][j] = False
                else:
                    p[i][j] = p[i - 1][j]
            elif nums[i] == j:
                p[i][j] = True
            elif nums[i] < j:
                if i == 0:
                    p[i][j] = False
                else:
                    p[i][j] = p[i - 1][j - nums[i]] or p[i - 1][j]

            if p[i][target]:
                return True

    return False

print(canPartition([3, 7, 5, 1]))