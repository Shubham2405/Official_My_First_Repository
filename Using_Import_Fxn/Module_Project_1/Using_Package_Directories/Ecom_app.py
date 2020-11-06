#Tip use __init__.py file to make any folder a package directory .

# Method 1 entire package

import Ecom_Project.shipping
Ecom_Project.shipping.shipping_cost()


 
# Method 2 only modules from package

from Ecom_Project import shipping
shipping.shipping_cost()



# Method 3 functions from module

from Ecom_Project.shipping import shipping_cost
shipping_cost()