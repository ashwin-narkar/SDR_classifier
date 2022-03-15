# SDR-based Protocol Classification in a 2.4 GHz Frequency Band

## Abstract
In a typical 2.4 Ghz space, there are often many radio transmitters operating in different frequency bands using various modulation schemes and protocols. These transmitters can be categorized and localized with an SDR. This project aims to identify and categorize 2.4 Ghz transmitters by their protocol and store the current identifiable devices that have been detected. The system will detect the active transmitting devices and remember recent devices if they begin transmitting again.

## Dependencies
Running this code requires GNU Radio 3.8 and the following OOT modules to be set up:
  -gr-ieee802-11
  -gr-foo
  -gr-bluetooth
  -gr-dnn
  -gr-ieee802-15-4
 


## Code to Run


-Classifier: software/gnuradio_classifier/classifier.grc
-Wifi Scanner: (in the gr-ieee802-15 module), run examples/wifi_rx.grc
-Bluetooth Scanner: software/gnuradio_bluetooth/usinggrbluetooth.grc
