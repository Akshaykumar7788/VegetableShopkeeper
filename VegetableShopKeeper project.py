# VEGETABLE SHOP BILLING SYSTEM
# Using Lists, For Loop, While Loop Only

items = ["Tomato", "Potato", "Onion"]
cost_prices = [15, 22, 30]
sell_prices = [20, 30, 40]
stock = [50, 60, 70]

total_revenue = 0
total_profit = 0

while True:

    print("\n=================================")
    print("     VEGETABLE SHOP SYSTEM")
    print("=================================")
    print("1. Customer")
    print("2. Shop Keeper")
    print("3. Reports")
    print("4. Exit")

    main_choice = int(input("Enter Choice: "))

    # ──────────────── CUSTOMER SECTION ────────────────
    if main_choice == 1:

        cart = []

        while True:

            print("\n=================================")
            print("         CUSTOMER MENU")
            print("=================================")
            print("1. Add Item to Cart")
            print("2. Remove Item from Cart")
            print("3. Update Item Quantity")
            print("4. View Cart")
            print("5. Billing (Checkout)")
            print("6. Exit Customer Menu")

            cust_choice = int(input("Enter Choice: "))

            if cust_choice == 1:

                print("\nAVAILABLE VEGETABLES")
                print("-" * 65)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Stock':<10}")
                print("-" * 65)

                for i in range(len(items)):
                    print(f"{i+1:<5}{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{stock[i]:<10}")

                print("-" * 65)

                choice = int(input("Enter Vegetable Number: "))

                if choice < 1 or choice > len(items):
                    print("Invalid Choice")
                    continue

                qty = int(input("Enter Quantity: "))
                index = choice - 1

                if qty <= 0:
                    print("Quantity must be greater than 0")
                    continue

                if qty > stock[index]:
                    print("Not Enough Stock")
                    continue

                found = False
                for c in range(len(cart)):
                    if cart[c][0] == index:
                        new_qty = cart[c][1] + qty
                        if new_qty > stock[index]:
                            print("Not Enough Stock for total quantity")
                        else:
                            cart[c][1] = new_qty
                            print(f"Updated {items[index]} quantity to {new_qty} in cart")
                        found = True
                        break

                if not found:
                    cart.append([index, qty])
                    print(f"\nItem Added to Cart!")
                    print(f"  Item       : {items[index]}")
                    print(f"  Cost Price : Rs.{cost_prices[index]} per kg")
                    print(f"  Sell Price : Rs.{sell_prices[index]} per kg")
                    print(f"  Quantity   : {qty}")
                    print(f"  Amount     : Rs.{qty * sell_prices[index]}")

            elif cust_choice == 2:

                if len(cart) == 0:
                    print("Cart is empty")
                    continue

                print("\nYOUR CART")
                print("-" * 75)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Qty':<8}{'Amount':<10}")
                print("-" * 75)

                for c in range(len(cart)):
                    idx = cart[c][0]
                    qty = cart[c][1]
                    amt = qty * sell_prices[idx]
                    print(f"{c+1:<5}{items[idx]:<15}{cost_prices[idx]:<15}{sell_prices[idx]:<15}{qty:<8}{amt:<10}")

                print("-" * 75)

                remove = int(input("Enter Cart Item Number to Remove: "))

                if remove < 1 or remove > len(cart):
                    print("Invalid Choice")
                    continue

                removed_item = items[cart[remove - 1][0]]
                cart.pop(remove - 1)
                print(f"{removed_item} removed from cart")

            elif cust_choice == 3:

                if len(cart) == 0:
                    print("Cart is empty")
                    continue

                print("\nYOUR CART")
                print("-" * 75)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Qty':<8}{'Amount':<10}")
                print("-" * 75)

                for c in range(len(cart)):
                    idx = cart[c][0]
                    qty = cart[c][1]
                    amt = qty * sell_prices[idx]
                    print(f"{c+1:<5}{items[idx]:<15}{cost_prices[idx]:<15}{sell_prices[idx]:<15}{qty:<8}{amt:<10}")

                print("-" * 75)

                update = int(input("Enter Cart Item Number to Update: "))

                if update < 1 or update > len(cart):
                    print("Invalid Choice")
                    continue

                new_qty = int(input("Enter New Quantity: "))
                idx = cart[update - 1][0]

                if new_qty <= 0:
                    print("Quantity must be greater than 0")
                elif new_qty > stock[idx]:
                    print("Not Enough Stock")
                else:
                    cart[update - 1][1] = new_qty
                    print(f"{items[idx]} quantity updated to {new_qty}")
                    print(f"New Amount : Rs.{new_qty * sell_prices[idx]}")

            elif cust_choice == 4:

                if len(cart) == 0:
                    print("Cart is empty")
                    continue

                print("\n" + "=" * 75)
                print("                        YOUR CART")
                print("=" * 75)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Qty':<8}{'Amount':<10}")
                print("-" * 75)

                cart_total = 0
                cart_cost_total = 0

                for c in range(len(cart)):
                    idx = cart[c][0]
                    qty = cart[c][1]
                    sell_amt = qty * sell_prices[idx]
                    cost_amt = qty * cost_prices[idx]
                    cart_total = cart_total + sell_amt
                    cart_cost_total = cart_cost_total + cost_amt
                    print(f"{c+1:<5}{items[idx]:<15}{cost_prices[idx]:<15}{sell_prices[idx]:<15}{qty:<8}{sell_amt:<10}")

                print("-" * 75)
                print(f"{'Total Cost (Shop Paid)':<45}{cart_cost_total:<10}")
                print(f"{'Total Bill (Customer Pays)':<45}{cart_total:<10}")
                print(f"{'Profit on This Cart':<45}{cart_total - cart_cost_total:<10}")
                print("=" * 75)

            elif cust_choice == 5:

                if len(cart) == 0:
                    print("Cart is empty. Add items before billing.")
                    continue

                print("\n" + "=" * 75)
                print("                      CUSTOMER BILL")
                print("=" * 75)
                print(f"{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Qty':<8}{'Amount':<10}")
                print("-" * 75)

                customer_bill = 0
                bill_cost_total = 0

                for c in range(len(cart)):
                    idx = cart[c][0]
                    qty = cart[c][1]
                    sell_amt = qty * sell_prices[idx]
                    cost_amt = qty * cost_prices[idx]

                    customer_bill = customer_bill + sell_amt
                    bill_cost_total = bill_cost_total + cost_amt

                    stock[idx] = stock[idx] - qty
                    total_revenue = total_revenue + sell_amt
                    total_profit = total_profit + (sell_amt - cost_amt)

                    print(f"{items[idx]:<15}{cost_prices[idx]:<15}{sell_prices[idx]:<15}{qty:<8}{sell_amt:<10}")

                print("-" * 75)
                print(f"{'Total Cost (Shop Paid)':<53}{bill_cost_total:<10}")
                print(f"{'TOTAL BILL (Customer Pays)':<53}{customer_bill:<10}")
                print(f"{'Profit Earned':<53}{customer_bill - bill_cost_total:<10}")
                print("=" * 75)

                cart = []
                print("\nThank you for your purchase!")
                break

            elif cust_choice == 6:
                break

            else:
                print("Invalid Choice")

    # ──────────────── SHOP KEEPER SECTION ────────────────
    elif main_choice == 2:

        while True:

            print("\n=================================")
            print("        SHOP KEEPER MENU")
            print("=================================")
            print("1. Add New Item")
            print("2. Modify Item")
            print("3. Remove Item")
            print("4. View All Items")
            print("5. Back")

            shop_choice = int(input("Enter Choice: "))

            # ── 1. ADD NEW ITEM ──
            if shop_choice == 1:

                print("\n--- ADD NEW ITEM ---")

                new_item = input("Enter Item Name: ")
                new_stock = int(input("Enter Stock Quantity: "))

                # Show cost price and selling price clearly
                print("\n--- PRICE DETAILS ---")
                new_cost = int(input("Enter Cost Price  (price shop paid): "))
                new_sell = int(input("Enter Sell Price  (price for customer): "))

                if new_sell <= new_cost:
                    print("Warning: Sell Price is not greater than Cost Price. No profit will be made!")

                margin = new_sell - new_cost

                items.append(new_item)
                cost_prices.append(new_cost)
                sell_prices.append(new_sell)
                stock.append(new_stock)

                print("\n" + "=" * 55)
                print("          ITEM ADDED SUCCESSFULLY")
                print("=" * 55)
                print(f"  Item Name    : {new_item}")
                print(f"  Stock        : {new_stock}")
                print(f"  Cost Price   : Rs.{new_cost} per kg")
                print(f"  Sell Price   : Rs.{new_sell} per kg")
                print(f"  Profit Margin: Rs.{margin} per kg")
                print("=" * 55)

            # ── 2. MODIFY ITEM ──
            elif shop_choice == 2:

                print("\nITEM LIST")
                print("-" * 65)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Stock':<10}")
                print("-" * 65)

                for i in range(len(items)):
                    margin = sell_prices[i] - cost_prices[i]
                    print(f"{i+1:<5}{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{stock[i]:<10}")

                print("-" * 65)

                modify = int(input("Enter Item Number To Modify: "))

                if modify >= 1 and modify <= len(items):

                    index = modify - 1

                    print(f"\nModifying: {items[index]}")
                    print(f"  Current Cost Price : Rs.{cost_prices[index]}")
                    print(f"  Current Sell Price : Rs.{sell_prices[index]}")
                    print(f"  Current Stock      : {stock[index]}")

                    print("\n--- ENTER NEW VALUES ---")
                    new_cost = int(input("Enter New Cost Price: "))
                    new_sell = int(input("Enter New Sell Price: "))
                    new_stock = int(input("Enter New Stock: "))

                    if new_sell <= new_cost:
                        print("Warning: Sell Price is not greater than Cost Price. No profit will be made!")

                    cost_prices[index] = new_cost
                    sell_prices[index] = new_sell
                    stock[index] = new_stock

                    print("\n" + "=" * 55)
                    print("          ITEM MODIFIED SUCCESSFULLY")
                    print("=" * 55)
                    print(f"  Item Name    : {items[index]}")
                    print(f"  Stock        : {stock[index]}")
                    print(f"  Cost Price   : Rs.{cost_prices[index]} per kg")
                    print(f"  Sell Price   : Rs.{sell_prices[index]} per kg")
                    print(f"  Profit Margin: Rs.{sell_prices[index] - cost_prices[index]} per kg")
                    print("=" * 55)

                else:
                    print("Invalid Item Number")

            # ── 3. REMOVE ITEM ──
            elif shop_choice == 3:

                print("\nITEM LIST")
                print("-" * 65)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Stock':<10}")
                print("-" * 65)

                for i in range(len(items)):
                    print(f"{i+1:<5}{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{stock[i]:<10}")

                print("-" * 65)

                remove = int(input("Enter Item Number To Remove: "))

                if remove >= 1 and remove <= len(items):

                    index = remove - 1

                    print(f"\nRemoving Item: {items[index]}")
                    print(f"  Cost Price : Rs.{cost_prices[index]}")
                    print(f"  Sell Price : Rs.{sell_prices[index]}")
                    print(f"  Stock      : {stock[index]}")

                    items.pop(index)
                    cost_prices.pop(index)
                    sell_prices.pop(index)
                    stock.pop(index)

                    print("Item Removed Successfully")

                else:
                    print("Invalid Item Number")

            # ── 4. VIEW ALL ITEMS ──
            elif shop_choice == 4:

                if len(items) == 0:
                    print("No items in shop")
                    continue

                print("\n" + "=" * 70)
                print("                    SHOP ITEM LIST")
                print("=" * 70)
                print(f"{'No':<5}{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Margin':<10}{'Stock':<10}")
                print("-" * 70)

                for i in range(len(items)):
                    margin = sell_prices[i] - cost_prices[i]
                    print(f"{i+1:<5}{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{margin:<10}{stock[i]:<10}")

                print("-" * 70)
                print(f"  Total Items in Shop: {len(items)}")
                print("=" * 70)

            elif shop_choice == 5:
                break

            else:
                print("Invalid Choice")

    # ──────────────── REPORT SECTION ────────────────
    elif main_choice == 3:

        while True:

            print("\n=================================")
            print("          REPORT MENU")
            print("=================================")
            print("1. Vegetable Report")
            print("2. Revenue Report")
            print("3. Profit Report")
            print("4. Itemized Profit")
            print("5. Back")

            report_choice = int(input("Enter Choice: "))

            if report_choice == 1:

                print("\nVEGETABLE REPORT")
                print("-" * 60)
                print(f"{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Stock':<10}")
                print("-" * 60)

                for i in range(len(items)):
                    print(f"{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{stock[i]:<10}")

                print("-" * 60)

            elif report_choice == 2:

                print("\n" + "-" * 30)
                print("TOTAL REVENUE =", total_revenue)
                print("-" * 30)

            elif report_choice == 3:

                print("\n" + "-" * 30)
                print("TOTAL PROFIT =", total_profit)
                print("-" * 30)

            elif report_choice == 4:

                print("\nITEMIZED PROFIT REPORT")
                print("-" * 55)
                print(f"{'Item':<15}{'Cost Price':<15}{'Sell Price':<15}{'Margin':<10}")
                print("-" * 55)

                for i in range(len(items)):
                    margin = sell_prices[i] - cost_prices[i]
                    print(f"{items[i]:<15}{cost_prices[i]:<15}{sell_prices[i]:<15}{margin:<10}")

                print("-" * 55)

            elif report_choice == 5:
                break

            else:
                print("Invalid Choice")

    elif main_choice == 4:

        print("\nThank You For Visiting")
        break

    else:
        print("Invalid Choice")
