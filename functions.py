def split_categories(dataframe, column): 
    # splits up categories by their sublevels into separate columns
    category_1 = []
    category_2 = []
    category_3 = []

    for x in column:
        # if not a string then appends nan to all categories
        if type(x) != str:
            category_1.append(float('NaN'))
            category_2.append(float('NaN'))
            category_3.append(float('NaN'))
            continue
        # appends to appropriate list and fills 
        # nan for remaining categories
        split = x.split('.')
        if len(split) == 1:
            category_1.append(split[0])
            category_2.append(float('NaN'))
            category_3.append(float('NaN'))
        elif len(split) == 2:
            category_1.append(split[0])
            category_2.append(split[1])
            category_3.append(float('NaN'))
        elif len(split) == 3:
            category_1.append(split[0])
            category_2.append(split[1])
            category_3.append(split[2])

    print(category_1)
    print(category_2)
    print(category_3)

    dataframe['category_1'] = dataframe[category_1]
    dataframe['category_2'] = dataframe[category_2]
    dataframe['category_3'] = dataframe[category_3]