import sys
import gc

"""Example of garbage collector"""

# lst = [1, 2, 3]
# print(id(lst))
# print(sys.getrefcount(lst))
# lst_ = lst
# # print(id(lst_))
# print(sys.getrefcount(lst))
# del lst_
# print(sys.getrefcount(lst))
# lst.append(lst)
# print(lst[-1] is lst)

def create():
    lst = [1, 2, 3]
    lst.append(lst)

for i in range(10):
    create()

print("Collecting...")
n = gc.collect()
print("Number of unreachable references ", n)
print("Reference left", gc.garbage)
