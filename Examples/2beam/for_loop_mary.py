import os
import string
current_cwd = os.getcwd()
for i in os.listdir():
    if i.startswith("r="):
    	for file in os.listdir(i):
    		if file.startswith("Mary_visualization_code") or file.startswith("Sophia_fft_code"): 
    			os.system("cd %s/%s \npython %s" %(current_cwd,i,file))
    
