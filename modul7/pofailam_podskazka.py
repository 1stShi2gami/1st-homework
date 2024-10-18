import os

print('Текущая дериктория',os.getcwd())
if os.path.exists('first'):
    os.chdir('first')
else:
    os.mkdir('first')
    os.chdir('first')
print('Текущая деректория:', os.getcwd())
os.chdir(r'E:\python projekts uu\pythonProject2.0\modul7')
print('Текущая деректория:', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(os.stat(file[7]))