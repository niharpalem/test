import sys

def get_values():
    # Accept values from command-line: python test.py NAME PLACE ANIMAL THING
    if len(sys.argv) >= 5:
        _, name, place, animal, thing, *rest = sys.argv
        return name, place, animal, thing
    # Otherwise prompt the user
    name = input("Name: ").strip()
    place = input("Place: ").strip()
    animal = input("Animal: ").strip()
    thing = input("Thing: ").strip()
    return name, place, animal, thing

def main():
    name, place, animal, thing = get_values()
    print(f"Name : {name}")
    print(f"Place: {place}")
    print(f"Animal: {animal}")
    print(f"Thing : {thing}")

if __name__ == "__main__":
    main()