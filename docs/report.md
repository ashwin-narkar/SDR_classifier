# Table of Contents
* Abstract
* [Introduction](#1-introduction)
* [Related Work](#2-related-work)
* [Technical Approach](#3-technical-approach)
* [Evaluation and Results](#4-evaluation-and-results)
* [Discussion and Conclusions](#5-discussion-and-conclusions)
* [References](#6-references)

# Abstract

This project attempts to use software defined radios to create a detector of Wifi and Bluetooth signals. I have used this project as the first part to a larger project which will use the detection of these signals within a network of SDRs to be able to locate the radio source that is emitting the Wifi or Bluetooth signal.

# 1. Introduction

## Motivation & Objective: 
    In this project, I will be using a network of time synchronized Software Defined Radios to create a spatial radar-like system to collect information about an environment including radio sources as well as object detection that may be out of the visible range. The motivation comes from being able to use a system like this to monitor the capacity of a room or use it for security. For example, this could also be used in search and rescue to triangulate a radio source in a remote location with greater accuracy than GPS as the area where the system would be deployed is smaller, thus can detect the source with greater SNR. This technology can also be used to monitor heartbeat and breathing for a room with multiple people which can be useful in a hospital setting.

## State of the Art & Its Limitations
Modern SDRs are used by amateur radio hobbyists and are very common. In a software defined radio (SDR), the motivation is that all the signal processing such as the demodulation is done in software rather than by dedicated hardware. This means that the only RF hardware needed is basically an A/D or D/A converter, an amplifier, and an antenna. This allows for greater flexibility of uses for the radio with a single unit. SDRs are heavily used in military and cellphone operations, where devices need to adapt to multiple different communication standards and protocols. SDRs are being used currently for spatial radar in areas in the military, security, and other scientific research fields. The flexibility of the approach allows for multiple antennas and receivers to be placed to allow for detection on a very wide spectrum.

## Novelty & Rationale: What is new in your approach and why do you think it will be successful?
I believe my approach is slightly different because it will eventually be used for object detection that would be outside of radio sources. I want to advance this project into a Masters capstone project, so while the class project might not cover this scope, I hope that eventually I am able to heartbeats and breathing in a room with multiple people. 

## Potential Impact
This project, if successful, could be very useful in a security or medical field. If I can detect heartbeats and breathing in a room, it could be used to monitor multiple patients in a hospital with a single setup of distributed SDRs instead of potentially invasive individual monitors on patients. 

## Challenges

There were significant challenges with this part of the project, the first being to get GNU radio set up and running. Talking to some students in Professor Srivastava's lab, getting the GNU radio framework set up and working to transmit and receive signals is a challenge in itself to acheive in the time frame of the class. The original goal of this first part was to be able to locate signals in 2d. However, the challenges and background information I needed to ramp up with GNURadio and telecommunication systems was signficant. I was able to create a detector for wifi and bluetooth. The future setup for wireless detection of heartbeats and breathing will require a different set of skills with finding datasets and a model that will help us detect heartbeat and breathing from the radios transmitting and receiving signals. 

## Requirements for Success

Because this project uses SDRs where all the signal processing is done in software, a signficant amount of knowledge of signal processing and communication systems will be needed. Getting GNU radio setup will be another challenge that is more on the software side. Once I move on to triangulation of an unknown radio source, I will require various forms of existing data to train a model to facilitate AMC (automatic modulation classification) so that I can detect an unkown source. For detecting heartbeats and breathing, I will require other datasets to detect changes in the Wifi channel estimate. In terms of resources, I currently am using 2 SDRs and 2 antennas in the 2.4-5 Ghz range to help me detect Wifi and Bluetooth signals. This frequency range allows me to detect the full wifi and bluetooth band.

## Metrics of Success

For the scope of this class, the metric for success is to be able to detect presense of a Wifi or Bluetooth signal using a single SDR. For the larger scope of the capstone project, my goal will be to triangulate the location of an unknown radio source in the 2.4 Ghz band.

# 2. Related Work

## 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

Wireless breathing detection: http://eprints.gla.ac.uk/225797/
    This paper discusses how the researchers were able to use a SDR and the channel state information to detect the movements caused by breathing on a single human subject

SDR Radar: https://corescholar.libraries.wright.edu/etd_all/91/
    This paper discusses what different parameters to create an effective SDR based radar using GNU radio

UAV Triangulation of CellPhone for Search and Rescue: https://digital.wpi.edu/concern/student_works/gb19f842x
    This paper discusses how a Unmanned Aerial Vehicle (UAV) with an SDR could be used to detect a cell phone signal by finding its direction and using the orientation of the UAV itself.


## 9.b. Datasets

I will be searching for datasets in the latter half of the project for my capstone.

## 9.c. Software

I will be using the GNU Radio open source framework for my SDRs. This framework contains different blocks for common communication protocols such as bluetooth and wifi. This will make the implementation of detecting a cellular source much simpler as I will not need to do all the signal processing from scratch. This will allow me to make full use of the SDRs flexibility for detecting radio sources.

# 3. Technical Approach

## Wifi Specification

Wifi is defined as the IEEE 802.11 wireless networking protocols. It has evolved from its inception to the point where IEEE 802.11 is a family of different protocols. It uses the 2.4GHz band and the 5Ghz band to transmit data. It uses Orthogonal Frequency Division Multiplexing to achieve a higher bandwidth were the channel is divided into subchannels and data is sent on each of these. I will be focusing on the 802.11g protocol, which operates in the 2.4Ghz band, along with Bluetooth and many other devices. In the 802.11g protocol, there are 11 overlapping channels that are 22Mhz apart. Due to the overlap, only 3 channels are used in the US, channels 1, 6, and 11 at 2.412 Ghz, 2.437 Ghz, and 2.462 Ghz center frequencies respectively. Wifi also uses adaptive modulation, so each of these carriers can use BPSK, QPSK, 16-QAM, or 64-QAM to send signals. To receive real wifi signals, the receiver must sample at 20Mhz and does an FFT. 
Each Wifi frame begins with a preamble sequence there is used to synchronize the transmitter and receiver. These sequences are different based on the different types of modulation and versions of 802.11 being used. In 802.11g, preamble consists of a short training field and a long training field each with 2 symbols. The short training field repeats over 16. The short field is used for initial timing and frequency synchronization, while the long field is used for channel estimation as well. The preamble also contains signal information that defines the data rate and size of packet to receive. This defines the modulation scheme and data rate to be used when sending packets. 

## Bluetooth Specification
Like 802.11g, Bluetooth also works in the 2.4Ghz frequency band. Bluetooth occupies an 80 Mhz bandwidth in this range, with 80 channels of 1Mhz bandwidth each. Bluetooth uses the frequency hopping spread spectrum (FHSS) approach, where transmission constantly hops between channels at a rate of 1600 hops per second. On each channel, symbols are transmitted using Gaussian Frequency Shift Keying, which is a variation of traditionally FSK. The data rate for Bluetooth is defined as 1 Mbps, where there is 1 bit per symbol.

## USRP Ettus B205i Mini
This is the software defined radio that I have used for this project. It interfaces well with GNU radio through the UHD driver that I installed. This setup was quite involved, where I had to update libraries, define environment variables, and debug the setup process. I was lucky to have a Linux machine, so I did not need to use any virtualization software or the Windows Subsystem for Linux when I was working on my project. This SDR has a bandwidth of around 50 Mhz and transmits over USB 3.09 for fairly high data rates. It has a wide frequency range from 70 MHz to 6 GHz.

## GNU Radio

For this project, I used GNU radio which is an open source framework for developing SDRs and other radio projects. GNU Radio works with flowgraphs, which have blocks that have various functions. This flowgraph is then converted to a coding language of your choice, in my case Python. GNU Radio also has modules that you can create yourself to accommodate different protocols. For my project, I used the gr-ieee802-11 module to facilitate detection and recognition of Wifi signals. This package includes a sample Wifi transceiver, that can be used to send data packets between 2 SDRs. It is recommended that this example be used as a test. For my project, I then used the receiver part of the example, and had to modify some receiver parameters to be able to detect actual Wifi frames that were send in my house on the 2.4Ghz band. The module also includes blocks that are able to decode the MAC frames, which was extremely useful for debugging the output and testing validity.
For the Wifi receiver, it takes advantage of the reptition in the Wifi synchronization signals to detect that a signal has been sent. The short wifi preamble sequence is 16 symbols long and repeats 10 times. By creating a delay of 16 and finding the autocorrelation, we are able to detect a wifi frame. We then equalize the frame using the channel estimate, at which point we can decode the symbols in a packet and find the mac frame.


For the Bluetooth receiver, the USRP has a bandwith of 50MHz, so we are not able to sniff the entire 80 MHz bandwidth of the Bluetooth protocol. However, we can use 2 USRPs to scan the entire Bluetooth range. In my case, I chose to scan one channel at a time, since the hopping occurs fairly often. For the Bluetooth detection, there is a library called gr-bluetooth with modules to help assist with the decoding of Bluetooth signals, however there is almost 0 documentation on how to use this library. I did not have the time to figure out how to use this library to decode Bluetooth signals, however I was able to down convert signals in the Bluetooth band and see the demodulated constellation diagram. I used a frequency translating FIR filter, which brings the center frequency down to 0 Mhz, and captures the 1MHz boundary around it. This helps me capture the single Bluetooth channel that I wish to scan. I then use a squelcher block, to only pass the signal through when the power is past certain threshold, that I found -70 db to be a good threshold to use. Then, I pass it through a GFSK demodulator to see the signal. I also look at a constellation diagram to see the signals being sent. I used this is a way to verify that I was indeed detecting Bluetooth signals. My immediate next step is to figure out how to use the burst tagger block to facilitate pulse detection for a Bluetooth signal so that I can detect the start of a Bluetooth signal. Then, I hope to be able to figure out how to use gr-bluetooth to decode packets, starting with advertisement packets, which are limited to only 3 channels in Bluetooth.


# 4. Evaluation and Results

This project was extremely challenging for me, as I had very little background in the actual RF space. In the timeframe that I had (around 5-6 weeks), I struggled to ramp up my knowledge of RF and communication systems to a level where I felt comfortable playing with GNU radio. In addition, setting up and using the GNU radio software was extremely challenging. I found very little documentation and tutorials for those beginning to enter GNU radio. Most of the tutorials and discussions online are through a very niche community of radio enthusiasts, using technical jargon that is difficult to easily research. In addition, being extremely busy with classes this quarter led me to reduce the scope of my project from locating a radio source to simply detecting presence of Wifi and Bluetooth signals. 
Next quarter, as I expand this project to my masters capstone, I hope to spend more time getting help from the lab so that I can be more comfortable working with GNU radio and figuring out how to locate devices using a pair of networked SDRs. 
For my results, I was able to successfully use the gr-ieee802_11 module to detect wifi signals in my apartment in the 2.4 GHz range. I primarily used the example wifi receiver in the gr-ieee802_11 module to facilitate this. Before I began, I tested the functionality using the wifi_tx and wifi_rx flowgraphs that are included as examples in the module. I also took quite a lot of time to understand the way these flowgraphs work in GNU radio and how the different modules interact. I was able to have my 2 SDRs transmit and receive using this, at which point I moved onto attempting to detect wifi frames on my network.
[show tx and rx receiver and transmitter constellation diagram]
The challenge here was that I had to sample at 20 MHz to receive these real signals, which caused significant overflows in the USRP with all the processing being done. I played with simple storing the raw signal in a file with one flowgraph, and then doing all the processing in another flowgraph at a later time to reduce the processing that needed to be done. This helped in reducing the frequency of the overflows, however I also found that reducing the amount of GUI widgets also helped to reduce the overflow rate. Printing the MAC output was extremely useful in being able to see the beacon frames being sent out that were advertising my local network. 

In the Bluetooth scanner module, I had less success in decoding the actual Bluetooth frames, because I did not have enough time to figure out how the gr-bluetooth module worked. I also attempted to manually decode this, however my inexperience in GNUradio led to this taking too long. I did not have enough time this quarter to fully implement the Bluetooth receiver, however I hope that next quarter I am able to implement this functionality.


# 5. Discussion and Conclusions
As mentioned before, time and inexperience as a significant factor in the limitations of my project at its current state. I had a fairly large scope because I want to extend this to a masters capstone project. I still want to keep this scope, as next quarter, I will dedicate all my time to this capstone project as I will have no classes. Working on this project by myself this quarter was extremely challenging. The lack of documentation and simple training material for GNU Radio made it a very steep learning curve for me in a field where I had little experience. In the beginning, I barely knew what each of the GNU radio blocks did functionally in the real world. For example, the power squelch block in GNU radio was something I did not even know existed. There was little documentation about the functionality other than the explanation of parameters. I had to do my own research about what a squelch circuit is in radio communications. I did not even know such a circuit existed, and I had to do a significant amount of research through papers to see that it could be used to stamp out noise. 
For next steps, I want to use Automatic Modulation Classification to identify the modulation scheme used in a raw radio signal. This can then be used to make a more informed decision about which protocol is being used in the 2.4 GHz range, as there are many. I want to focus on localization of Wifi and Bluetooth signals, as these are fairly common signals that advertise their presence and are common on most smartphones. In a search and rescue setting, a smartphone that has wifi or Bluetooth enabled would be constantly advertising its presence or searching for a Wifi signal and give a reply. This is where simulating a Wifi transmitter could be useful. The Bluetooth signal would always be advertised as the phone is discoverable.
I also want to move this project to use more machine learning techniques. I want to use the channel estimate information from Wifi to decipher information about a scene. There are currently research papers that have used this approach, and I want to build off of it, so that I can use a single application that can either locate signals or use channel estimate information from a discovered wifi signal to decipher information about the scene.  

# 6. References

GNU Radio Setup: https://kb.ettus.com/Building_and_Installing_the_USRP_Open-Source_Toolchain_(UHD_and_GNU_Radio)_on_Linux
Gr-ieee802_11: https://github.com/bastibl/gr-ieee802-11
Detecting Wi-Fi and Bluetooth signals using SDR: http://www.koreascience.or.kr/article/JAKO202120461903891.page
IEEE 802.11g Standard: https://www.electronics-notes.com/articles/connectivity/wifi-ieee-802-11/802-11g.php
Bluetooth Physical Layer: https://www.rfwireless-world.com/Tutorials/Bluetooth-physical-layer.html
GNU Radio Tutorials: https://wiki.gnuradio.org/index.php/Tutorials
