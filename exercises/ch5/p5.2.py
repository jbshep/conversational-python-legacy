xs = [1, 3, 5]
ys = xs
xs.append(7)
ys.append(9)
print(xs)
print(ys)
ys = xs[:]
ys.remove(9)
ys.pop(0)
print(xs)
print(ys)
