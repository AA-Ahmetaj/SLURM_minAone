IN ORDER TO RUN THIS EXPERIMENT:
1)Log in to your cluster account.
2)Upload the current git repo to your account by first downloading it your computer and then uploading it using the instructions on this file""https://github.com/AA-Ahmetaj/SLURM_minAone/blob/main/SLURM_HPC_guideline.pdf".
3)Open a jupyter notebook on your cluster account using the instructions mentioned on "https://github.com/AA-Ahmetaj/SLURM_minAone/blob/main/SLURM_HPC_guideline.pdf"
4)Open "forward_integration.ipynb" and run all the cells using Jupyter Notebook
5)Open a new terminal window and log into your cluster account again.
6)Navigate to the directory where this experiment is located:
7)Run the following commands on your terminal in order to run the optimization procedure:
                   a)python minAone.py
                   b)make
                   c)./neutrinos.cpp
                   d)sbatch submit.sbatch
8) Lastly plot the results by running "plotting_code.ipynb" on your Jupyter Notebook.
