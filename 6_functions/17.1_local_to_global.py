def outer():
    name = "Ban Ban"
    def inner():
        nonlocal name
        name = "Aung Aung"
    inner()
    return name    
print(outer())