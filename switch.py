

with open('./path.txt','r') as file:
    path = file.readlines()

path = path[0]


path1 = path + '/config.ini'
path2 = path + '/Genshin Impact Game/config.ini'

lines_offi = ['cps=mihoyo\n','channel=1\n','sub_channel=2\n',
              'channel=1\n','cps=mihoyo\n','sub_channel=2\n']

lines_bili = ['cps=bilibili\n','channel=14\n','sub_channel=1\n',
              'channel=14\n','cps=bilibili\n','sub_channel=1\n']

flag = input()
if flag == 'g':
    lines_re = lines_offi

elif flag == 'b':
    lines_re = lines_bili


with open(path1,'r') as file:
  lines = file.readlines()
  
lines[2] = lines_re[0]
lines[3] = lines_re[1]
lines[4] = lines_re[2]

with open(path1, 'w') as file:  
    file.writelines(lines)


with open(path2,'r') as file:
  lines = file.readlines()

lines[1] = lines_re[3]
lines[2] = lines_re[4]
lines[4] = lines_re[5]

with open(path2, 'w') as file:  
    file.writelines(lines)
