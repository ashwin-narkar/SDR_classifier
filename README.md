# SDR-based Protocol Classification in a 2.4 GHz Frequency Band

## Abstract
In a typical 2.4 Ghz space, there are often many radio transmitters operating in different frequency bands using various modulation schemes and protocols. These transmitters can be categorized and localized with an SDR. This project aims to identify and categorize the protocols present in a 10 MHz band within the 2.4 GHz frequency space using an existing CNN and LSTM solution. In addition, the models categorize the protocols further into their respective channels for 3 different technologies: Wi-Fi, Bluetooth, and Zigbee. This project analyzes the real-world inference potentials for these models, in a typical household setting where there are numerous 2.4 GHz transmitters active at any given time. Using a USRP Ettus b205i-mini and GNU Radio, the SDR is used to collect samples in the sensing bandwidth, which are then fed into a trained model. Decoders for these technologies are also implemented using GNU Radio to test and verify performance of the model.

## Dependencies
Running this code requires GNU Radio 3.8 and the following OOT modules to be set up:
- gr-ieee802-11
- gr-foo
- gr-bluetooth
- gr-dnn
- gr-ieee802-15-4
 


## Code to Run

- CNN Training Code: software/RF_CNN_Classifier.ipynb (based on the code from here: https://github.com/dl4amc/dl4wii/)
- LSTM Training Code: software/RF_LSTM_Classifier.ipynb (based on the code from here: https://github.com/dl4amc/dl4wii/)
- Classifier: software/gnuradio_classifier/classifier.grc
- Wifi Scanner: (in the gr-ieee802-15 module), run examples/wifi_rx.grc
- Bluetooth Scanner: software/gnuradio_bluetooth/usinggrbluetooth.grc
