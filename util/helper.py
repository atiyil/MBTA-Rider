import json

def select_a_route(response):
  """ This function provides the user a list of routes and
  receives the user's route choice with available directions"""
  
  # min response should be "{'data':[]}"
  if len(response.content) > 10:
    routes = json.loads(response.content.decode('UTF-8'))
    
    if 'data' in routes:
      route_dict = {}
      
      for route in routes.get('data'):
        # create a dictionary of routes with available directions {route_id:direction_destinations}
        route_dict.update({route.get('id'):route.get('attributes').get('direction_destinations')})
        print(route.get('id'))
        
      print("Please select a route from the list above: (such as Red, Green-B, etc )")
      
      # TODO: refactor the code section below as a new function as all 3 functions have it
      # receive the user's choice and return it
      selected_route = None
      while not selected_route:
        selected_route = input()
        if selected_route not in route_dict.keys():
          print("Please enter a valid route!")
          selected_route = None
      
      return selected_route, route_dict.get(selected_route)
    
    else:
      return None
    
  else:
    return None
  
def select_a_stop(response):
  """ This function provides the user a list of stops and receives the user's choice"""

  # min response should be "{'data':[]}"
  if len(response.content) > 10:
    stops = json.loads(response.content.decode('UTF-8'))
  
    if 'data' in stops:
      stop_dict = {}

      for stop in stops.get('data'):
        # create a dictionary of available stops {stop_name:stop_id}
        stop_dict.update({stop.get('attributes').get('name'):stop.get('id')})
        print(stop.get('attributes').get('name'))

      print("Please select a stop from the list above: (such as Park Street, Downtown Crossing, etc )")

      # receive the user's choice and return it
      selected_stop = None
      while not selected_stop:
        selected_stop = input()
        if selected_stop not in stop_dict.keys():
          print("Please enter a valid stop!")
          selected_stop = None

      return selected_stop
    
    else:
      return None
    
  else:
    return None

def select_a_direction(available_directions):
  """ This function provides the user a list of directions for the chosen route and receives the user's choice"""
  for direction in available_directions:
    print(direction)
    
  print("Please select a direction from the list above:")
  
  # receive the user's choice and return it
  selected_direction = None
  while not selected_direction:
    selected_direction = input()
    if selected_direction not in available_directions:
      print("Please enter a valid direction!")
      selected_direction = None
  
  # return the direction id as it will be used in the get call for predictions
  return 0 if available_directions[0] == selected_direction else 1
