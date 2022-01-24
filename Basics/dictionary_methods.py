



demo_dict2={"qa":"testurl", "uat":"uaturl","preprod":"preprodurl"}
# get() returns the value for speifeid key in the dictionary
print(demo_dict2.get("preprod"))

# keys() Returns a copy of dictionary keys
print(demo_dict2.keys())

# items() returns a copy dictionaries key value pair
print(demo_dict2.items())

# values() returns a copy of the calues in the dictionary
print(demo_dict2.values())

# pop() removes the arbituary key:value pair
print(demo_dict2.pop("uat"))

# update() adds the specified key-value pairs to dictionary
demo_dict2.update({"prod":"produrl"})
# copy() returns a copy of the dictionary
demo_copy=demo_dict2.copy()
print(demo_dict2)
print(demo_copy)
# clear() removes all the elements form the dictionary
demo_copy.clear()
print(demo_copy)