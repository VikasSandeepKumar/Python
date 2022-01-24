#add(elem) - Add element elem to the set.
#remove(elem) - Remove element elem from the set
#discard(elem) - Remove elem from set if it is present
#pop() - remove and return an arbitary element from the set
#clear() remove all elements from the set
#joining two sets
#union()
#update()
#keep only duplicates
#intersection()
#intersection_update()
#keep all excluding duplicates
#symmetric_differences()
#symmetric_difference_update()
#return set containg
#difference()
#difference_update()
#issubset()
#issuperset()

demo_set1={"delhi","kolkata","hyderabad","mumbai"}
demo_set2={"delhi","kolkata","hyderabad","mumbai","newyork","london","china"}



#print(demo_set1)
demo_set1.add("Gold coast")
#print(demo_set1)
demo_set1.remove("delhi")
#print(demo_set1)
demo_set1.discard("delhi")
#print(demo_set1)
demo_set1.pop()
#print(demo_set1)

demo_set3=demo_set1.union(demo_set2)
#print(demo_set3)

demo_set4=demo_set1.update(demo_set2)
#print(demo_set4)

demo_set3=demo_set1.intersection(demo_set2)
#print(demo_set3)

demo_set3=demo_set1.intersection_update(demo_set2)
#print(demo_set3)

demo_set3 = demo_set1.symmetric_difference(demo_set1)
print(demo_set3)
demo_set2.difference_update(demo_set1)
print(demo_set2)

