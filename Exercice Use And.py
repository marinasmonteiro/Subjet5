
a=input("What weather is there?")
b=input("What temperature is outside?")

if a=="raining" and b=="cold":
    print("take an umbrella and a jacket!")
elif a=="raining" and b=="warm":
    print("take an umbrella and a T-shirt!")
elif a=="sunny" and b=="cold":
    print("take sunglasses and a jacket!")
elif a=="sunny" and b=="warm":
    print("take sunglasses and T-shirt!")
else:
    print("Stay at home!")