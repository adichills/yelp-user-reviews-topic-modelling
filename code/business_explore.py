import  json

def filterRestraunts(inputFilename,outputFilename1,outputFilename2):
    restaurants = []
    nonRestaurants = []
    i = 0
    with open(inputFilename,'r',encoding='utf8') as f:
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)


            business = json.loads(line)
            attributes = business['attributes']
            isRestaurant = False

            categories = business['categories']

            if categories:
                if 'restaurant' in categories.lower():
                    restaurants.append(line)
                else:
                    nonRestaurants.append(line)


            # if attributes:
            #
            #     for key in attributes.keys():
            #         if key.lower().startswith('restaurant'):
            #             restaurants.append(line)
            #             isRestaurant = True
            #             break
            #
            # print(isRestaurant)
            # if isRestaurant == False:
            #     print(isRestaurant)
            #     nonRestaurants.append(line)

        print(str(len(restaurants)) + ' No of restaurants')
        print(str(len(nonRestaurants)) + 'No of non restaurants')

        print (len(restaurants) + len(nonRestaurants))
        print(i)

        def writeDataToFile(outputFileName,data):
            with open(outputFileName,'w',encoding='utf8') as f:
                for business in data:
                    f.write(business)

        writeDataToFile(outputFilename1,restaurants)
        writeDataToFile(outputFilename2,nonRestaurants)









def getBusinessTypes(inputFilename,outputFilename):
    allCategories = set()
    print("processing businesses")
    i = 0
    noCategory = 0
    with open(inputFilename,'r',encoding='utf8') as f:
        for line in f:
            i+=1
            if i % 10000 == 0:
                print(i)
            business = json.loads(line)
            businessCategories = business['categories']
            if businessCategories:
                categories = set(business['categories'].lower().split(','))
                categories = set(map(lambda x: x.strip(),categories))
                allCategories = allCategories.union(categories)
            else:
                noCategory+=1

    print("writing results")
    print('number of different categories ' + str(len(allCategories)))
    print('no categories ' + str(noCategory))
    with open(outputFilename,'w') as f:
        for category in allCategories:
            f.write(category + '\n')


#getBusinessTypes('input/yelp_academic_dataset_business.json','output/business_categories.txt')
filterRestraunts('input/yelp_academic_dataset_business.json','output/restaurants.json','output/nonrestaurants.json')

