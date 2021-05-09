# JavaBuilder.py
# Compile and run java files from sublime in the command prompt

# Modified: 05/03/2021
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
            return path, file_name
            
        def get_file(path):
            """Gets the name of the file without extension"""
            file_name_ext = path[-1]
            file = file_name_ext.split(".")
            file_name = file[0]
            return file_name

        def directory_cmd(path):
            """Create the change directory command"""
            current_driver = path[0]
            current_directory = "/".join(path)
            change_directory = "cd " + current_directory + " & " + current_driver
            return change_directory, current_driver

        def create_bat(change_directory, file_name):
            """Creates a batch file containing the commands to compile and run the Java file"""
            commands = open(os.path.dirname(__file__) + '/../commands.bat', "w+")
            commands.write("@echo off\n"
                            + change_directory
                            + "\njavac " + file_name + ".java"
                            + "\nstart cmd /k java " + file_name
                            )
            commands.close() 

        def run_bat():
            """Runs the batch file that was created"""
            batchfile = os.path.dirname(__file__) + '/../commands.bat'
            subprocess.call([r'{}'.format(batchfile)])
            os.remove(os.path.dirname(__file__) + '/../commands.bat')

        def main(self):
            """Main routine"""
            path, file_name = get_path(self)
            change_directory, current_driver = directory_cmd(path)
            create_bat(change_directory, file_name)
            run_bat()
            
        main(self)
