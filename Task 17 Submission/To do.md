- [ ] When editing a task/marking as complete, go back to the start of the view mine function.
	- Current issue: When returning to the start of view_mine after editing a task (particularly the username edit), do I want it to recreate the user_tasks_index every time? That would seem quite slow. But that's really an optimisation for later. The main problem is HOW do I return to the start of the function from the end of the function. I mean I can just put it in a while loop for now.
	- [x] Quick fix using while loop.
	- [ ] Find a way of making the while loop more readable.
	- [ ] After core functionality is done come back to this to optimise.
- [x] Start the next function in the assignment doc
- [x] Completed the logic for the `generate_reports()` function, now just need to turn it into a txt file.
- [x] Sort out when the txt files are written. Have a function that updates these files and call it whenever it is needed. E.g. when exiting the program.
- [x] `display_stats` ... Display it straight from the txt file??
- [x] Make the `function_select` more modular:
	- [x] In the `functions` dictionary, each key should also have a description value as well as pointing to the function.
	- [x] Line 144 update the input string so that it uses the keys and descriptions from the `functions` dictionary
- [x] Line 155 and 157... what is the point of `"continue"` and `"exit"`? Get rid of them?
- [x] `view_mine`
	- [x]  When displaying a task, show if it is complete or not. 
	- [x] If task is complete, remove the option to edit the task.
	- [x] Update the labels for the inputs (`c`,`m`,`edit`,`exit` etc...)
	- [x] Clear the screen and add input messages for `edit_date`, `edit_username` and `mark_complete` line 128.
	- [x] Also check both of these for valid inputs.
		- [x] Check for valid date.
		- [x] When updating a tasks user, check that the user exists.
- [x] Add an update txt files function.
- [ ] 33r434r33
- [ ] 



### TO do part 2:
- [x] Make sure duplicate users cannot be added to user.txt
- [ ] vm:
	- [x] Each task is displayed in a nice way and has a number to identify them.
	- [x] -1 to return to main menu
		- [x] Screen should be cleared when returning to MM
	- [x] User should be able to edit or mark task as complete
	- [x] Task marked as complete should say 'Yes/No' instead of 'True/False'
	- [x] Split edit task into two options, assignment OR due date.
- [ ] Check gr is in the menu
	- [ ] task_overview.txt should contain:
		- [x] The total number of tasks that have been generated and tracked using the task_manager.py.
		- [x] The total number of completed tasks.
		- [x] The total number of uncompleted tasks.
		- [x] The total number of tasks that haven’t been completed and that are overdue.
		- [x] The percentage of tasks that are incomplete.
		- [x] The percentage of tasks that are overdue.
	- [x] user_overview.txt should contain:
		- [x] The total number of users registered with task_manager.py.
		- [x] The total number of tasks that have been generated and tracked using task_manager.py.
		- [x] For each user also describe:
			- [x] The total number of tasks assigned to that user.
			- [x] The percentage of the total number of tasks that have been assigned to that user
			- [x] The percentage of the tasks assigned to that user that have been completed
			- [x] The percentage of the tasks assigned to that user that must still be completed
			- [x] The percentage of the tasks assigned to that user that has not yet been completed and are overdue
- [x] Modify the menu option that allows the admin to display statistics so that the reports generated are read from tasks.txt and user.txt and displayed on the screen in a user-friendly manner. If these text files don’t exist (because the user hasn’t selected to generate them yet), first call the code to generate the text files.



Strong software development fundamentals will be highly useful in this role. Many of the different departments within the Graduate scheme will use code in their projects, e.g. Automation, Software Engineering and Data/Analytics. HyperionDev's course will enable me to produce my own code and work on important projects from day one. I have improved my ability to understand code written by other people, meaning I will be able to learn from my peers' work quickly and excel in this fast paced environment. In such a large business, many different people would need to understand, test and build upon my work. It is vital that I am able to write code that is not only functional and efficient, but also clearly structured and well documented. I have learned how to write clean and readable code on this course, which could lead to my contributions being utilized in successful projects, also allowing me to receive accurate feedback to further improve my skills and boost my career in technology.