text = "Hello, Python!"
print(text)
print(text.upper())
print(text.lower())
print(text.replace("Python", "World"))
print(text.split(","))

print(len(text))
print("Python" in text)
print(text.find("Python"))

for char in text:
    print(char)

words = text.split()
print(words)
print(" ".join(words))

text2 = "   spaces   "
print(text2.strip())
print(text2.lstrip())
print(text2.rstrip())

text3 = "python"
print(text3.capitalize())
print(text3.title())

text4 = "123"
print(text4.isdigit())
print(text4.isalpha())
print(text4.isalnum()) 