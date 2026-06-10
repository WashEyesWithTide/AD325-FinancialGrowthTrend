def trend(arr: list[int]) -> list[int]:
    # O(n log n) time, O(n) extra space
    for i in range(len(arr)):
        arr[i] = arr[i] ** 2
    arr.sort()
    return arr


if __name__ == "__main__":
    print(trend([-4, -1, 0, 3, 10]))
    print(trend([-7, -3, 2, 3, 11]))