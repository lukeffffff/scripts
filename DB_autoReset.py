import os

TeamSQL_DIR = ""

print('====================================================')
print('This script is used to simplify the DB-reset process')
print('====================================================')

original_dir = os.getcwd()
print("The original directory is %s", original_dir)
os.chdir(TeamSQL_DIR)