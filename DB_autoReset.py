import os
import glob
TeamSQL_DIR = "."
Api_DIR = "."
Migration_file_name = "."

def del_migration_files(path, file_name):
    for name in glob.glob(path):
        if name = filename:
            return complete_path = path + filename
        else:
            print ('cannot find the file specified')
            os._exit()




print('====================================================')
print('This script is used to simplify the DB-reset process')
print('====================================================')

original_dir = os.getcwd()
print("The original directory is %s", original_dir)

os.chdir(Api_DIR)
os.system()
os.chdir(TeamSQL_DIR)