import datetime


def gather_profile_response(name, age, colour):
        if name == '' or name is None:
            return {
                'status': 'error',
                'message': 'Invalid name must be provided',
            }
        if age <= 0 or age > 100:
            return {
                'status': 'error',
                'message': 'Invalid age must be between 1 and 100',
            }
        if colour == '' or colour is None:
            return {
                'status': 'error',
                'message': 'Invalid colour must be provided',
            }


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

print(gather_profile_response('', 10, 'blue'))




