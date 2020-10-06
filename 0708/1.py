import datetime


def main():
    days = ['Monday', 'Tuesday', 'Wednesday',
            'Thursday', 'Friday', 'Saturday', 'Sunday']
    print('Robot: "Hi, What\'s your name?"')
    name = input('You: ')
    print(f'Robot: "Hello, {name}."')

    q = input('You: ')
    while(q != 'What day is it?'):
        print('Robot: "THX, but I don\'t know what do you mean, please ask me "What day is it?"')
        q = input('You: ')

    print(f'Robot: "Today is {days[datetime.datetime.today().weekday()]}."')


if __name__ == "__main__":
    main()
