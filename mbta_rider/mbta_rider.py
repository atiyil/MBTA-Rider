import requests
import util.helper
import json


def mbta_rider():
  """ This function provides a predicted departure time for a train based on user input"""
  try:
    # make a GET request to get route types 0 and 1 (light rail and heavy rail)
    response_route = requests.get('https://api-v3.mbta.com/routes?filter%5Btype%5D=0%2C1')
    if response_route.status_code == 200:
      selected_route, available_directions = util.helper.select_a_route(response_route)
      
      response_stop = requests.get(f'https://api-v3.mbta.com/stops?filter%5Broute%5D={selected_route}')
      if response_stop.status_code == 200:
        # print(response_stop.content)
        selected_stop = util.helper.select_a_stop(response_stop)
        
        # use available directions from the first get call
        selected_direction = util.helper.select_a_direction(available_directions)
      
        response_prediction = requests.get(f'https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D={selected_direction}&filter%5Bstop%5D={selected_stop}&filter%5Broute%5D={selected_route}')
        if response_prediction.status_code == 200:
          prediction = json.loads(response_prediction.content.decode('UTF-8'))
          print("next predicted departure time: ",prediction.get('data')[0].get('attributes').get('departure_time'))
          
        # TODO: improve error/exception handling
        
  except Exception as e:
    print("Exception: ", e)

if __name__ == "__main__":
  mbta_rider()
