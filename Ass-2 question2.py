
# Instagram Reel Engagement Tracker

views = int(input("Enter views: "))
likes = int(input("Enter likes: "))
comments = int(input("Enter comments: "))

total = likes + comments
rate = (total / views) * 100

print("Views:", views)
print("Likes:", likes)
print("Comments:", comments)
print("Engagement Rate:", rate, "%")
