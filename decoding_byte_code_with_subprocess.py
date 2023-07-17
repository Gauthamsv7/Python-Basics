import subprocess as sp

res = sp.run(["host","8.8.8.8"],capture_output=True)
#print(res)
#print(res.returncode)
#print(res.stdout)
'''
Now Converting Byte Code to UTF-8
'''

res_modified = res.stdout.decode().split()
print(res_modified[1])


'''

Knowing about the STD ERR : it will take the error and warning and will store it

'''

removing_file = sp.run(["rm", "adipurush_file_as_it_donot_exits"],capture_output=True)
#print(removing_file)
#print(removing_file.stdout)
#print(removing_file.stderr)

