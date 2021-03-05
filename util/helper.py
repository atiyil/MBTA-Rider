import ast

def choose_a_route(response):
  """ This function provides a list of routes to the user and receives the user's choice"""
  
  # min response should be "{'data':[]}"
  if len(response) > 10:
    routes = ast.literal_eval(response.content.decode('UTF-8'))
    
    if 'data' in routes:
      route_list = []
      
      for route in routes.get('data'):
        # create a list of available routes
        route_list.append(route.get('attributes').get('direction_destinations')[0].lower())
        print(route.get('attributes').get('long_name'), " ==> ", route_list[-1])
        
        route_list.append(route.get('attributes').get('direction_destinations')[1].lower())
        print(route.get('attributes').get('long_name'), " ==> ", route_list[-1])
      
      print("Please select a route from the list above: (such as ashmont, alewife, oak grove, etc )")
      
      # receive the user's choice and return it
      chosen_route = None
      while not chosen_route:
        chosen_route = input().lower()
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