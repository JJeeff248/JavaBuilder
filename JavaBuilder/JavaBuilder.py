# JavaBuilder.py
# Compile and run java files from sublime in the command prompt

# Modified: 18/01/2020
# Created: 15/01/2020
# By JJeeff248

import subprocess, sublime_plugin, os, sublime

class JavabuilderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for view in self.view.window().views():
            view.run_command('save')

        def get_path(self):
            """Get the current file path"""
            file_path = self.view.file_name() # C:\users\..\file.java
            path = file_path.split("\\")
            file_name = get_file(path)
            path.pop()
            startup = directory_cmd(path)
            create_bat(startup, file_name)
            
        def get_file(path):
            """Gets the name of the file without extension"""
            file_name_ext = path[-1]
            file = file_name_ext.split(".")
            file_name = file[0]
            return file_name

        def directory_cmd(path):
            """Create directory command"""
            current_driver = path[0]
            current_directory = "\\".join(path)
            startup = "cd " + current_directory + " & " + current_driver
            return startup
            
        def create_bat(startup, file_name):
            """Create batch file"""
            commands = open(os.path.dirname(__file__) + '/../commands.bat', "w+")
            commands.write(startup+"\njavac "+file_name+".java \ncls\njava "+file_name+"\npause")
            commands.close()

        def run_bat():
            batchfile = os.path.dirname(__file__) + '/../commands.bat'
            subprocess.call([r'{}'.format(batchfile)])
            os.remove(os.path.dirname(__file__) + '/../commands.bat')

        get_path(self)
        run_bat()
