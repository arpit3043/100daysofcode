list = ['ajay', 'akeesha', 'anubhav', 'anuj', 'ashish']
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
print(list[-1])
print(list[-2])
print(list[-3])
print(list[-4])
print(list[-5])


print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[0].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[1].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[2].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[3].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[4].title())

print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[-1].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[-2].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[-3].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[-4].title())
print('you are invited to my birthday party on 19 july 2020' + 'Mr' + list[-5].title())

list.remove('ashish')
print(list)

list.insert(0, 'brijesh sir')
print(list)

list.insert(1, 'sandeep')
print(list)