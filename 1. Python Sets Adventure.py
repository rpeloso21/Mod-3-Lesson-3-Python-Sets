# Task 1



our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

shared_routes = our_routes.intersection(competitor_routes)
print(f"\nThe destinations that we share with our competitor are {shared_routes}.")

our_unique_destinations = our_routes.difference(competitor_routes)
print(f"\nThe destinations that only we fly to are {our_unique_destinations}.")

unshared_routes = our_routes.symmetric_difference(competitor_routes)
print(f"\nThe destinations that are not shared between either airlines are {unshared_routes}.\n")
