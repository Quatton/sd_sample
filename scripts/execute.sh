wait() {
  sbatch $1
  trap $2 INT
  while true; do squeue; sleep 1; clear; done
}

wait job.sh
