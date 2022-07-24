def first_three(str):
    return str[:3] if len(str) > 3 else str

print(first_three('ipy'))
print(first_three('python'))
print(first_three('py'))