#Dwayne Winn CIS362 Invoice Line Item Calator"

#start Main function 
def main():
    #set grand total to 0
    g_total = float()
    #print title
    print("The Invoice Line Item Calculator")
    #set answer to yes
    answer = "y"
    #start loop
    while answer == "y":
        #get price
        price = i_price()
        #get quantity
        quantity = i_quantity()
        #caculate and display tota; amount
        total = price * quantity 
        print()
        print("Price: $", f"{price: .2f}") 
        print("Quantity: ", quantity)
        print("Total: $y",  f"{total: .2f}")
        #get user input for answer
        answer = input("Enter another line item? (y/n): ")
        #caculate grand toital
        g_total += total
    #display grand total
    print()   
    print("Grand total : $", f"{g_total: .2f}")  
    print("Thank you!") 
 # user input price function
def i_price():
     while True:
         try:
            price = float(input("Enter price: "))
            return price
         except ValueError:
             print("Invaild decimal.//(0.00) Please try again.")       
#user input quantity function    
def i_quantity():
    while True:
       try:
          quantity = int(input("Enter quantity: "))
          return quantity
       except ValueError:
          print("Invaild integer. Please try again.")

if __name__== "__main__":
   main()