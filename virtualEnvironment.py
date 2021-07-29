'''
The command that creates a virtual environment has the following structure:
 python -m venv virtual-environment-name
'''

'''
You are now going to create a virtual environment inside the flasky directory. A com‐
monly used convention for virtual environments is to call them venv, but you can use
a different name if you prefer. Make sure your current directory is set to flasky, and
then run this command:
 python -m venv venv
'''

'''
When you want to start using a virtual environment, you have to “activate” it:
 venv\Scripts\activate

When a virtual environment is activated, the location of its Python interpreter is
added to the PATH environment variable in your current command session, which
determines where to look for executable files

After a virtual environment is activated, typing python at the command prompt will
invoke the interpreter from the virtual environment instead of the system-wide inter‐
preter. If you are using more than one command prompt window, you have to acti‐
vate the virtual environment in each of them.


'''

'''
While activating a virtual environment is usually the most conve‐
nient option, you can also use a virtual environment without acti‐
vating it.:
 venv\Scripts\python

When you are done working with the virtual environment, type deactivate at the
command prompt to restore the PATH environment variable for your terminal session
and the command prompt to their original states.
'''