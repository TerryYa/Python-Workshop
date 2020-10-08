import os

members = []

black_list = ['img', 'src']

for path in os.listdir(f'.'):
    if os.path.isdir(path) and (path not in black_list):
        for m in members:
            target = os.path.join(path, m)
            if not os.path.isdir(target):
                os.mkdir(target)
