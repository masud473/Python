questions = [
    "1. What is the theoretical temperature at which molecular motion stops?\n1) 100 K\n2) 273 K\n3) 0 K\n4) 373 K",
    "2. Which element is known as the 'building block of life'?\n1) Hydrogen\n2) Oxygen\n3) Carbon\n4) Nitrogen",
    "3. What force keeps us grounded on Earth?\n1) Electromagnetism\n2) Gravity\n3) Weak nuclear force\n4) Strong nuclear force",
    "4. How long does light from the Sun take to reach Earth?\n1) 8 hours\n2) 8 seconds\n3) 8 minutes\n4) 8 days",
    "5. What is the powerhouse of the cell?\n1) Ribosome\n2) Mitochondria\n3) Nucleus\n4) Endoplasmic reticulum",
    "6. Which planet is known as the 'Red Planet'?\n1) Saturn\n2) Mars\n3) Jupiter\n4) Venus",
    "7. What is the most abundant gas in Earth's atmosphere?\n1) Carbon dioxide\n2) Nitrogen\n3) Oxygen\n4) Argon",
    "8. Who proposed the theory of relativity?\n1) Niels Bohr\n2) Stephen Hawking\n3) Albert Einstein\n4) Isaac Newton",
    "9. What is the chemical formula for table salt?\n1) C12H22O11\n2) NaCl\n3) CO2\n4) H2O",
    "10. What phenomenon causes a mirage?\n1) Interference\n2) Refraction\n3) Reflection\n4) Diffraction",
    "11. What is the hardest natural substance on Earth?\n1) Topaz\n2) Quartz\n3) Granite\n4) Diamond",
    "12. What is the term for a solid turning directly into a gas?\n1) Condensation\n2) Vaporization\n3) Sublimation\n4) Deposition",
    "13. What type of galaxy is the Milky Way?\n1) Irregular\n2) Spiral\n3) Lenticular\n4) Elliptical",
    "14. What is the main gas found in the sun?\n1) Methane\n2) Hydrogen\n3) Neon\n4) Helium",
    "15. What is the pH level of pure water?\n1) 11\n2) 7\n3) 9\n4) 5",
]
a = []
b = [3, 3, 2, 3, 2, 2, 2, 3, 4, 2, 4, 3, 2, 1, 1]
levels = [
    0,
    1000,
    2000,
    3000,
    5000,
    10000,
    20000,
    40000,
    80000,
    160000,
    320000,
    640000,
    700000,
    800000,
    900000,
    1000000,
]

for i in range(0, len(questions)):
    print(f"For Rs.{levels[i+1]} your question is:")
    print(questions[i])
    l = 0
    l = int(input())
    a.append(l)
    if a[i] == b[i]:
        print(f"Congratulations! You have won Rs.{levels[i+1]}\n")
    else:
        print(f"Wrong answer! you have won Rs.{levels[i]}")
        break
    if i == 14:
        print("Congratulations! You are now a crorepati")
    