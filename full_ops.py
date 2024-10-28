# full_ops.py
#
# Usage: python3 full_ops.py c_in n_wv
# This script calculates the output shape and operation count of a fully-connected layer.
# Parameters:
# c_in: input channel count (number of input features)
# n_wv: number of weight vectors (number of neurons in the fully-connected layer)
# Output:
# The script prints the following values:
# - Output channel count
# - Output height count
# - Output width count
# - Number of additions performed
# - Number of multiplications performed
# - Number of divisions performed
#
# Written by Michael Hoffman
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

import sys

# Parse script arguments
if len(sys.argv) != 3:
    print('Usage: python3 full_ops.py c_in n_wv')
    sys.exit(1)

c_in = int(sys.argv[1])
n_wv = int(sys.argv[2])

# Calculate output dimensions
c_out = n_wv
h_out = 1
w_out = 1

# Calculate the number of operations
muls = c_in * n_wv
adds = muls - n_wv
divs = 0

# Print the results
print(int(c_out))  # output channel count
print(int(h_out))  # output height count
print(int(w_out))  # output width count
print(int(adds))   # number of additions performed
print(int(muls))   # number of multiplications performed
print(int(divs))   # number of divisions performed
