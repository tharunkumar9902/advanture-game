name=input("enter your name:")
print("welcome",name, "to this adventure!")
answer=input("you are in dirti road, it as come to an end and you can go left or right.which way would you like to go? ").lower()
if answer=="left":
    answer=input("you come to a river you can walk around it or swim accross? type walk to walk around and swim to swim accross: ").lower()
    if answer=="swim":
        print("you swim acrross and were eaten by alligator.")
    elif answer=="walk":
        print("you walked for many miles,ran out of water you lost the game.")
    else:
        print("Not a valid option.you lose")
elif answer=="right":
    answer=input("you come to a bridge,it looks wobbly,do you want to cross it or head back(cross/back)? ")
    if answer=="back":
        print("you go back and lose.")
    elif answer=="cross":
        answer=input("you cross the bridge andmeet a stranger.do you talk to them(yes/on)? ").lower()
        if answer=="yes":
            print("you talk to the stranger they give you gold you win.")
        elif answer=="no":
            print("you ignore the strange they offended you lose.")
        else:
            print("Not a valid option.you lose.")
    else:
        print("Not a valid option.you lose.")
else:
    print("Not a valid option.you lose.")
print("thank you for trying",name)