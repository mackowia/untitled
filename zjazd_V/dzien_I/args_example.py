import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("imie", help="your name")
    args = parser.parse_args()

    print(args)
    print(f"Witaj {args.imie}")

if __name__ == '__main__':
    main()
