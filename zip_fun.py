from termcolor import colored

print(colored("="*30 + " WELCOME TO OUR PYTHON JOURNEY " + "="*24, 'magenta'))

print("-" * 60)
print("Element/Month	 January	    February	March")
print("Total Sales	   52,000.00	    51,000.00	48,000.00")
print("Production Cost	 46,800.00	    45,900.00	43,200.00")
print("-" * 60)


Total_sales = [52000.00 , 51000.00,	48000.00]
Prod_cost = [46800.00 ,	45900.00, 43200.00]
for sale1 ,sale2 in zip(Total_sales ,Prod_cost):
    print(f"Total profit: {sale1 - sale2}")