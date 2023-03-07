for i in range(0,100):
    if i < 10:
        print(f"0{i:d},", end=" ")
    elif i >= 10 and i != 99:
        print(f"{i:d},", end=" ")
    else:
        print(f"{i:d}")
