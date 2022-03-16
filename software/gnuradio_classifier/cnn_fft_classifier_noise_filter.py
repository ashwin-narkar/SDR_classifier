#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Not titled yet
# Author: ashwin
# GNU Radio version: 3.8.5.0

from distutils.version import StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
import sip
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import filter
from gnuradio.filter import firdes
from gnuradio import gr
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
from gnuradio import uhd
import time
from gnuradio.qtgui import Range, RangeWidget
import dnn
import onnxruntime
import epy_block_0_0_0
import epy_block_0_1

from gnuradio import qtgui

class cnn_fft_classifier_noise_filter(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Not titled yet")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Not titled yet")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "cnn_fft_classifier_noise_filter")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 10e6
        self.gain = gain = 0.75

        ##################################################
        # Blocks
        ##################################################
        self._gain_range = Range(0, 1, 0.01, 0.75, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, 'gain', "counter_slider", float)
        self.top_layout.addWidget(self._gain_win)
        self.uhd_usrp_source_0_0 = uhd.usrp_source(
            ",".join(("serial=3186907", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0_0.set_center_freq(2.4265e9, 0)
        self.uhd_usrp_source_0_0.set_normalized_gain(gain, 0)
        self.uhd_usrp_source_0_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0_0.set_time_unknown_pps(uhd.time_spec())
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0 = qtgui.time_raster_sink_f(
            10e6,
            256,
            15,
            [],
            [],
            "Classification USRP 3186907",
            1
        )

        self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_intensity_range(0, 1)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0_win)
        self.freq_xlating_fir_filter_xxx_0_0 = filter.freq_xlating_fir_filter_ccc(1, firdes.complex_band_pass(1, samp_rate, -5e6, 5e6, 1e5), 2426.5e6, samp_rate)
        self.fft_vxx_0_0 = fft.fft_vcc(128, True, window.blackmanharris(128), False, 1)
        self.epy_block_0_1 = epy_block_0_1.blk(vlen=128)
        self.epy_block_0_0_0 = epy_block_0_0_0.blk(vlen=128)
        self.dnn_dnn_onnx_sync_0_0 = dnn.dnn_onnx_sync('/home/ashwin/Documents/Capstone/data/fft_model.onnx', 1, 'CPU')
        self.blocks_vector_to_stream_2_0_0_1_0_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 15)
        self.blocks_vector_to_stream_1_1 = blocks.vector_to_stream(gr.sizeof_float*1, 128)
        self.blocks_vector_to_stream_1_0_0 = blocks.vector_to_stream(gr.sizeof_float*1, 128)
        self.blocks_stream_to_vector_1_0 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 128)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, 256)
        self.blocks_interleave_0_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_complex_to_float_0_0 = blocks.complex_to_float(128)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_float_0_0, 1), (self.epy_block_0_0_0, 0))
        self.connect((self.blocks_complex_to_float_0_0, 0), (self.epy_block_0_1, 0))
        self.connect((self.blocks_interleave_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.dnn_dnn_onnx_sync_0_0, 0))
        self.connect((self.blocks_stream_to_vector_1_0, 0), (self.fft_vxx_0_0, 0))
        self.connect((self.blocks_vector_to_stream_1_0_0, 0), (self.blocks_interleave_0_0, 1))
        self.connect((self.blocks_vector_to_stream_1_1, 0), (self.blocks_interleave_0_0, 0))
        self.connect((self.blocks_vector_to_stream_2_0_0_1_0_0_0, 0), (self.qtgui_time_raster_sink_x_0_0_0_0_1_0_0_0, 0))
        self.connect((self.dnn_dnn_onnx_sync_0_0, 0), (self.blocks_vector_to_stream_2_0_0_1_0_0_0, 0))
        self.connect((self.epy_block_0_0_0, 0), (self.blocks_vector_to_stream_1_0_0, 0))
        self.connect((self.epy_block_0_1, 0), (self.blocks_vector_to_stream_1_1, 0))
        self.connect((self.fft_vxx_0_0, 0), (self.blocks_complex_to_float_0_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0_0, 0), (self.blocks_stream_to_vector_1_0, 0))
        self.connect((self.uhd_usrp_source_0_0, 0), (self.freq_xlating_fir_filter_xxx_0_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "cnn_fft_classifier_noise_filter")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, -5e6, 5e6, 1e5))
        self.uhd_usrp_source_0_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0_0.set_normalized_gain(self.gain, 0)





def main(top_block_cls=cnn_fft_classifier_noise_filter, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    def quitting():
        tb.stop()
        tb.wait()

    qapp.aboutToQuit.connect(quitting)
    qapp.exec_()

if __name__ == '__main__':
    main()
