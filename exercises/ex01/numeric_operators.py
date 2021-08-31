"""Numeric Operators Exercise."""

left_hand: str = (input("What is the left-hand side?"))
right_hand: str = (input("What is the right-hand side?"))
print("Left-hand side = " + left_hand)
print("Right-hand side = " + right_hand)
x: int = int(left_hand)
y: int = int(right_hand)
z: str = " ** "
a: str = " is "
print(left_hand + z + right_hand + a + str(int(left_hand) ** int(right_hand)))
b: str = " / "
print(left_hand + b + right_hand + a + str(int(left_hand) / int(right_hand)))
c: str = " // "
print(left_hand + c + right_hand + a + str(int(left_hand) // int(right_hand)))
d: str = " % "
print(left_hand + d + right_hand + a + str(int(left_hand) % int(right_hand)))
_author_: str = "730402819"