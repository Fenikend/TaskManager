import cmd
class MyCLI(cmd.Cmd):
    def precmd(self, line):
        print("Before command execution")
        return line  
    def do_add_task(self, line):
        i_beg=line.index('"')
        i_end=line.index('"',i_beg+1)
        print(f"Hello, {line[i_beg:i_end+1]}")

    def do_quit(self, line):
        """Exit the CLI.""" 
        return True
    

if __name__ == '__main__':
    MyCLI().cmdloop()