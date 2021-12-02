src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]

src_gen = (i for i in src)
result = [x for x in src[1:] if x > next(src_gen)]
print(result)
