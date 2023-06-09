# Пузырьковый метод сортировки

lst = [100, 25, 1, 3, 30, 2, 6, 4, 8, 5]

for i in range(len(lst)-1):
    for j in range(len(lst)-i-1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print(lst)

# Бинарный поиск. Только для сортированного списка
lst_ = lst
to_find = int(input())

mid = len(lst) // 2
min_ = 0
max_ = len(lst) - 1
count = 0

while to_find != lst_[mid] and min_ <= max_:
    if to_find > lst_[mid]:
        min_ = mid + 1
    else:
        max_ = mid - 1

    mid = (max_ + min_) // 2
    count += 1

if min_ > max_:
    print(f"{to_find} Not found")
else:
    print(f"ID = {mid}", count)

# Линейный поиск
count_ = 0
for i in range(len(lst_) - 1):
    if to_find == lst_[i]:
        print(f"ID = {i}", end = " ")
        break
    count_ += 1
print(count_)