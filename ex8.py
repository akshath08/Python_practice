while True:
    veg = ['brinjal', 'tomato', 'onion', 'ladies finger', 'carrot', 'potato']
    quantity = [40, 45, 50, 40, 30, 20]
    selling_price = [20, 20, 20, 20, 20, 20]
    market_price = [10, 10, 10, 10, 10, 10]
    cart = []
    kgs = []
    item_price = []
    purchased_item = []
    itemized_price = []
    customer_name = []
    bought_price = []
    flag = True

    while flag:
        user = input('Are you (owner (or)customer):')

        if user == 'owner':
            name = input('enter the name please:')
            key = int(input('enter the password:'))
            if key == 262002:
                list1 = sum(item_price)
                list2 = sum(market_price)
                today_profit = list1 - list2
                print('-' * 30, 'today profit', '-' * 30)
                print('today_profit is', today_profit)
                print('-' * 70)
                print()
                print('*' * 30, 'no.of customers came today', '*' * 20)

                for i in zip(customer_name, bought_price):
                    print(i)
                    print()

                print('*' * 35, 'Remaining_veg And Their_Quantity', '*' * 30)
                for it in zip(veg, quantity):
                    print(it)
                    print()
                close = input('do you wanna close the shop(yes/no):')
                if close == 'yes':
                    print('thank you')
                    print('shop closed')
                    flag = False
                    break
                else:
                    basket = []
                    kgs = []
                    price = []
                    print('*' * 70)
                    print('do you want add the vegetable (or) remove the vegetable (or)close the shop')
                    print('*' * 30, 'options', '*' * 30)
                    print('1.To remove vegetable from veg')
                    print('2.To display vegetables')
                    print('3.To add to basket')
                    print('4.total_bill')
                    print('5.closing the shop ')
                    print('*' * 70)
                    while True:
                        num = int(input('select any option:'))
                        if num == 1:
                            print('*' * 30, 'menu', '*' * 30)
                            for i in zip(veg, quantity):
                                print(i)
                                print()
                            item = input('what item you want to remove:')
                            if item in veg:
                                idx = veg.index(item)
                                print()
                                qty = float(input('how much quantity you want remove:'))
                                quantity[idx] = quantity[idx] - qty
                                print(qty, 'kgs is removed from the quantity')
                                print('*' * 70)
                            if item not in veg:
                                print('item is not there')
                        elif num == 2:
                            for it in zip(veg, quantity):
                                print(it)
                                print()
                        elif num == 3:
                            print('*' * 35, 'items in market', '*' * 30)
                            market = ['brinjal', 'tomato', 'onion', 'ladies finger', 'carrot', 'potato', 'califlower', 'cucumber']
                            quant = [50, 50, 50, 50, 50, 50, 50, 50]
                            for i in zip(market, quant):
                                print(i)
                                print()
                            market_price = [10, 10, 10, 10, 10, 10, 10, 10]
                            print('*' * 70)
                            item = input('what item you want:')
                            if item in market:
                                idx = market.index(item)
                                qty = float(input('enter the quantity:'))
                                if qty <= quant[idx]:
                                    amount = qty * market_price[idx]
                                    print('amount for  item is', amount)
                                    if item in basket:
                                        basket.append(item)
                                        veg.append(item)
                                        price.append(amount)
                                        kgs.append(qty)
                                        quantity.append(qty)
                                        print('item is added to basket', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)

                                    else:
                                        if item not in basket:
                                            basket.append(item)
                                            veg.append(item)
                                            price.append(amount)
                                            kgs.append(qty)
                                            quantity.append(qty)
                                            print('item is added to  basket', qty, 'kgs')
                                            print('amount is added to item_price')
                                            print('*' * 70)

                                else:

                                    print('out off stock')
                                    print('we only have this much of ', quant[idx], 'kgs')

                            else:
                                print('we dont have that item')
                                print('do you want anything')

                        elif num == 4:
                            print('*' * 70)
                            print('name is ', name)
                            print(basket, '-->', price)
                            print('total items price', sum(price))
                            print('*' * 70)

                        elif num == 5:
                            print('shop is closed')
                            print('thank you')
                            flag = False
                            break


            else:
                print('*' * 70)
                print('invalid password')
                print('*' * 70)

        else:
            if user == 'customer':
                while True:
                    name = input('enter the name please:')
                    customer_name.append(name)
                    ph_no = input('enter the ph_no:')
                    if len(str(ph_no)) == 10:
                        break  # Break out of the inner while loop if phone number is valid
                    else:
                        print('invalid number')
                        continue  # Ask for phone number again

                cart = []
                kgs = []
                item_price = []
                print('*' * 35, 'menu', '*' * 30)
                for it in zip(veg, quantity):
                    print(it)
                    print()
                print('*' * 70)
                print('*' * 30, 'options', '*' * 30)
                print('1.add item to cart')
                print('2.diplay items in cart')
                print('3.remove items in cart')
                print('4.total bill')
                print('*' * 70)
                while True:
                    ch = int(input('select any action-option:'))
                    if ch == 1:
                        item = input('what item do you want:')
                        if item == veg[0]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                print('amount for  brinjal', amount)
                                quantity[idx] = quantity[idx] - qty
                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    kgs.append(qty)
                                    purchased_item.append(item)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to  cart', qty, 'kgf')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out off stock')
                                print('you have only ', quantity[0], 'kgs')

                        elif item == veg[1]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                print('amount for tomato', amount)
                                quantity[idx] = quantity[idx] - qty

                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    kgs.append(qty)
                                    purchased_item.append(item)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to cart', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out off stock')
                                print('you have only ', quantity[1], 'kgs')
                        elif item == veg[2]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                print('amount for onion', amount)
                                quantity[idx] = quantity[idx] - qty

                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    kgs.append(qty)
                                    purchased_item.append(item)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to cart', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out off stock ')
                                print('you have only ', quantity[2], 'kgs')
                        elif item == veg[3]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                quantity[idx] = quantity[idx] - qty
                                print('amount for ladies finger', amount)
                                quantity[idx] = quantity[idx] - qty

                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to cart', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out of stock')
                                print('you have only ', quantity[3], 'kgs')
                        elif item == veg[4]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                print('amount for carrot', amount)
                                quantity[idx] = quantity[idx] - qty

                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    kgs.append(qty)
                                    purchased_item.append(item)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to cart', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out of stock')
                                print('you have only ', quantity[4], 'kgs')
                        elif item == veg[5]:
                            qty = float(input('enter the quantity:'))
                            idx = veg.index(item)
                            if qty <= quantity[idx]:
                                amount = qty * selling_price[idx]
                                print('amount for potato', amount)
                                quantity[idx] = quantity[idx] - qty

                                if item in cart:
                                    cart.append(item)
                                    item_price.append(amount)
                                    kgs.append(qty)
                                    purchased_item.append(item)
                                    itemized_price.append(amount)
                                    print('item is added to cart', qty, 'kgs')
                                    print('amount is added to item_price')
                                    print('*' * 70)
                                else:
                                    if item not in cart:
                                        cart.append(item)
                                        item_price.append(amount)
                                        kgs.append(qty)
                                        purchased_item.append(item)
                                        itemized_price.append(amount)
                                        print('item is added to cart', qty, 'kgs')
                                        print('amount is added to item_price')
                                        print('*' * 70)
                            else:
                                print('out of stock')
                                print('you have only ', quantity[5], 'kgs')
                        else:
                            print('we dont have that item')

                    if ch == 2:
                        print('*' * 30, 'ITEMS IN CART', '*' * 25)
                        for it in zip(cart, kgs):
                            print(it[0], '-->', it[1])
                            print()

                    if ch == 3:
                        print('*' * 30, 'items in cart', '*' * 30)
                        for it in zip(cart, kgs):
                            print(it)
                            print()
                        item = input('what item you want to remove:')
                        if item in cart:
                            idx = cart.index(item)
                            print()
                            qty = float(input('how much quantity you want remove:'))
                            if qty <= kgs[idx]:
                                kgs[idx] = kgs[idx] - qty
                                amount = qty * selling_price[idx]
                                item_price[idx] = item_price[idx] - amount
                                print(qty, 'kgs has been removed')
                                print('*' * 70)
                        if item not in cart:
                            print('item is not there')

                    if ch == 4:
                        print('*' * 70)
                        print('name is ', name)
                        print('ph_no is', ph_no)
                        print('-' * 30, 'items', '-' * 30)
                        for it in zip(cart, item_price):
                            print(it)
                            print()
                        total_price = sum(item_price)
                        print('-' * 30, 'price', '-' * 30)
                        print('tatal price=', total_price)
                        bought_price.append(total_price)
                        print()
                        print('*' * 70)
                        # Reset cart, kgs, and item_price for the next customer
                        cart = []
                        kgs = []
                        item_price = []
                        # Re-enter the customer loop
                        break  # Break out of the inner customer loop
        break  # Break out of the outer loop if the user is either 'owner' or 'customer'