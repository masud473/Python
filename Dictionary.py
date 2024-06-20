a = {"Name": "Farhan", "Roll": 16}
b={"Name1":"Rahim", 'Roll1':54}
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
"""The line below is a method to print both the key and its value together
in a line.
1.i is set as the key 
2. using an f string the value of i which is a key will be shown
3. a[i]: here i identifies the key and a[i] means the value of that key in a"""

for i in a:
    print(f"Value of Key {i} is {a[i]}")
