import os

schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory",
                },
            },
        },
    },
}


def get_files_info(working_directory: str, directory: str = ".") -> str:
	try:
		working_dir_abs = os.path.abspath(working_directory)
		target_dir=os.path.normpath(os.path.join(working_dir_abs, directory))
		valid_target_dir=os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs
		if not valid_target_dir:
			return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
		if not os.path.isdir(target_dir):
			return f'Error: "{directory}" is not a directory'
		if directory == ".":
			header="Result for current directory:"
		else:
			header="Result for '{directory}' directory:"
		lines=[header]
		for item in os.listdir(target_dir):
			item_path=os.path.join(target_dir, item)
			is_dir=os.path.isdir(item_path)
			size=os.path.getsize(item_path)
			lines.append(f" - {item}: file_size={size} bytes, is_dir={is_dir}")
		return "\n".join(lines)
#return f'Success: "{directory}" is within the working directory'
	except Exception as e:
		return f"Error: {str(e)}"
#We need to give our agent the ability to do stuff. We'll start by allowing it to list the contents of a directory and see each file's metadata (name and size).

#Before we integrate this function with our LLM agent, let's just build the function itself. Now remember, LLMs work with text, so our end goal with this function is for it to accept a directory path and return a string that represents the contents of that directory.

#But the first step is the most important: making sure the requested directory is safely inside the working directory that we allow the agent to use.

#Assignment
#Make a new directory called functions in the root of your project (not within the calculator directory). Inside, create a new file called get_files_info.py. Start writing the following function there:

#def get_files_info(working_directory: str, directory: str = ".") -> str:

#For reference, here's my project structure so far:#

#project_root/
#├── calculator/
#│   ├── main.py
#│   ├── pkg/
#│   │   ├── calculator.py
#│   │   └── render.py
#│   └── tests.py
#└── functions/
#    └── get_files_info.py

#The key idea is that the directory parameter will be treated as a relative path within the working_directory. We'll allow the LLM agent to specify which directory it wants to scan, but the working_directory will be set by us. This means we can limit the scope of directories and files that the LLM is able to view.

#Begin implementing the get_files_info function. First we need to validate that the path to the directory is inside the working_directory.

#Construct the full path to the target directory by calling os.path.join() with the absolute working_directory and the directory argument. To protect against shenanigans, also make sure to call os.path.normpath() on the combined path. This will handle things like "..", turning the path into its true form. The calls should look something like this:
#target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

#Now check if target_dir falls within the absolute working_directory path. The safest way of doing this is to use os.path.commonpath(), which finds the longest sub-path shared by two paths. For example, if the working directory is "/home/steve/ai-agent-project/calculator" and the target directory is "/home/steve/ai-agent-project/calculator/pkg", then the common path will be "/home/steve/ai-agent-project/calculator". That is, the common path should be the same as the absolute working directory path – if the target directory is valid. You could code this expectation like so:
# Will be True or False
#valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

#If the target directory does not fall within the working directory, return an error string in the following format:
#f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

#Now our LLM agent has some guardrails: we never want it to be able to perform any work outside the working_directory that we give it.

#]Without this restriction, the LLM might run amok anywhere on the machine, reading sensitive files or overwriting important data. This is a very important step that we'll bake into every function the LLM can call.

#If the directory argument is not a directory, again, return an error string:

#f'Error: "{directory}" is not a directory'

#All of our "tool call" functions, including get_files_info, should always return a string. If errors can be raised inside them, we need to catch those errors and return a string describing the error instead. This will allow the LLM to handle errors gracefully.

#If the target directory is valid, return a success string:

#f'Success: "{directory}" is within the working directory'

#If any errors are raised by the standard library functions that you call, catch them and instead return a string describing the error. You may find it convenient to put everything in this function in a try/except block. When returning an error string, always prefix it with Error:.

#We need a way to manually debug our new get_files_info function! Create a new test_get_files_info.py file in the root of your project. When executed directly (uv run test_get_files_info.py) it should run these function calls and print their results:

#To import from a subdirectory, use this syntax: from DIRNAME.FILENAME import FUNCTION_NAME

#Where DIRNAME is the name of the subdirectory, FILENAME is the name of the file without the .py extension, and FUNCTION_NAME is the name of the function you want to import.

