#%%
#!/usr/bin/env python3

import os

files = os.listdir(".")

for file in files:
    re_ = r"notebooks_Block_\d_Jupyter\ Notebook Block\ \d\ -\ "
    filename_new = re.sub(re_, "", file)
    
    re_ = r"notebooks_Block_\d_Solutions\ to\ Exercises\ Block\ \d\ -\ "
    filename_new = re.sub(re_, "", filename_new)
    
    re_ = r"notebooks_Block_\d_Exercises Block\ \d\ -\ "
    filename_new = re.sub(re_, "", filename_new)    

    re_ = r"notebooks_Block_\d_Solutions to Exercises\ -\ "
    filename_new = re.sub(re_, "", filename_new)    

    try:
        print('Old file name is: ', file, '\nNew file name is: ', filename_new,'\n')
        os.rename(file, filename_new)
    except:
        print(e)

# %%

