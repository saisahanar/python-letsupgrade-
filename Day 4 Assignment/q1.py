s = "what we think we become; we are Python programmer"
tofind = input("enter substring to be found in the string:")
i = s.find(tofind)
if i == -1:
    print(f"the given substring {tofind} is not present in the string")
while i != -1:
    print(f"{tofind}--->{i}th index")
    i = s.find(tofind, i + len(tofind))





