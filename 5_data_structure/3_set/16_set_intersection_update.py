s1 = {"a","b","c"}
s2 = {"d","e","a"}
s3 = {"g","h","a"}
r = s1.intersection_update(s2,s3)# not return new set
print(s1)
print(r)
# The intersection_update() method is different from the intersection() method,
# because the intersection() method returns a new set, without the unwanted items,
#  and the intersection_update() method removes the unwanted items from the original set.