import requests

APPLICATION_ID = "144bad81"
API_KEY = "52cbe126915a348137b6afadd581848e"

exercise_post_url = "https://trackapi.nutritionix.com/v2/natural/exercise"

def get_headers():

    headers = {
        "x-app-id": APPLICATION_ID,
        "x-app-key": API_KEY,
        "x-remote-user-id": "0"
    }
    return headers

def exercise_post(post_url):

    user_exercise = input("Write witch exercise you did: ")

    workout_exercise = {

        "query": user_exercise
    }

    make_post = requests.post(url=post_url, json=workout_exercise, headers=get_headers())

    return make_post

print(exercise_post(post_url=exercise_post_url).text)