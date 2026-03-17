def signup_member(**kwargs):
    print("type is ",type(kwargs))
    print(kwargs)
    for key in kwargs:
        print(kwargs[key])
signup_member(name="Ban Ban",age=17,gander="Male")
