# list with 4 indexes
a = ["a", "b", "c", "d"]

# exclusive slice reassignment ( I can)
a[1:4] = ["d, e, f, g"]

# result
print(a)

a = {"a":0, "b": 1}
a.add('c', 2)