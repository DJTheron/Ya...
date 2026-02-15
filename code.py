import time

tasks = []                                      # this is a /list\ that will hold all the tasks that atre added

while True:
    print('\n\n\nWelcome to your To-Do List')
    print('1. Add tasks.')
    print('2. List tasks.')
    print('3. Finish a task.')
    print('4. Quit.')

    choice = input('Please enter a number: ')

    if choice == '1':
        tasknumber = int(input('How many tasks do you want to add? '))
        for i in range(tasknumber): 
            task = input(f'{i + 1}: ')          # instead of numberi, numberii it adds all of them and the +1 is cuz it starts at 0
            tasks.append(task)                  # puts all the tasks in the list Task[] 
    elif choice == '2':
        if len(tasks) == 0:                     # len is for length and shows that if there are 3 items it prints the 3 items but if there are 0 it prints no tasks yet
            print('No tasks yet!')
        else:
            print('\nYour tasks:')              # here there are tasks and it prints the tasks that you used
            for i, task in enumerate(tasks):    # enumerate is what it used to print all the things in tasks 
                print(f'{i + 1}. {task}')       # agian this is used to print starting from 1 using i
                time.sleep(0.5)                 # this is used to make it wait a bit before it prints the next task
            time.sleep(3)                       # this is used to make it wait a bit before it prints from the begining

    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks to complete.')
        else:
            print('\nWhich task did you finish?')
            for i, task in enumerate(tasks):
                print(f'{i + 1}. {task}')
            finished = int(input('Enter task number: ')) - 1
            if 0 <= finished < len(tasks):
                removed = tasks.pop(finished)  # Remove it from the list
                print(f'Great job finishing: {removed}!')
            else:
                print('Invalid task number.')

    elif choice == '4':
        print('FINISH YOUR TASKS NOW YOU....')      # Loop instead of repeating 14 times
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        time.sleep(0.5)
        print('.')
        break               # finally quits and dosnt restart

    else:
        print('Invalid input. Please try again.')     # at the verry end incase their input is rong
