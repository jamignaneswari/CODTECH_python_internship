# TASK 1: API Integration and Data Visualization
# CODTECH Internship
# Public API: JSONPlaceholder
# Python Version: 3.9

import requests
import matplotlib.pyplot as plt

# Fetch data from public API
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
data = response.json()

# Extract first 5 records
post_ids = []
title_lengths = []

for post in data[:5]:
    post_ids.append(post["id"])
    title_lengths.append(len(post["title"]))

# Print output
print("Post IDs:", post_ids)
print("Title Lengths:", title_lengths)

# Visualization
plt.figure(figsize=(8, 5))
plt.bar(post_ids, title_lengths)
plt.xlabel("Post ID")
plt.ylabel("Title Length")
plt.title("Post Title Length Visualization")

plt.savefig("api_visualization.png")
plt.show()
