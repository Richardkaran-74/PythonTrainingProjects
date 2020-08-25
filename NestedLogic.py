r_day,r_month,r_year = (int(e) for e in input().strip().split(' '))
d_day,d_month,d_year = (int(e) for e in input().strip().split(' '))

#check year
if r_year < d_year:
    print(0)
elif r_year == d_year:
    #check month
    if r_month < d_month:
        print(0)
    elif r_month == d_month:
        #check day
        if r_day < d_day:
            print(0)
        else:
            print(15 * (r_day - d_day))
    else:
        print(500 * (r_month - d_month))

else:
    print(10000)

