# Task 1

import copy # imports the function copy for shallow copy

set1 = set({1, 2, 3, 4, 5});  # set1
set2 = set({4, 5, 6, 7, 8});  # set2

# Length of the sets
print('Length of set1 is: ', len(set1));
print('Length of set2 is: ', len(set2));

# Union
set3 = set1.union(set2);
print('Union is: ', set3);

# Intersection
set4 = set1.intersection(set2);
print('Intersection is: ', set4);

# Difference
set5 = set1.difference(set2);
print('Difference is: ', set5);

set6 = set2.difference(set1);
print('Difference is: ', set6);

# Disjoint
set7 = set1.isdisjoint(set2);
print('Disjoint is: ', set7);

# Maximum element in a set in a function
def max_Num(set):
  return max(set);

print("Maximum number in set is: ", max_Num(set1));
print("Maximum number in set is: ", max_Num(set2));

# Minimum number in a set in a function
def min_Num(set):
  return min(set);

print("Minimum number in set is: ", min_Num(set1));
print("Minimum number in set is: ", min_Num(set2));

# Shallow copy of a set
set8 = set1.copy();
print("Shallow copy of set1 is: ", set8);

# Subset
set9 = set1.issubset(set2);
print("Is subset: ", set9);

# Remove elements
set10 = set({4, 0, 2, 8, 9});
set11 = set10.clear();
print("Cleared set is: ", set11);

# Comparing if two sets have nothing in common
set12 = set({1, 3, 5, 7, 9});
set13 = set({2, 4, 6, 8, 0});
set14 = set12.isdisjoint(set13);
print('Disjoint is: ', set14);

# Checing if a set is a superset
set15 = set1.issuperset(set2);
print("Is superset: ", set15);

set16 = set({2, 3, 4, 5});
set17 = set1.issuperset(set16);
print('Is superset: ', set17);
