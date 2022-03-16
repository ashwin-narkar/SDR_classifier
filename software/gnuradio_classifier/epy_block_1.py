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

    def __init__(self, vlen=128, threshold=-40.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Vector Average',   # will show up in GRC
            in_sig=[(np.float32,vlen)],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.vlen = vlen
        self.thresh = threshold

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        inp = np.asarray(input_items[0])
        if (np.mean(inp) >= self.thresh):
            output_items[0][:] = 1
        else:
            output_items[0][:] = 0
        return len(output_items[0])
