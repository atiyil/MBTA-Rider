import requests
import util.helper


def mbta_rider():
  """ This function provides predicted departure time for a train based on user input"""
  try:
    # make a GET request to get route types 0 and 1 (light rail and heavy rail)
    response_route = requests.get('https://api-v3.mbta.com/routes?filter%5Btype%5D=0%2C1')
    if response_route.status_code == 200:
      selected_route = util.helper.select_a_route(response_route)
      
      response_stop = requests.get(f'https://api-v3.mbta.com/stops?filter%5Broute%5D={selected_route}')
      if response_stop.status_code == 200:
        print(response_stop.content)
        selected_stop = util.helper.select_a_stop(response_stop)
        
        # use direction_destinations from first get call
        selected_direction = util.helper.select_a_direction(response_route)
      
        response_prediction = requests.get(f'https://api-v3.mbta.com/predictions?filter%5Bdirection_id%5D={selected_direction}&filter%5Bstop%5D={selected_stop}&filter%5Broute%5D={selected_route}')
        if response_prediction.status_code == 200:
          print(response_prediction.content)
          prediction = json.loads(response_prediction.content.decode('UTF-8'))
          print("next predicted departure time: ",prediction.get('data')[0].get('attributes').get('departure_time'))
            
  except Exception as e:
    print("Exception: ", e)

if __name__ == "__main__":
  mbta_rider()
