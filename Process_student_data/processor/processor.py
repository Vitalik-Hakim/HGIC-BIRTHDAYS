import json
import re



with open('../Months/December.txt', 'r') as file:
    names = file.readlines()
    names = map(lambda s: s.strip(), names)


for name in names:



    with open('../Data/BASE.json') as d:
        userdata = json.load(d)
        # name  = "Kojo"

        #Day definition
        birthday_number = re.findall("\d+", name)
        print(birthday_number)
        birthday_number_day = birthday_number[0]
        print(int(birthday_number[0]))
        name = ' '.join(name.split())
        new_userdata = {name: userdata}
        # Serializing json
        new_userdata[name][0]['Day'] = birthday_number_day
        user_data = json.dumps(new_userdata, indent=4)

    # Write this new name and replace an old one
    with open('../Data/single_user.json', 'w') as outfile:

        outfile.write(user_data)

    with open("../Data/single_user.json", "r") as json_file:

        Full_user_data = json.load(json_file)
        # spartan['ABDUL MUBARIK MOHAMMED'] = NAME
        # spartan['ABDUL MUBARIK MOHAMMED'][0]['lateness'] = LATENESS
        # spartan['ABDUL MUBARIK MOHAMMED'][0]['hostel'] = HOSTEL
        # spartan['ABDUL MUBARIK MOHAMMED'][0]['streak'] = STREAK



    with open('../Data/December.json', 'r+') as file:
        data = json.load(file)
        data['December'].update(Full_user_data)
        # data['SPARTANS'][name][0]['0'] = year

        file.seek(0)
        json.dump(data, file, indent=4)
