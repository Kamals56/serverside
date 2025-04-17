# Exercise 1: Create variables car1 and car2 which contains the following information:
# car1: brand = "Toyota", model = "Corolla", year = 2010
# car2: brand = "BMW", model = "X5", year = 2015
# After that, print the variables

# Solution
car = {
    "car1" : {
        "brand" : "Toyota",
        "model" : "corolla",
        "year" : 2010
    },
    "car2" : {
        "brand" : "BMW",
        "model" : "X5",
        "year" : 2015
    }
}

print(car["car1"], car["car2"])
# Exercise 2: Create a list called cars which contains the variables car1 and car2
# After that, print the list

# Solution
cars = [car["car1"], car["car2"]]
print(cars)

# Exercise 3: Change year of car with name "Toyota" to 2015
# After that, print the list

# Solution
for car in cars:
    if car["brand"] == "Toyota":
        car["year"] = 2016
print(cars)

# Exercise 4:
# First, create a variable domain which contains text "google"
# Create variable urls which is a dictionary which contains names and url addresses.
# It should contain these two mappings:
# google = www.google.com
# samk = www.samk.fi
# Then, check if content of variable domain exists in urls
# If it does, print: "I found this: {url}" replacing {url} with the url
# Otherwise print "Cannot find {domain}"
domain = "google"
urls = {
    "google" : "www.google.com",
    "samk" : "www.samk.fi"
}
if domain in urls:
    print(f"I found this: {urls[domain]}")
else:
    print(f"couldnot find this {domain}")

