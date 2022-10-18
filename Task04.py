from Task03 import calc_dragon_head

def main():
    age = int(input("Input dragon's age : "))

    head = calc_dragon_head(age)

    msg = f"Dragon with {age} years has {head} heads"

    print(msg)

main()