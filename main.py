import cmd
import json
import sys
from time import asctime


class MyCmd(cmd.Cmd):
    def preloop(self):
        try:
            with open('tasks.json', 'r') as create_new:
                print('')
        except FileNotFoundError:
            create_new = open('tasks.json', 'w')

    prompt = '>>'
    intro = 'Welcome to my task tracker :)'

    def __init__(self):
        super().__init__()
        self.taskid = None
        self.n = 0
        self.task_dict = {}
        self.description = None

    #add a task and gives it an id
    def do_add(self, arg):
        self.n += 1
        self.task_dict.update({self.n: {'description': arg, 'status' : 'todo', 'createdAt': asctime(), 'updatedAt': 'not yet updated'}})
        with open('tasks.json', 'r+') as task_file:
            json.dump(self.task_dict, task_file)
        print('Task added successfully (ID: ' + str(self.n) + ')')

    def do_update(self, arg):
        words = arg.split(maxsplit=1)
        try:
            self.taskid = int(words[0])
            self.description = words[1]
        except ValueError:
            print('invalid task id, please try again')
            return
        self.task_dict[self.taskid]['description'] = self.description
        self.task_dict[self.taskid]['updatedAt'] = asctime()
        print('Task updated successfully (ID: ' + str(self.taskid) + ')')

    def do_mark_in_progress(self, ID):
        self.task_dict[int(ID)]['status'] = 'in_progress'
        print('Task updated successfully')

    def do_mark_done(self, ID):
        self.task_dict[int(ID)]['status'] = 'done'
        print('Task updated successfully')





    def do_list(self, arg):
        if arg == '':
            for task in self.task_dict:
                print(self.task_dict[task])

        elif arg == 'done':
            for task in self.task_dict:
                if self.task_dict[task]['status'] == 'done':
                    print(self.task_dict[int(task)])

        elif arg == 'in_progress':
            for task in self.task_dict:
                if self.task_dict[task]['status'] == 'in_progress':
                    print(self.task_dict[int(task)])
    def do_delete(self, ID):
        self.task_dict[int(ID)]['status'] = 'deleted'


    #quits the program
    @staticmethod
    def do_quit(self):
        print('Quitting')
        return True



if __name__ == '__main__':
    MyCmd().cmdloop()
