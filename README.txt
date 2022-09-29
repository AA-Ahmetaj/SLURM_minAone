This repository contains information on how to run the minAone packages on a SLURM-HPC cluster using batch scripts.
All the examples contained in this repo are run by following this list of instructions:
       1) Run the forward integration code
       2) Compile the minAone python scripts
       3) Submit the optimization task as a batch job
       4) Visualize the results
FOR A DETAILED LIST OF INSTRUCTIONS ON HOW TO RUN THESE JOBS, PLEASE REFER TO THE “EXAMPLES” DIRECTORY.
The “slurm_hpc_guideline.pdf” contains a general introduction to SLURM-HPC, a list of SLURM commands and instructions on how to create a Jupyter Notebook on a SLURM-HPC cluster.
The userguide_minaone contains information on the minAone packages and instructions on how to write the equations, specs and injection files needed for these annealing procedures to work.
The "submit.sbatch" script is used submit the annealing procedure as a computational job on a SLURM-HPC cluster. this file contains extensive comments for each line so that later change of any task parameter will seem feasible.
all the minAone scripts mentioned on this repository have been created by jingxin et al, and can be found at
 https://github.com/yejingxin/minAone .

