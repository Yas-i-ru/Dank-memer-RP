level = input("What is your level? ")
prestige = input("What is your prestige level? ")
status = input("What do you want to show as the status? ")
image = input("What do you want to show as the small image? ")
tooltip = input("What do you want to show as the tooltip? ")

with open ("./data.ini" , "w") as info:
        info.write(
f"""[data]
level = {level}
prestige = {prestige}
status = {status}
image = {image}
tooltip = {tooltip}
""")