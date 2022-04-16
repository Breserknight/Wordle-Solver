mod = {1:31, 2:28 , 3:31 , 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

def leap(year):
    if year%4 == 0:
        if year % 100 == 0 and year % 400 == 0:
            return 1
        elif year%100 == 0: return 0
        else: return 1
    else: return 0

with open("wordle.txt", "r") as f:
    x = f.readline().split(',')
    space = "\n-----------------------------------------------------------------------\n"
    while True:
        choice  = int(input(f"{space}1. Find A Word By Word\n\n2. Find A Word By Number\n\n3. Find By Date\n\n4. Exit\n\nEnter Choice :: "))
        print(space)
        if choice == 1:
            p = input('Enter a Word : ')
            count = 0
            for i in x:
                if i[1:len(i)-1] == p:
                    count+=1
                    break
                else:
                    count+=1
            if count < len(x) or x[-1][1:len(x[-1])- 1] == p:
                print(f"Word Count {p} -> {count}")
            else: print("::: WORD NOT FOUND ::: ")
        elif choice == 2:
            p = int(input("Enter a number between 1 and {} : ".format(len(x))))
            if p > len(x):
                print("Invalid Number\n")
                continue
            count = 1
            for i in x:
                if count == p:
                    print("Word is {}".format(i))
                    break
                else: count += 1
        elif choice == 3:
            cur = list(map(int, input("Enter Date in DD-MM-YYY Format : ").split('-')))
            # cur[0] = DATE, cur[1] = MONTTH, cur[2] = YEAR
            start_date = [18, 6, 2021]
            find_index = 0
            
            # adds days in sets of months
            if cur[2] - start_date[2] != 0:
                for i in range(start_date[1]+1, 13):
                    find_index += mod[i] # months from oct to dec
                if  cur[2]  - start_date[2] > 1:
                    for o in range(cur[2] - start_date[2] - 1):
                        if leap(cur[2] - o + 1): find_index += 1
                        for i in range(1, 13):
                            find_index += mod[i]

                find_index += mod[start_date[1]] - start_date[0] # days in oct

                for i in range(1, cur[1]):
                    find_index += mod[i]
                if leap(cur[2] and cur[1] >= 2): find_index += 1
                find_index += cur[0]

                p = find_index + 1
                count = 1

                for i in x:
                    if count == p:
                        print("Word is {}".format(i))
                        break
                    else: count += 1
        elif choice == 4:
            break
        else:
            print(": : : Invalid Choice : : : ")
