"""
Даны два списка чисел, которые могут содержать до 100000 чисел каждый. Посчитайте, сколько чисел содержится
одновременно как в первом списке, так и во втором.
"""
nums_list1 = set(map(int, input().split()))
nums_list2 = set(map(int, input().split()))
print(len(nums_list1 & nums_list2))