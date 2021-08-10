import random
import time
from concurrent.futures import ThreadPoolExecutor

sort_list = []# からのソート用のリストを作成する
for i in range(1000000):# ソートする配列の数
    random_number = random.randint(0,1000000)
    sort_list += [random_number]

# マージソート
def merge_sort(nums):
    if len(nums) <= 1:
        return nums

    split = len(nums) // 2
    left = nums[:split]
    right = nums[split:]

    left = merge_sort(left)
    right = merge_sort(right)

    i, j, k= 0, 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1

    return nums

start = time.time()
merge_sort(sort_list)# マージソートの実行
print(time.time()-start)# 逐次処理時間を表示

start = time.time()
with ThreadPoolExecutor(max_workers=6) as e:# 並列処理を実行
    e.submit(merge_sort(sort_list))    
print (time.time()-start)
