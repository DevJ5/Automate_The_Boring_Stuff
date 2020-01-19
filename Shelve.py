import shelve

#shelfFile = shelve.open("../somefile")
#shelfFile['cats'] = ['Zophie', 'Pooka', 'Simon', 'Fat-tail']
#shelfFile.close()



shelfFile = shelve.open('../somefile')
#shelfFile['student'] = {
#    'name': 'Bert',
#    'age': '33'
#    }

# list(shelfFile.keys())
# list(shelfFile.values())
print(shelfFile['student'])
shelfFile.close()


