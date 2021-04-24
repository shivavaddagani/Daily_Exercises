# =================== Problem 1 ======================
# first last #
def firstlast(x):
    y = [x[0], x[-1]]
    return y
print(firstlast('abc'))
print(firstlast([1,2,3,4]))

# the above code does needs to defines in such a way that output of a string abc will be ac
def firstlast2(x):
    y = x[:1] + x[-1:]      # tried y = x[0] + x[-1] but it did not work. recollect why?
    return y
print(firstlast2('abc'))
print(firstlast2([1,2,3,4]))