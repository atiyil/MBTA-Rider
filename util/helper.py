import json

def select_a_route(response):
  """ This function provides a list of routes to the user and receives the user's choice"""
  
  # min response should be "{'data':[]}"
  if len(response.content) > 10:
    routes = json.loads(response.content.decode('UTF-8'))
    
    if 'data' in routes:
      route_list = []
      
      for route in routes.get('data'):
        # create a list of available routes
        route_list.append(route.get('id'))
        print(route_list[-1])
        
      print("Please select a route from the list above: (such as Red, Green-B, etc )")
      
      # receive the user's choice and return it
      chosen_route = None
      while not chosen_route:
        chosen_route = input()
        if chosen_route not in route_list:
          print("Please enter a valid route!")
          chosen_route = None
        else:
          print(chosen_route)
      
      return chosen_route
    
    else:
      return None
  else:
    return None
  
def select_a_stop(response):
  """ This function provides a list of stops to the user and receives the user's choice"""

  # min response should be "{'data':[]}"
  if len(response.content) > 10:
    stops = json.loads(response.content.decode('UTF-8'))
  
    if 'data' in stops:
      stop_dict = {}
    
      for stop in stops.get('data'):
        # create a dictionary {name:id} of available stops
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
        else:
          print(stop_dict.get(selected_stop))

      return selected_stop

  else:
    return None
