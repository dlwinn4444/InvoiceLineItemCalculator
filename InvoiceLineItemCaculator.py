#Dwayne Winn CIS362 Invoice Line Item Caculator"

def main():
    g_total = float()
    print("The Invoice Line Item Calculator")
    answer = "y"
    print(answer)
    while answer == "y":
        price = i_price()
        quantity = i_quantity()
        total = price * quantity 
        print()
        print("Price: $", f"{price: .2f}") 
        print("Quantity: ", quantity)
        print("Total: $y",  f"{total: .2f}")
        answer = input("Enter another line item? (y/n): ")
        g_total += total
   
    print()   
    print("Grand total : $", f"{g_total: .2f}")  
    print("Thank you!") 
   

def i_price():
     while True:
         try:
            price = float(input("Enter price: "))
            return price
         except ValueError:
             print("Invaild decimal.//(0.00) Please try again.")       
         
def i_quantity():
    while True:
       try:
          quantity = int(input("Enter quantity: "))
          return quantity
       except ValueError:
          print("Invaild integer. Please try again.")

if __name__== "__main__":
   main()