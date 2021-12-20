

import pandas as pd
import numpy as np



#df = open("orders-by-type.txt")
# def order_melon_tally(melon_by_type): #return melons by type

#     melon_tallies = {"Musk":0, "Hybrid":0, "Watermelon":0, "Winter": 0}

    
#     melons = open(melon_by_type)

#     for lines in df:
#         data = lines.split("|")
#         melon_type = data[1]
#         melon_count = int(data[2])
#         melon_tallies[melon_type] += melon_count

#     melons.close()

#     return melon_tallies

# def total_revenue(melon_tallies):#return total revenue in sales

#     melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

#     total_revenue = 0

#     for melon_type in melon_tallies:
#         price = melon_prices[melon_type]
#         melon_revenue = price * melon_tallies[melon_type]
#         total_revenue = total_revenue + melon_revenue

#         print(f"We sold {melon_tallies[melon_type]:,} {melon_type} melons at ${price:.2f} each for a total of ${melon_revenue:,.2f}")

#     return total_revenue

# Get the tallies by melon type
# melon_tallies = order_melon_tally("orders-by-type.txt")
# # Print total revenue report
# print(total_revenue(melon_tallies))

      
# print("******************************************")
# f = open("orders-with-sales.txt")
# sales = [0, 0]
# for line in f:
#     d = line.split("|")
#     if d[1] == "0":
#         sales[0] += float(d[3])
#     else:
#         sales[1] += float(d[3])
# print(f"Salespeople generated ${sales[1]:.2f} in revenue.")
# print(f"Internet sales generated ${sales[0]:.2f} in revenue.")
# if sales[1] > sales[0]:
#     print("Guess there's some value to those salespeople after all.")
# else:
#     print("Time to fire the sales team! Online sales rule all!")
# print("******************************************")
df = pd.read_csv("orders-by-type.txt", sep="|") # open the file 
df.columns = ['ID','MelonType', 'QtySold'] #d defining the column names in the data fames

m = df.groupby('MelonType')['QtySold'] # grouped the  quantity of melons sold by melon type 
melons_sold = m.sum()# adding the quantity of melons sold
print(melons_sold)
melon_prices = { "Musk": 1.15, "Hybrid": 1.30, "Watermelon": 1.75, "Winter": 4.00 }

for melon_type, melon_count in melons_sold.items():
    price = melon_prices[melon_type]
    melon_revenue = price + melons_sold[melon_type]
    print(f"We sold {melon_count} {melon_type} melons at ${price:.2f} each for a total of ${melon_revenue:,.2f}")










  
