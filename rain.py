rain = float(input("Enter rainfall amount (in mm): "))

if rain < 1:
    print("No rain")
elif rain < 5:
    print("Light rain")
elif rain < 10:
    print("Moderate rain")
else:
    print("Heavy rain")
