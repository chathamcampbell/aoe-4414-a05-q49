# full_ops
#
# Usage: python3 full_ops.py c_in n_wv
#  Determine the output shape and operation count of a pooling layer
# Parameters:
# c_in: input channel count 
# n_wv: number of weight vectors

# Output:
# A description of the script output
# c_out: output channel count
# h_out: output height count
# w_out: output width count
# adds: number of additions performed
# muls: number of multiplications performed
# divs: number of divisions performed
#
# Written by Chatham Campbell
# Other contributors: None
#

# import Python modules

import sys # argv
import math

#initialize script arguments
c_in = float('nan') 
n_wv = float('nan')

#parse script arguments
if len(sys.argv)==3:
  c_in = int(sys.argv[1])
  n_wv = int(sys.argv[2])
else:
  print(\
   'Usage: '\
   'python3 full_ops.py c_in n_wv'
  )
  exit()

# write script below this line

c_out = n_wv
h_out = 1
w_out = 1

adds = n_wv*c_in
muls = n_wv*c_in
divs = 0


print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
#python3 full_ops.py 120 84