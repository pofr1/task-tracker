import cmd
import json
class MyCmd(cmd.Cmd):
    def prcmd(self, line):
        with open('tasks.json', 'r') as tasks_file:
            tasks = json.load(tasks_file)
        return line

    prompt = '>>'
    intro = 'Welcome to my task tracker :)'
    def __init__(self):
        super().__init__()
        self.n = 0
        self.tasks = []
        self.task_dict = {}
    #add a task and gives it an id
    def do_add(self, arg):
        self.n += 1
        self.task_dict.update({self.n: arg})

        print('Task added successfully (ID: '+ str(self.n)+')')


    #quits the program
    def do_quit(self):
        print('Quitting')
        return True
if __name__ == '__main__':
    MyCmd().cmdloop()