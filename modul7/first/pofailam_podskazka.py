import os

print('Текущая дериктория',os.getcwd())
if os.path.exists(''):
    os.chdir('')
else:
    os.mkdir('')
    os.chdir('')
print('Текущая деректория:', os.getcwd())
os.chdir(r'/modul7')
print('Текущая деректория:', os.getcwd())
file = [f for f in os.listdir() if os.path.isfile(f)]
dirs = [d for d in os.listdir() if os.path.isdir(d)]
print(os.stat(file[7]))