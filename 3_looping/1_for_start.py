# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# We got ten integers starting from 0 to 10. If you notice, range() didn't inclube 10 in its result because it generates number up to the stop number but never includes the stop number in its result.

for i in range(21):
    print(i,end=' ')