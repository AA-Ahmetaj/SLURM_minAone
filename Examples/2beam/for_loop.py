import os, shutil

start_point = int(input("Please enter the start point:"))
end_point= int(input("Please enter the end point:"))
step_size = int(input("Please enter the step size:"))
for i in range(start_point+step_size, end_point,step_size):
    os.mkdir("r=%s,r=%s,r=%s" %(start_point,i, end_point))
    file_1_name = ("B1_ICFC_N%s_%s_%s.txt" %(start_point,i, end_point))
    file_2_name= ("B2_ICFC_N%s_%s_%s.txt" %(start_point,i, end_point))
    r_1_file = open("B1_ICFC_N50001.txt","r")
    r_2_file = open("B2_ICFC_N50001.txt","r")
    list_of_lines_1 = r_1_file.readlines()
    list_of_lines_2 = r_2_file.readlines()
    for a in range(0,50001):
        list_of_lines_1[a] = "0.000000000000000000e+00\n"
        a+=1
    for a in range(0,50001):
        list_of_lines_2[a] = "0.000000000000000000e+00\n"
        a+=1
    list_of_lines_1[start_point-1] = list_of_lines_2[start_point-1] = "1.000000000000000000e+00\n"
    list_of_lines_1[end_point-1] = list_of_lines_2[end_point-1] = "1.000000000000000000e+00\n"
    list_of_lines_1[i-1] = list_of_lines_2[i-1] = "1.000000000000000000e+00\n"
    w_1_files = open(file_1_name, "w")
    w_2_files = open(file_2_name, "w")
    w_1_files.writelines(list_of_lines_1)
    w_2_files.writelines(list_of_lines_2)
    w_1_files.close()
    w_2_files.close()
    shutil.move(file_1_name, "r=%s,r=%s,r=%s" %(start_point,i, end_point))
    shutil.move(file_2_name, "r=%s,r=%s,r=%s" %(start_point,i, end_point))
    sr_1_file = open("specs.txt","r")
    slist_of_lines_1 = sr_1_file.readlines()
    slist_of_lines_1[7] = ("./B1_ICFC_N%s_%s_%s.txt\n" %(start_point,i, end_point))
    slist_of_lines_1[8] = ("./B2_ICFC_N%s_%s_%s.txt\n" %(start_point,i, end_point))
    sw_1_files = open("specs.txt", "w")
    sw_1_files.writelines(slist_of_lines_1)
    sw_1_files.close()
   
    list_of_necessary_files = ["sim_.txt","Sophia_fft_code_1.py","Sophia_fft_code_2.py","Sophia_fft_code_3.py","Sophia_fft_code_4.py","Sophia_fft_code_5.py","Sophia_fft_code_6.py","IC_generate_code.ipynb","Mary_visualization_code.py","makecppAone.py","makehppAone.py","makemakeAone.py","makeoptAone.py","discAone.py","minAone.py","P1z_.txt","P2z_.txt","equations.txt","submit.sbatch","specs.txt","times_N50001.txt"]
    for f in list_of_necessary_files:
        shutil.copy(f,"r=%s,r=%s,r=%s" %(start_point,i, end_point))

    
    
