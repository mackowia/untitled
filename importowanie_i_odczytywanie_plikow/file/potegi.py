with open ("nowy.txt", "w") as f:
    for i in range(100):
        f.write(str(2 ** i) + "\n")