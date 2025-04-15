#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -o result.log
#SBATCH -e result.err
#SBATCH --gpus 1

source .venv/bin/activate && python main.py
