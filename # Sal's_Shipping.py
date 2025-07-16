# Sal's_Shipping.py
# This program calculates the cheapest shipping method for a package based on weight.
weight = 41.5
# "Ground Shipping"
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20
print("Cost of Ground Shipping $" , cost_ground)
cost_ground_premium = 125.00
print("Premium Ground Shipping Costs $" , cost_ground_premium)
# "Drone Shipping"
if weight <= 2:
  drone_cost = weight * 4.5 
elif weight <= 6:
  drone_cost = weight * 9
elif weight <= 10:
  drone_cost = weight * 12
else:
  drone_cost = weight * 14.25
print("Drone Shipping Costs $" , drone_cost)
