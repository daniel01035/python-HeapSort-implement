#  best case = N log N  ||  average case = N log N  ||  worst case = N log N
import time
start = time.time()


def MaxHeapify(arr, root, length):
    # 這邊宣告的都是直接使用原本的索引值(0,1,2,3,4,5,6...)
    left = 2 * root + 1      # 取得left child
    right = 2 * root + 2     # 取得right child
    largest = root           # largest用來記錄包含root與child, 三者之中Key最大的node

    if left < length and arr[left] > arr[root]:       # 如果左節點大於root, 最大的紀錄為左節點
        largest = left

    if right < length and arr[right] > arr[largest]:  # 如果右節點大於最大節點, 最大的紀錄為右節點
        largest = right

    if largest != root:                                      # 如果目前root的Key不是三者中的最大
        arr[largest], arr[root] = arr[root], arr[largest]    # 就調換root與三者中Key最大的node之位置
        MaxHeapify(arr, largest, length)                     # 調整新的subtree成Max Heap


def HeapSort(arr):
    n = len(arr)
    for i in range(n//2, -1, -1):       # 將array調整成Max Heap, 因為只有判斷父節點, 所以做陣列長度一半就好
        MaxHeapify(arr, i, n - 1)

    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]    # 將最大值與array的最後一個位置做交換
        MaxHeapify(arr, 0, i)              # 調整「忽略最後一個位置」的矩陣, 所以一直-1
    return arr


array = [9, 1, 10, 4, 2, 3, 7, 6, 8, 5]
print(HeapSort(array))