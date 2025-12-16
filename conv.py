import os

os.system("cls")
print("Welcome to the converter!")
print("You can convert between different units.")
conv_type = input("Enter the type of conversion (cm/km/m): ")
if conv_type == "cm":
    cm_value = float(input("Enter value in centimeters: "))
    km_value = cm_value / 100000
    m_value = cm_value / 100
    cm_value = int(cm_value)
    km_value = int(km_value)
    m_value = int(m_value)
    mm_value = m_value * 1000
    print("The value in kilometers is: " + str(km_value) + "km")
    print("The value in meters is: " + str(m_value) + "m")
    print("The value in centimeters is: " + str(cm_value) + "cm")
    print("The value in milimeters is: " + str(mm_value) + "mm")
if conv_type == "km":
    km_value = float(input("Enter value in kilometers: "))
    cm_value = km_value * 100000
    m_value = km_value * 1000
    cm_value = int(cm_value)
    km_value = int(km_value)
    m_value = int(m_value)
    mm_value = m_value * 1000
    print("The value in centimeters is: " + str(cm_value) + "cm")
    print("The value in meters is: " + str(m_value) + "m")
    print("The value in kilometers is: " + str(km_value) + "km")
    print("The value in milimeters is: " + str(mm_value) + "mm")
if conv_type == "m":
    m_value = float(input("Enter value in meters: "))
    cm_value = m_value * 100
    km_value = m_value / 1000
    cm_value = int(cm_value)
    km_value = int(km_value)
    m_value = int(m_value)
    mm_value = m_value * 1000
    print("The value in centimeters is: " + str(cm_value) + "cm")
    print("The value in kilometers is: " + str(km_value) + "km")
    print("The value in meters is: " + str(m_value) + "m")
    print("The value in milimeters is: " + str(mm_value) + "mm")
