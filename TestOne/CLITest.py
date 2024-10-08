import cmd
from jsonTest import *
class MyCLI(cmd.Cmd):
    jsonCheck()
    jsonData=readJsonData()
    ids=list()
    for items in jsonData['Tasks']:
        ids.append(items['id'])  

    prompt = '>> '
    intro = '''
    list of commands:
    add id "descr"- to add task
    update id "descr" - to update task need id
    delete id - to delete task
    mark_done id - mark tsk as done 
    mark_in_progress id - mark tsk as in progress
    list status - to show tasks if status empty return all of them 
    status(done,todo,in-progress)
    '''

    def do_add(self, line):
        if line == '':
            return 0

        i_beg=line.index('"')
        i_end=line.index('"',i_beg+1)
        task_descr=line[i_beg+1:i_end]
        addItem(ids,task_descr)
        writeJsonData(jsonData)
        print(f"Task added: {task_descr}")
    
    def do_delete(self,line):
        user_input_id=line.partition(' ')[0]
        deleteItem(jsonData,user_input_id)
        writeJsonData(jsonData)

    
    def do_update(self,line):
        if line == '':
            return 0
        try:
            i_beg=line.index('"')
            i_end=line.index('"',i_beg+1)
            int(task_id=line[:i_beg])
        except ValueError:
            print('Try again line is invalid')
            return 0
        except TypeError:
            print('Try again id is invalid')
            return 0
        i_beg=line.index('"')
        i_end=line.index('"',i_beg+1)
        task_descr=line[i_beg+1:i_end]
        task_id=line[:i_beg]
        task_id=task_id.replace(' ', '')
        updateItem(jsonData,task_id,task_descr)
        writeJsonData(jsonData)

    def do_list(self,line):
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
    
    def do_mark_done(self,line):
        try:
            int(line)
        except TypeError:
            print('Id is not exist')
        markTask(jsonData,line,'done')
        writeJsonData(jsonData)

    def do_mark_in_progress(self,line):
        markTask(jsonData,line,'in-progress')
        writeJsonData(jsonData)


    def do_quit(self, line):
        """Exit the CLI.""" 
        return True
    

if __name__ == '__main__':
    MyCLI().cmdloop()
  
