IN ORDER TO RUN THIS EXPERIMENT:
1)Open a jupyter notebook on your cluster account using the instructions mentioned on "https://github.com/AA-Ahmetaj/SLURM_minAone/blob/main/SLURM_HPC_guideline.pdf"
2)Open "forward_integration.ipynb" and run all the cells using Jupyter Notebook
3)Then run the following commands on your terminal in order to run the optimization procedure:
                   a)python minAone.py
                   b)make
                   c)./neutrinos.cpp
                   d)sbatch submit.sbatch
