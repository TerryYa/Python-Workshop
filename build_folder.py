import os

members = [
    'Mehtab Khalil', 'Akeem Peters', 'Tyler Eck', '蕭芯儀', '劉沛妮', '黃柊森', 'Astrid Adhipurusa', '黃瀅芳', '陳冠銘', '方傑', 'Sasa Tarzn', 'Jason Yeh', '熊亭媛', 'Leon Wang', '何昀軒', '王津峰', 'Ly Shen', '譚宇翔']

black_list = ['img', 'oj', 'src']

for path in os.listdir(f'.'):
    if os.path.isdir(path) and (path not in black_list):
        for m in members:
            target = os.path.join(path, m)
            if not os.path.isdir(target):
                os.mkdir(target)
