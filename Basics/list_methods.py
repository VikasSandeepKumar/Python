#list.append(x)
#list.insert(i,x)
#list.remove(x)
#list.pop([i])
#list.clear()
#list.index(x[, start[, end]])
#list.count(x)
#list.sort(*, key=None, reverse=False)
#list.reverse()
#list.copy()

cities=["Delhi","hyderabad","Mumbai","Chennai"]
print(cities)
cities.append("Lucknow")
cities.insert(2,"mysore")
#cities.remove("Mumbai")
cities.pop(3)
#print(cities.index("Chennai"))
print(cities.count("Mumbai"))
cities.sort()
print(cities)
cities.reverse()
new_cities=cities.copy()
print(cities)
print(new_cities)
updatedlist=new_cities.clear()
print(updatedlist)
