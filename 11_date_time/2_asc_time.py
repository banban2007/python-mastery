import time

print(time.localtime(
           time.time()
        )
    )
print(time.asctime(
    time.localtime(
        time.time()
        )
    )
)

# Python time method time.asctime() is used to convert a tuple or a time