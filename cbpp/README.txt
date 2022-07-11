
please read me carefully


why is the project name called 'cbpp'?
    'cbpp' means 'Create a Basic Python Project'.

# basic usage:
The tool is to create a simple Python working directory quickly, you can use it by following command:
$: python pyp.py [project_name] [project_dir]
** it need to be noticed that the first argument [project_name] is required,  but the second argument 
[project_dir] can be default and if you do not provide it, the project will be created in the current path.

# advanced usage:
You can customize self-Python-Working-Dir relying on needs.
The tool can create a Python-Working-Dir like this:
---- root(your project name) [dir]
    ---- core [dir] # the key codes of project should be put here
    ---- tools [dir] # the frequent funtions can be added here
    ---- data [dir] # the data operated should be put here
    ---- results [dir] # the executing results can be put here
    ---- log [dir] # some significant information of executing process can be added here
    ---- main.py [file] # the common enter of project
    ---- configs.py [file] # the default global configrations file for project

If you want to change or add some [sub_dir], you just need do some modification in the './cbpp/configs.py',
you will see a list variable named 'BAISC_DIRS' in this file, and you just need to modify this vairable, add new one or change name that you want.

If you want to change or add some [sub_file], you just need do some modification in the './cbpp/configs.py',
you will see a list variable named 'BAISC_FILES' in this file, and you just need to modify this vairable, add new one or change name that you want.
** Noticed: if you have some template files according your coding style, you just put them into './abpp/templates/' and add its name to 
'./abpp/configs.py/BAISC_FILES'.



