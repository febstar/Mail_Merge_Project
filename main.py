PLACEHOLDER = "[name]"

with open("../../Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()

with open("../../Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt") as f:
    x = f.read()
    for i in names:
        w= i.strip()
        newletter = x.replace(PLACEHOLDER, w)
        with open(f"./Output/ReadyToSend/letter_for_{w}.txt",mode="w") as complete_letter:
            complete_letter.write(newletter)

