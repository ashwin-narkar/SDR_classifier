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
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import blocks
from gnuradio import filter
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
import epy_block_0
import epy_block_0_0
import epy_module_0  # embedded python module
import threading

from gnuradio import qtgui

class lstm_modelclassifier(gr.top_block, Qt.QWidget):

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

        self.settings = Qt.QSettings("GNU Radio", "lstm_modelclassifier")

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
        self.threshold = threshold = 0
        self.samp_rate = samp_rate = 20e6
        self.gain = gain = 0.75

        ##################################################
        # Blocks
        ##################################################
        self.avg_energy = blocks.probe_signal_f()
        def _threshold_probe():
            while True:

                val = self.avg_energy.level()
                try:
                    self.set_threshold(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _threshold_thread = threading.Thread(target=_threshold_probe)
        _threshold_thread.daemon = True
        _threshold_thread.start()

        self._gain_range = Range(0, 1, 0.01, 0.75, 200)
        self._gain_win = RangeWidget(self._gain_range, self.set_gain, 'gain', "counter_slider", float)
        self.top_layout.addWidget(self._gain_win)
        self.uhd_usrp_source_0 = uhd.usrp_source(
            ",".join(("serial=3186907", "")),
            uhd.stream_args(
                cpu_format="fc32",
                args='',
                channels=list(range(0,1)),
            ),
        )
        self.uhd_usrp_source_0.set_center_freq(2.4265e9, 0)
        self.uhd_usrp_source_0.set_normalized_gain(gain, 0)
        self.uhd_usrp_source_0.set_antenna('TX/RX', 0)
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_time_unknown_pps(uhd.time_spec())
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0 = qtgui.time_raster_sink_f(
            10e6,
            256,
            15,
            [],
            [],
            "Classification USRP 3186907",
            1
        )

        self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_update_time(0.10)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_intensity_range(0, 1)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0.enable_grid(False)
        self.qtgui_time_raster_sink_x_0_0_0_0_1_0.enable_axis_labels(True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [0, 0, 0, 0, 0,
            0, 0, 0, 0, 0]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_line_label(i, labels[i])
            self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_color_map(i, colors[i])
            self.qtgui_time_raster_sink_x_0_0_0_0_1_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_raster_sink_x_0_0_0_0_1_0_win = sip.wrapinstance(self.qtgui_time_raster_sink_x_0_0_0_0_1_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_raster_sink_x_0_0_0_0_1_0_win)
        self.qtgui_sink_x_0 = qtgui.sink_c(
            1024, #fftsize
            firdes.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate/2, #bw
            "", #name
            True, #plotfreq
            True, #plotwaterfall
            True, #plottime
            True #plotconst
        )
        self.qtgui_sink_x_0.set_update_time(1.0/10)
        self._qtgui_sink_x_0_win = sip.wrapinstance(self.qtgui_sink_x_0.pyqwidget(), Qt.QWidget)

        self.qtgui_sink_x_0.enable_rf_freq(False)

        self.top_layout.addWidget(self._qtgui_sink_x_0_win)
        self.qtgui_number_sink_1 = qtgui.number_sink(
            gr.sizeof_float,
            0,
            qtgui.NUM_GRAPH_HORIZ,
            1
        )
        self.qtgui_number_sink_1.set_update_time(0.10)
        self.qtgui_number_sink_1.set_title("")

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        units = ['', '', '', '', '',
            '', '', '', '', '']
        colors = [("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"),
            ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black"), ("black", "black")]
        factor = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]

        for i in range(1):
            self.qtgui_number_sink_1.set_min(i, -1)
            self.qtgui_number_sink_1.set_max(i, 1)
            self.qtgui_number_sink_1.set_color(i, colors[i][0], colors[i][1])
            if len(labels[i]) == 0:
                self.qtgui_number_sink_1.set_label(i, "Data {0}".format(i))
            else:
                self.qtgui_number_sink_1.set_label(i, labels[i])
            self.qtgui_number_sink_1.set_unit(i, units[i])
            self.qtgui_number_sink_1.set_factor(i, factor[i])

        self.qtgui_number_sink_1.enable_autoscale(False)
        self._qtgui_number_sink_1_win = sip.wrapinstance(self.qtgui_number_sink_1.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_number_sink_1_win)
        self.freq_xlating_fir_filter_xxx_0 = filter.freq_xlating_fir_filter_ccc(2, firdes.complex_band_pass(1, samp_rate, -samp_rate/(2), samp_rate/(2), 1e5), 2426.5e6, samp_rate)
        self.epy_block_0_0 = epy_block_0_0.blk(vlen=128)
        self.epy_block_0 = epy_block_0.blk(vlen=128)
        self.dnn_dnn_onnx_sync_0 = dnn.dnn_onnx_sync('/home/ashwin/Documents/Capstone/data/lstm_iq.onnx', 1, 'CPU')
        self.blocks_vector_to_stream_2_0_0_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 15)
        self.blocks_vector_to_stream_1_0 = blocks.vector_to_stream(gr.sizeof_float*1, 128)
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_float*1, 128)
        self.blocks_threshold_ff_0 = blocks.threshold_ff(-5, -4, 0)
        self.blocks_stream_to_vector_2 = blocks.stream_to_vector(gr.sizeof_float*1, 15)
        self.blocks_stream_to_vector_1 = blocks.stream_to_vector(gr.sizeof_gr_complex*1, 128)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, 256)
        self.blocks_nlog10_ff_0 = blocks.nlog10_ff(1, 1, 0)
        self.blocks_multiply_xx_0 = blocks.multiply_vff(15)
        self.blocks_moving_average_xx_0 = blocks.moving_average_cc(20, 1/20, 4000, 1)
        self.blocks_interleave_0 = blocks.interleave(gr.sizeof_float*1, 1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_float_0 = blocks.complex_to_float(128)
        self.analog_const_source_x_0 = analog.sig_source_f(0, analog.GR_CONST_WAVE, 0, 0, threshold)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_const_source_x_0, 0), (self.blocks_stream_to_vector_2, 0))
        self.connect((self.blocks_complex_to_float_0, 0), (self.epy_block_0, 0))
        self.connect((self.blocks_complex_to_float_0, 1), (self.epy_block_0_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_nlog10_ff_0, 0))
        self.connect((self.blocks_interleave_0, 0), (self.blocks_stream_to_vector_0, 0))
        self.connect((self.blocks_moving_average_xx_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_vector_to_stream_2_0_0_1_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.blocks_threshold_ff_0, 0))
        self.connect((self.blocks_nlog10_ff_0, 0), (self.qtgui_number_sink_1, 0))
        self.connect((self.blocks_stream_to_vector_0, 0), (self.dnn_dnn_onnx_sync_0, 0))
        self.connect((self.blocks_stream_to_vector_1, 0), (self.blocks_complex_to_float_0, 0))
        self.connect((self.blocks_stream_to_vector_2, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_threshold_ff_0, 0), (self.avg_energy, 0))
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_interleave_0, 0))
        self.connect((self.blocks_vector_to_stream_1_0, 0), (self.blocks_interleave_0, 1))
        self.connect((self.blocks_vector_to_stream_2_0_0_1_0, 0), (self.qtgui_time_raster_sink_x_0_0_0_0_1_0, 0))
        self.connect((self.dnn_dnn_onnx_sync_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.epy_block_0, 0), (self.blocks_vector_to_stream_1, 0))
        self.connect((self.epy_block_0_0, 0), (self.blocks_vector_to_stream_1_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_moving_average_xx_0, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.blocks_stream_to_vector_1, 0))
        self.connect((self.freq_xlating_fir_filter_xxx_0, 0), (self.qtgui_sink_x_0, 0))
        self.connect((self.uhd_usrp_source_0, 0), (self.freq_xlating_fir_filter_xxx_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "lstm_modelclassifier")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_threshold(self):
        return self.threshold

    def set_threshold(self, threshold):
        self.threshold = threshold
        self.analog_const_source_x_0.set_offset(self.threshold)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.freq_xlating_fir_filter_xxx_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, -self.samp_rate/(2), self.samp_rate/(2), 1e5))
        self.qtgui_sink_x_0.set_frequency_range(0, self.samp_rate/2)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

    def get_gain(self):
        return self.gain

    def set_gain(self, gain):
        self.gain = gain
        self.uhd_usrp_source_0.set_normalized_gain(self.gain, 0)





def main(top_block_cls=lstm_modelclassifier, options=None):

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
