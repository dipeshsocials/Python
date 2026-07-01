age = int(input("Age: "))
has_license = input("License (yes/no): ")

if age >= 18:
    if has_license.lower() == "yes":
        print("You can drive.")
    else:
        print("Get a license first.")
else:
    print("Too young.")

