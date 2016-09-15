
from time import time
import os
start = time()
x = os.popen('./ltp-3.3.2/bin/examples/cws_cmdline --input input --threads 10 | ./ltp-3.3.2/bin/examples/pos_cmdline --threads 4 | ./ltp-3.3.2/bin/examples/par_cmdline --threads 4').read()
#m = x.communicate()
#n = y.communicate()
#l = z.communicate()
print(x)
end = time()
print(end-start)
