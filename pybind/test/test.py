import sys, os, json

import montecarlopi

if __name__ == '__main__':
    reps = int(1e8)
    estimate = montecarlopi.pi(reps)
    print(f"The Monte Carlo estimate for pi with {reps} samples is [{estimate}]")


