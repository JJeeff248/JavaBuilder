# JavaBuilder.py
# Compile and run java files from sublime in the command prompt

# Modified: 16/01/2020
# Created: 15/01/2020
# By JJeeff248

import subprocess, sublime_plugin, os

class JavabuilderCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        file_path=self.view.file_name() # C:\users\..\file.java
        path = file_path.split("\\")

        # Gets the name of the file without extension
        file_name_ext = path[-1]
        file = file_name_ext.split(".")
        file_name = file[0]

        # Create directory command
        current_driver=path[0]
        path.pop()
        current_directory="\\".join(path)
        startup= "cd "+current_directory
        
        # Create batch file
        commands = open(os.path.dirname(__file__) + '/../commands.bat', "w+")
        commands.write(startup+"\njavac "+file_name+".java \njava "+file_name+"\npause")
        commands.close()

        batchfile = os.path.dirname(__file__) + '/../commands.bat'

        subprocess.call([r'{}'.format(batchfile)])

        os.remove(os.path.dirname(__file__) + '/../commands.bat')


