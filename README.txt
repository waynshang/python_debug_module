This is a package to print log with color

Step 
1: pip install debuggerModule
2: from debugger import getLogger
3: DEBUG = getLogger()
4: DEBUG.INFO("log")

There are five different type
1. logging.DEBUG: green
2. logging.INFO: blue
3. logging.WARNING: yellow
4. logging.ERROR: red
5. logging.CRITICAL: bold_red