"""Relational Operators Exericse"""

left_hand: str = input("What is the left-hand side?")
right_hand: str = input("What is the right-hand side?")
print("Left-hand side = " + left_hand)
print("Right-hand side = " + right_hand)
a: str = " is "
b: str = " < "
print(left_hand + b + right_hand + a + str(int(left_hand) < int(right_hand)))
c: str = " >= "
print(left_hand + c + right_hand + a + str(int(left_hand) >= int(right_hand)))
d: str = " == "
print(left_hand + d + right_hand + a + str(int(left_hand) == int(right_hand)))
e: str = " != "
print(left_hand + e + right_hand + a + str(int(left_hand) != int(right_hand)))
_author_: str = "730402819"