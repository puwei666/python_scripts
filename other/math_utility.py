
# 返回x * y
def multiply (x, y):
    return x * y

# 接受list，求积
def prod (nums):
    return reduce(multiply, nums)


nums = [1, 2, 3, 4, 5]

pnums = prod(nums)

print pnums

