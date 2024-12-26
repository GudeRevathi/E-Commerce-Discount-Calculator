price=[]
while True:
    item_price=input("enter item price:")
    if item_price.lower()=="done":
        break
    price.append(float(item_price)) 
total_price=sum(price)
discount=float(input("enter discount:"))
discount_amount=(discount/100)*total_price 
final_price=total_price-discount_amount 
print(final_price)
