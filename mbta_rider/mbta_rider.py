import requests
import util.helper


def mbta_rider():
  """ This function provides predicted departure time for a train based on user input"""
  try:
    # make a GET request to get route types 0 and 1 (light rail and heavy rail)
    response = requests.get('https://api-v3.mbta.com/routes?filter%5Btype%5D=0%2C1')
    if response.status_code == 200:
      chosen_route = util.helper.choose_a_route(response)
      
  except Exception as e:
    print("Exception: ", e)

if __name__ == "__main__":
  mbta_rider()
