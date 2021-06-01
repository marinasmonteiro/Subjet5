def converter(Mbq):
    if (Mbq)<0:
        print("any value negative are allowed - You had write a mistake...")
    msg_1 = " Mbq is "
    msg_2 = " mci."
    result = (Mbq/37)
    return str(Mbq)+msg_1+str(result)+msg_2

#print(converter(1))
#with reusability and add a input function....

chose=input("emter the value in Mbq:")
Mbq_mCi=converter(float(chose))

if float (chose)>1000:
    print("Are you sure? Radiocativite danger!!!!!")
print((Mbq_mCi))