import filecmp
import os
import subprocess as sp

file1 = "/Users/gautham/Music/abc.txt"
file2 = "/Users/gautham/Movies/abc.txt"
final_res = filecmp.cmp(file1, file2,shallow=False)
print(final_res)

if final_res == False:
    sp.run(f"rm -r {file1}",shell=True)
    os.chdir("/Users/gautham/Movies/")
    sp.run(f"cp -r abc.txt /Users/gautham/Music/",shell=True)
    sp.run("cat /Users/gautham/Music/abc.txt",shell=True)
else:
    pass
    
