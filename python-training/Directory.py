import os

print(os.getcwd())
print(os.getcwdb())

os.chdir(r'C:\\Users\\user\Desktop\\python-training')
print(os.listdir())
os.mkdir('Test', exist_ok=True)
os.rename('Test', 'New_One')
