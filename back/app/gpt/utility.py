
import requests


def get_mobum_data(restaurant_name: str = "", gu: str = ""):
    print(restaurant_name, gu)
    print(len(restaurant_name), len(gu))
    try:
        data = requests.get(f"http://localhost:8001/v1/mobums?name={restaurant_name}&gu={gu}", timeout=40)
        return data.json()
    except requests.exceptions.Timeout as e:
        print("Request Time out")
    except requests.exceptions.RequestException as e:
        print("request error")
    return None # data.json()

def get_restaurant_data(restaurant_name: str = "", gu: str = "", restaurant_type: str = ""):
    print(restaurant_name, gu, restaurant_type)
    print(len(restaurant_name), len(gu), len(restaurant_type))
    try:
        data = requests.get(f"http://localhost:8001/v1/restaurants?name={restaurant_name}&gu={gu}&restaurantType={restaurant_type}", timeout=40)
        return data.json()
    except requests.exceptions.Timeout as e:
        print("Request Time out")
    except requests.exceptions.RequestException as e:
        print("request error")
    return None # data.json()
