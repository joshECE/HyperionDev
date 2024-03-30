# Notes: 
# 1. Use the following username and password to access the admin rights 
# username: admin
# password: password
# 2. Ensure you open the whole folder for this task in VS Code otherwise the 
# program will look in your root directory for the text files.

#=====importing libraries===========
import os
from datetime import datetime, date

DATETIME_STRING_FORMAT = "%Y-%m-%d"

def clear_term():
    '''Clears the current text from the terminal.'''
    os.system('cls||clear')

class Setup:
    '''
    Contains functions to set up .txt files and load variables
    to `task_manager.py` before the user interacts with the program.

    Attributes:

    _task_manager (class): An instance of TaskManager.

    '''
    def __init__(self,task_manager):
        self._task_manager = task_manager
        clear_term()

    def config_txt_files(self):
        '''
        Creates two .txt files used by the program with default contents
        if they do not already exist.

        '''
        if not os.path.exists("tasks.txt"):
            with open("tasks.txt", "w") as default_file:
                default_file.write(
                    "admin;Add functionality to task manager;"
                    "Add additional options and refactor the code.;"
                    "2022-12-01;2022-11-22;No")

        if not os.path.exists("user.txt"):
            with open("user.txt", "w") as default_file:
                default_file.write("admin;password")

    def load_task_data(self):
        '''
        Loads each task from `task.txt` to the `task_list` attribute of
        _task_manager.

        '''
        task_list = []
        # Add each task (non-empty lines) from `tasks.txt` to a list.
        with open("tasks.txt", 'r') as task_file:
            task_data = task_file.read().split("\n")
            task_data = [t for t in task_data if t != ""]

        # Split each task into its components and append to `task_list`.
        for t_str in task_data:
            curr_t = {}

            task_components = t_str.split(";")
            curr_t['username'] = task_components[0]
            curr_t['title'] = task_components[1]
            curr_t['description'] = task_components[2]
            curr_t['due_date'] = datetime.strptime(task_components[3], DATETIME_STRING_FORMAT).date()
            curr_t['assigned_date'] = datetime.strptime(task_components[4], DATETIME_STRING_FORMAT).date()
            curr_t['completed'] = True if task_components[5] == "Yes" else False

            task_list.append(curr_t)

        self._task_manager.task_list = task_list

    def load_user_data(self):
        '''
        Loads each username and password from `users.txt` to the 
        username_password attribute of _task_manager.

        '''
        username_password = {}
        # Read in user_data.
        with open("user.txt", 'r') as user_file:
            user_data = user_file.read().split("\n")

        # Convert to a dictionary.
        for user in user_data:
            username, password = user.split(';')
            username_password[username] = password
            self._task_manager.username_password = username_password

class TaskSet:
    '''
    Various methods for determining and storing the properties of a
    set of tasks.

    Attributes:

    total (int):            Total number of tasks in the set.
    complete (int):         Number of tasks marked as "complete".
    incomplete (int):       Number of tasks marked as "incomplete".
    overdue (int):          Number of tasks marked as "overdue". 
    prc_incomplete (int):   Percentage of "incomplete" tasks. 
    prc_overdue (int):      Percentage of "overdue" tasks. 
    
    '''
    def __init__(self):
        self.total = 0
        self.complete = 0
        self.incomplete = 0
        self.overdue = 0
        self.prc_incomplete = 0
        self.prc_overdue = 0

    def add_task(self,t,curr_date):
        '''
        Adds the properties of an individual task to the set.

        Parameters: 
        t (dictionary):             A task.
        curr_date (DATE_TIME?):     Todays date.

        '''
        self.total += 1
        if t['completed'] == False:
            self.incomplete += 1
            if t['due_date'] < curr_date:
                self.overdue += 1

    def add_list(self,task_list,curr_date):
        '''
        Adds the properties of a list of tasks to the set.

        Parameters: 
        task_list (list):           A list of tasks.
        curr_date (DATE_TIME?):     Todays date.

        '''
        for t in task_list:
            self.add_task(t,curr_date)

    def calculate_properties(self):
        '''
        Calculate the remaining properties of the set of tasks.

        '''
        if self.total == 0:
            print("This set of tasks is empty.")
            return
        self.complete = self.total - self.incomplete
        self.prc_incomplete = self.incomplete/self.total
        self.prc_overdue = self.overdue/self.total

    def display_stats(self):
        '''
        Returns:
        dsp_str (str): A block of text containing the properties of the
        set of tasks.
        
        '''
        dsp_str = f"Total Tasks:\t\t\t\t\t\t{self.total}\n"
        dsp_str += f"Complete tasks:\t\t\t\t\t\t{self.complete}\n"
        dsp_str += f"Incomplete tasks:\t\t\t\t\t{self.incomplete}\n"
        dsp_str += f"Overdue tasks:\t\t\t\t\t\t{self.overdue}\n"
        dsp_str += f"Percentage of tasks incomplete:\t\t{int(self.prc_incomplete*100)}%\n"
        dsp_str += f"Percentage of tasks overdue:\t\t{int(self.prc_overdue*100)}%\n"
        return dsp_str


class MainMenu:
    '''Task manager core functions, menu display and user control.

    Contains the methods for the user to view and run the core
    functions of `task_manager.py`. The first set of methods are called
    by other methods/functions within this program. The second set of functions are selected by the user of the program to view, add and edit task and user properties. These properties are stored in an instance of the TaskManager class and in .txt files generated by the program.
    
    Attributes: 
    _task_manager (class):  Instance of TaskManager.
    functions (dict):       Contains the *callers* and descriptions of 
                            the functions selectable by the user.
    mm_str (str):           The string displaying the users' options at
                            the head of the main menu.
    
    '''
    def __init__(self,task_manager):
        self._task_manager = task_manager
        self.functions = {
            "r"  : [self.reg_user,
                    "Register a new user to the Task Manager."],
            "a"  : [self.add_task,
                    "Add a new task to the Task Manager."],
            "va" : [self.view_all,
                    "View all tasks in the Task Manager."],
            "vm" : [self.view_mine,
                    "View all tasks assigned to you."],
            "gr" : [self.generate_reports,
                    "Generate files containing the data stored in "
                    "the Task Manager."],
            "ds" : [self.display_stats,
                    "Display statistics about the tasks stored in "
                    "the Task Manager."],
            "e"  : [self.exit_program,"Exit the program."]
        }
        self.mm_str = ("Select one of the following options "
                              "below.\n")
        self.generate_mm_str()


    # Internal functions of this class (not called by the user):
        
    def generate_mm_str(self):
        '''
        Builds the string at the head of the main menu using the keys
        and descriptions in `self.functions`.

        '''
        for func in self.functions.keys():
            self.mm_str += f"{func}\t- {self.functions[func][1]}\n"
        self.mm_str += ": "

    def disp_full_task(self,t):
        '''Prints a block of text containing the properties of a task.

        Parameters:
        t (dictionary): A task.
        '''
        clear_term()
        disp_str = f"Task: \t\t{t['title']}\n"
        disp_str += f"Assigned to: \t{t['username']}\n"
        disp_str += f"Date Assigned: \t{t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        disp_str += f"Due Date: \t{t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
        # Bool -> 'Yes'/'No' string for readability in text.
        completed = "Yes" if t['completed'] == True else "No"
        disp_str += f"Task Complete? \t{completed}\n"
        disp_str += f"Task Description: \n {t['description']}\n"
        print(disp_str)  
    
    def get_due_date(self):
        '''Returns a correctly formatted due date from the user. 
        '''
        while True:
            try:
                task_due_date = input("Due date of task (YYYY-MM-DD): ")
                due_date = datetime.strptime(task_due_date, DATETIME_STRING_FORMAT).date()
                clear_term()
                return due_date
            except ValueError:
                clear_term()
                print("Invalid datetime format. Please use the format specified")

    def edit_date(self,i):
        '''Updates the due date assigned to a task with user input.

        Requests a date to be entered by the user and updates the due date of a task stored in task_manager. Applies this update to
        tasks.txt.

        Parameters:
        i (int): The index of the task to be updated in task_manager.task_list.
        '''
        clear_term()
        due_date = self.get_due_date()
        self._task_manager.task_list[i]['due_date'] = due_date
        print(f"The task's due date has been updated to {due_date}")
        self.update_task_db()

    def edit_username(self,i):
        '''Updates the username assigned to a task with user input.

        Updates the username assigned to a task if the text input by the user matches a username stored in task_manager. Applies this update to tasks.txt.

        Parameters:
        i (int): The index of the task to be updated in task_manager.task_list.
        '''
        new_username = input(
            "Enter a username to assign this task to: ")
        user_list = self._task_manager.username_password.keys()
        if new_username in user_list:
            self._task_manager.task_list[i]['username'] = new_username
            self.update_task_db()
            clear_term()
            print(f"Task reassigned to {new_username}.")
        else:
            print("The username entered does not exist.\n"
                  "Task not reassigned to another user.")
            
    def edit_task(self,i):
        usr_in = ""
        while usr_in not in ['d','u']:
            usr_in = input("Edit due date (d), or edit username (u): ").lower()
            if usr_in == 'd':
                self.edit_date(i)
            elif usr_in == 'u':
                self.edit_username(i)
            else:
                clear_term()
                print("Invalid input, try again.")

    def mark_complete(self,i):
        '''Marks a task as complete.
        
        Parameters:
        i (int): The index of the task to be updated in task_manager.task_list.
        '''
        clear_term()
        self._task_manager.task_list[i]['completed'] = True
        print("Task marked as complete!")

    def update_task_db(self):
        with open("tasks.txt", "w") as task_file:
            task_list_to_write = []
            for t in self._task_manager.task_list:
                str_attrs = [
                    t['username'],
                    t['title'],
                    t['description'],
                    t['due_date'].strftime(DATETIME_STRING_FORMAT),
                    t['assigned_date'].strftime(DATETIME_STRING_FORMAT),
                    "Yes" if t['completed'] else "No"
                ]
                task_list_to_write.append(";".join(str_attrs))
            task_file.write("\n".join(task_list_to_write))

    def function_select(self):
        '''Displays a menu of functions to the user that they can run.

        A list of functions and their descriptions (stored in this class) are printed to the terminal and the user is prompted to select one or exit the program. With a valid input, the terminal screen will be cleared and the desired function will run. Otherwise an error message will be displayed.
        '''
        user_input = input(self.mm_str).lower()
        clear_term()
        try:
            return self.functions[user_input][0]()
        except:
            print("Invalid input. Please try again.")
    
    
    # Core MainMenu functions called by the user:

    def reg_user(self):
        '''Adds a new user to user.txt.
        
        The user is prompted to enter a username. If it doesn't already exist in task_manager, then the user is prompted to enter and confirm a corresponding password. If the passwords entered by the user match, the username-password pair is added to the list (username_password) stored in task_manager and added to user.txt. 
        
        '''
        print("Register a new user.")

        new_username = input("New Username: ")

        if new_username in self._task_manager.username_password:
            print("Username already exists, please enter a " 
                "different one.")
            return

        new_password = input("New Password: ")

        confirm_password = input("Confirm Password: ")
        
        clear_term()
        # - Check if the new password and confirmed password are the same.
        if new_password == confirm_password:
            # - If they are the same, add them to the user.txt file.
            
            self._task_manager.username_password[new_username] = new_password
            
            with open("user.txt", "w") as out_file:
                user_data = []
                for k in self._task_manager.username_password:
                    user_data.append(f"{k};{self._task_manager.username_password[k]}")
                out_file.write("\n".join(user_data))
            print(f"Added a new user ({new_username}) to the database.")

        # - Otherwise you present a relevant message.
        else:
            print("Passwords do no match, user was not added to the database.")
            
    def add_task(self):
        '''Allows a user to add a new task to task.txt.
            
        Prompts a user for the following: 
            - A username of the person whom the task is assigned to.
            - A title of a task.
            - A description of the task.
            - The due date of the task.
        
        Updates task_manager and tasks.txt with the new task.
        '''
        print("Add a new task.")
        task_username = input("Name of person assigned to task: ")
        usernames = self._task_manager.username_password.keys()
        if task_username not in usernames:
            print("User does not exist. Please enter a valid username")
            return
        
        task_title = input("Title of Task: ")
        task_description = input("Description of Task: ")

        due_date = self.get_due_date()
    
        curr_date = date.today()

        new_task = {
            "username": task_username,
            "title": task_title,
            "description": task_description,
            "due_date": due_date,
            "assigned_date": curr_date,
            "completed": False
        }

        self._task_manager.task_list.append(new_task)
        self.update_task_db()
        clear_term()
        print("Task successfully added.")
    
    def view_all(self):
        '''Prints all tasks stored in task_manager in full.
        '''
        print("All tasks.")
        for t in self._task_manager.task_list:
            disp_str = f"Task: \t\t {t['title']}\n"
            disp_str += f"Assigned to: \t {t['username']}\n"
            disp_str += f"Date Assigned: \t {t['assigned_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Due Date: \t {t['due_date'].strftime(DATETIME_STRING_FORMAT)}\n"
            disp_str += f"Task Description: \n {t['description']}\n"
            print(disp_str)

    def view_mine(self):
        '''Display and edit the tasks of the current user.

        Displays the titles of all of the tasks assigned to the current user. A corresponding number is printed next to each task. The user can view the full details of any of these tasks by entering its number. They can then view another task or apply an action to the current task. Possible actions:
            - Mark the task as complete.
            - Assign the task to a different user.
            - Change the due date of the task. 

        Properties of the task can only be edited if the task is NOT complete. 
        The user can return to the main menu by entering '-1' or 'exit' at any time.
        '''
        curr_user = self._task_manager.curr_user
        while True:
            user_task_index = []
            index = 0
            counter = 0

            print(f"{curr_user}'s Tasks.\n")

            for t in self._task_manager.task_list:
                if t['username'] == curr_user:
                    disp_str = f"Task {counter + 1}: \t {t['title']}"
                    print(disp_str)
                    counter += 1
                    user_task_index.append(index)
                index += 1

            if counter == 0:
                print("\nUser has no tasks.")
                return
        
            # Select task
            task_no = input("\nSelect a task to view (e.g. type 1 for "
                            "Task 1) OR\n"
                            "Type -1 to return to the main menu: ")
            if task_no == "-1":
                clear_term()
                return
            try:
                task_no = int(task_no)
            except:
                clear_term()
                print("Invalid input.")
                continue

            if task_no < 1 or task_no > counter:
                clear_term()
                print("Invalid input.")
                continue
            else:
                task_list = self._task_manager.task_list
                # confusing line below
                curr_task = task_list[user_task_index[task_no - 1]]
                self.disp_full_task(curr_task)
                valid_input = True
            

            valid_input = False
            while valid_input != True:
                action = input("Mark task as complete (c) or edit task (edit): ").lower()
                if action in [-1,"exit"]:
                    return
                elif action == "c":
                    self.mark_complete(user_task_index[task_no - 1])
                    valid_input = True
                elif action == "edit":
                    if curr_task['completed'] == False:
                        self.edit_task(user_task_index[task_no - 1])
                    else:
                        clear_term()
                        print("This task is already complete so "
                              "cannot be edited.")
                    valid_input = True
                else:
                    print("Invalid input.")
        
        

    def generate_reports(self):
        '''Creates .txt files detailing the properties of task_manager.
        
        In this method, the properties of different sets of tasks are determined. 
            - The set of all tasks in task_manager.
            - Sets of tasks corresponding to each user stored in task_manager.

        The properties determined are as follows:
            - Total number of tasks in the set.
            - Number of tasks marked as "complete".
            - Number of tasks marked as "incomplete".
            - Number of tasks marked as "overdue". 
            - Percentage of "incomplete" tasks. 
            - Percentage of "overdue" tasks. 

        A unique instance of the TaskSet class is created for each set of tasks, where their properties are determined, stored and then converted to readable strings of text to be written to a
        .txt file.

        Two files are written, task_overview.txt and user_overview.txt.
        - task_overview:
            Displays the properties of all tasks in task_manager.
        - user_overview
            Displays the properties of each user in task_manager.    
        '''
        task_list = self._task_manager.task_list
        curr_date = date.today()

        # task_overview.txt
        all_tasks = TaskSet()
        all_tasks.add_list(task_list,curr_date)
        all_tasks.calculate_properties()
        with open("task_overview.txt", "w") as task_overview:
            dsp_str = "`task_manager.py` - Task Overview\n"
            dsp_str += "-----------------------------------------\n"
            dsp_str += all_tasks.display_stats() + "\n"
            task_overview.write(dsp_str)

        # user_overview.txt
        users = {}
        for t in task_list:
            if t['username'] not in users:
                users[t['username']] = TaskSet()
            users[t['username']].add_task(t,curr_date)

        with open("user_overview.txt","w") as user_overview:
            with open("tasks.txt", 'r') as task_f:
                num_tasks = sum(1 for _ in task_f)

            with open("user.txt", 'r') as user_f:
                num_users = sum(1 for _ in user_f)

            dsp_str = '`task_manager.py` - User Overview\n'
            dsp_str += "-----------------------------------------\n"
            dsp_str += f"Number of users: \t\t {num_users}\n"
            dsp_str += f"Number of tasks: \t\t {num_tasks}\n"
            dsp_str += '\n'
            user_overview.write(dsp_str)

            for u in users.keys():
                users[u].calculate_properties()
                dsp_str = "-----------------------------------------\n"
                dsp_str += f"{u}'s Stats:\n\n"
                dsp_str += users[u].display_stats()
                dsp_str += "\n"
                user_overview.write(dsp_str)
        
        print("Reports generated!")

    def display_stats(self):
        '''Displays the number of tasks and number of users.
        '''

        print("Task Manager Stats.")
        curr_user = self._task_manager.curr_user
        if curr_user == 'admin': 
            '''If the user is an admin they can display statistics about number of users
                and tasks.'''

            with open("tasks.txt", 'r') as task_f:
                num_tasks = sum(1 for _ in task_f)

            with open("user.txt", 'r') as user_f:
                num_users = sum(1 for _ in user_f)


            print("-----------------------------------")
            print(f"Number of users: \t\t {num_users}")
            print(f"Number of tasks: \t\t {num_tasks}")
            print("-----------------------------------") 
        else:
            print("Only the admin can run 'ds'.")

    def exit_program(self):
        clear_term()
        print("Writing files...")
        self.update_task_db()
        print("Exiting program...")
        return "exit"

        
    
    # def display_stats(self):
    #     curr_user = self._task_manager.curr_user
    #     username_password = self._task_manager.username_password
    #     task_list = self._task_manager.task_list
    #     if curr_user == 'admin': 
    #         '''If the user is an admin they can display statistics about number of users
    #             and tasks.'''
            
    #         num_users = len(username_password.keys())
    #         num_tasks = len(task_list)

    #         print("-----------------------------------")
    #         print(f"Number of users: \t\t {num_users}")
    #         print(f"Number of tasks: \t\t {num_tasks}")
    #         print("-----------------------------------") 
        

class TaskManager:
    '''Top level class containing a task manager program.
    
    Attributes:
    curr_user (str):            The user logged into the program.
    task_list (list(dict)):     All tasks stored in the program.
    username_password (dict):   All username + password pairs.
    logged_in (bool):           True when user is logged in.
    setup (object):             Generates .txt files and loads data.
    main_menu (object):         Main menu display and functions.

    When an instance of TaskManager is created, it calls methods of the setup class to configure the .txt files used by the program and load data from these files to `task_list` and `username_password`.
    '''
    def __init__(self):
        self.curr_user = ""
        self.task_list = []
        self.username_password = {}
        self.logged_in = False

        self.setup = Setup(self)
        self.main_menu = MainMenu(self)
        self.setup.config_txt_files()
        self.setup.load_task_data()
        self.setup.load_user_data()

    def login(self):
        '''Gets the user to login to the program.

        Request the user to input a username and password. Until a 
        valid username and password is entered, this function will loop.
        After a successful login attempt, `logged_in` becomes True.
        '''
        while not self.logged_in:
            print("Login.")
            curr_user = input("Username: ")
            curr_pass = input("Password: ")
            if curr_user not in self.username_password.keys():
                clear_term()
                print("User does not exist, try again.")
                continue
            elif self.username_password[curr_user] != curr_pass:
                clear_term()
                print("Wrong password, try again.")
                continue
            else:
                clear_term()
                print("Login Successful!")
                self.logged_in = True
                self.curr_user = curr_user
        
# Create the task_manager.
task_manager = TaskManager()

task_manager.login()

f_return = ""

'''Main loop of the program. The user selects and runs functions from
the main menu until they select the exit function, ending the program.
'''
while f_return != "exit":
    f_return = task_manager.main_menu.function_select()

    

