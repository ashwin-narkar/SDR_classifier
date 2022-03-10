"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, vlen=15, thresh = 1):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Embedded Python Block',   # will show up in GRC
            in_sig=[(np.float32,vlen),(np.float32,vlen)],
            out_sig=[(np.float32,vlen)]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.thres = thresh

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        # input_items[i] is ith input vector
        # input_items[i][0] is the actual vector itself with 15 elements to address

        for i in range(15):
            if (1/self.thres) <= input_items[0][0][i] / input_items[1][0][i] <= self.thres:
                output_items[0][0][i] = max(input_items[0][0][i],input_items[1][0][i])
            else:
                output_items[0][0][i] = 0

        return len(output_items[0])
