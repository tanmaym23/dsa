def locate_card(cards,query):
    lo,hi=0, len(cards)-1

    while lo <=hi:
        mid=(lo+hi)//2
        mid_number=cards[mid]

        print("lo:",lo," ,hi:",hi," ,mid:",mid," ,mid_number:",mid_number )

        if mid_number==query:
            print(mid)
            break
            # return mid
        elif mid_number<query:
            hi=mid-1
        elif mid_number>query:
            lo=mid+1
    
    return -1

card = [13, 11, 10, 7, 4, 3, 1, 0]
query =11
qwe=locate_card(card,query)   