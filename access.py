>>> import os
>>> os.access('my_file', os.R_OK) # Check for read access
True
>>> os.access('my_file', os.W_OK) # Check for write access
True
>>> os.access('my_file', os.X_OK) # Check for execution access
False
>>> os.access('my_file', os.F_OK) # Check for existance of file
True