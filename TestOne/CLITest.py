import cmd
from jsonTest import *
class MyCLI(cmd.Cmd):
    jsonCheck()
    jsonData=readJsonData()
    ids=list()
    for items in jsonData['Tasks']:
        ids.append(items['id'])  

    prompt = '>> '
    intro = 'Welcome to task manager ClI'
    def precmd(self, line):
        print("Before command execution")
        return line


    def do_add_task(self, line):
        if line == '':
            return 0
        
        i_beg=line.index('"')
        i_end=line.index('"',i_beg+1)
        task_descr=line[i_beg+1:i_end]
        # task_id=line[:i_beg]
        addItem(ids,task_descr)
        writeJsonData(jsonData)
        # print(jsonData)
    
    def do_delete(self,line):
        user_input_id=line.partition(' ')[0]
        #user_input_line=line.partition(' ')[2]
        deleteItem(jsonData,user_input_id)
        writeJsonData(jsonData)
       #pass
    
    def do_update(self,line):
        if line == '':
            return 0
        i_beg=line.index('"')
        i_end=line.index('"',i_beg+1)
        task_descr=line[i_beg+1:i_end]
        task_id=line[:i_beg]
        task_id=task_id.replace(" ", "")
        updateItem(jsonData,task_id,task_descr)
        writeJsonData(jsonData)
        #update 1 "do the dishes" 

    def do_line(self,line):
        line=line.replace(' ','')
        match line:
            case 'done':
                listTasks(jsonData,'done')
            case 'todo':
                listTasks(jsonData,'todo')
            case 'in-progress':
                listTasks(jsonData,'in-progress') 
            case '':
                listTasks(jsonData,'') 
            case _:
                print('something wrong')    


    def do_quit(self, line):
        """Exit the CLI.""" 
        return True
    

if __name__ == '__main__':
    MyCLI().cmdloop()
  