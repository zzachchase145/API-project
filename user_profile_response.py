import datetime



def gather_name():
        name = input("What is your name?: ")
        while name == '':
            print("Please enter a valid name.")
            name = input("What is your name?: ")
        return name

def gather_age():
        while True:
            try:
                age = int(input("What is your age?: "))
            except ValueError:
                print("Please enter a valid age.")
            continue

        if age <= 0 or age > 100:
            print("Please enter a valid age.")


def gather_fav_colour():
        fav_colour = input("What is your favorite colour?: ")
        while fav_colour == '':
            print("Please enter a valid favorite colour.")
            fav_colour = input("What is your favorite colour?: ")
        return fav_colour


name = gather_name()
age = gather_age()
colour = gather_fav_colour()


def gather_profile_response():
        person_info = {
            "name": name,
            "age": age,
            "fav_colour": colour,
            'id': 'user 1',
            'created_at': str(datetime.datetime.now())
        }

        response = {
            'status': 'success',
            'data': person_info,

        }

        return response

print(gather_profile_response())




