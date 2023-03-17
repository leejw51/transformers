#!/usr/bin/python3
import json
import urllib.request

# URL of the JSON file
url= "https://s3.amazonaws.com/deep-learning-models/image-models/imagenet_class_index.json"

# Read the JSON data from the URL
with urllib.request.urlopen(url) as url:
    data = json.loads(url.read().decode())

# Extract a value from a specific key
# read the key from the user
my_key=input("Enter the key: ")

my_value = data.get(my_key)

# Print the extracted value
print(f"The value of '{my_key}' is: {my_value}")
