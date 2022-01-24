# Used to iterate over the sequence like list, string, dictionary, set or tuples
# less like the for loop in other programming language

cities = [["India","Delhi"],["Australia","Melbourne"],["Uttar Pradesh","Lucknow"],["Canada","Toronto"]]
# for country,city in cities:
#     print("country is " +country+ " and city is " +city)

my_dictionary=dict(cities)
print(my_dictionary)
for country, city in my_dictionary.items():
    print(country, city)
    for s in country:
        print(s)

# cities = {"Delhi","New York"}
# for city in cities:
#     print(city)