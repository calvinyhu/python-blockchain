import pickle

user_data = []
with open('demo.txt', mode='rb') as f:
    file_content = pickle.loads(f.read())
    user_data = file_content['data']
user_input = input('Type something in: ')
while user_input:
    if user_input == 'q':
        break
    if user_input == 'o':
        print(user_data)
    else:
        user_data.append(user_input)
        print(user_data)
    user_input = input('Type something in: ')
with open('demo.txt', mode='wb') as f:
    f.write(pickle.dumps({'data': user_data}))
print('Done!')
