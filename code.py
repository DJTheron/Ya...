import time

tasks = []                                      # this is a list that will hold all the tasks that are added

while True:
    print('\n\n\nWelcome to your To-Do List')
    print('1. Add tasks.')
    print('2. List tasks.')
    print('3. Finish a task.')
    print('4. Quit.')

    choice = input('Please enter a number: ')

    if choice == '1':
        try:
            task_number = int(input('How many tasks do you want to add? '))
        except ValueError:
            print('Please enter a valid number of tasks.')
            continue
        if task_number <= 0:
            print('Please enter at least one task.')
            continue
        for i in range(task_number):
            task = input(f'{i + 1}: ')          # prompt for each task using 1-based numbering for display
            tasks.append(task)                  # puts all the tasks in the list tasks[]
    elif choice == '2':
        if len(tasks) == 0:                     # Check if task list is empty
            print('No tasks yet!')
        else:
            print('\nYour tasks:')
            for i, task in enumerate(tasks):    # enumerate provides both the index and the task value
                print(f'{i + 1}. {task}')       # again this is used to print starting from 1 using i
                time.sleep(0.5)                 # this is used to make it wait a bit before it prints the next task
            time.sleep(3)                       # this is used to make it wait a bit before it prints from the beginning

    elif choice == '3':
        if len(tasks) == 0:
            print('No tasks to complete.')
        else:
            print('\nWhich task did you finish?')
            for i, task in enumerate(tasks):
                print(f'{i + 1}. {task}')
            try:
                finished = int(input('Enter task number: ')) - 1
            except ValueError:
                print('Please enter a valid task number.')
                continue
            if 0 <= finished < len(tasks):
                completed_task = tasks.pop(finished)  # Remove it from the list
                print(f'Great job finishing: {completed_task}!')
            else:
                print('Invalid task number.')

    elif choice == '4':
        print('FINISH YOUR TASKS NOW YOU....')      # Loop instead of repeating several times
        for _ in range(5):
            time.sleep(0.5)
            print('.')
        break               # finally quits and doesn't restart

    else:
        print('Invalid input. Please try again.')     # at the very end in case their input is wrong
