num_list1 = list(map(int, input().split()))
num_list2 = list(map(int, input().split()))

def dup_remove(l: list):
  l = set(l)
  l = list(l)
  return l

def merge(l1: list, l2: list):
  result = l1 + l2
  return dup_remove(result)

def dup(l1: list, l2: list):
  result = [item for item in l1 if item in l2]
  return dup_remove(result)

print("합집합 : ", merge(num_list1, num_list2))
print("교집합 : ", dup(num_list1, num_list2))