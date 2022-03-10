# Project Proposal

## 1. Motivation & Objective

What are you trying to do and why? (plain English without jargon)

In this project, I will be using a network of time synchronized Software Defined Radios to create a spatial radar-like system to collect information about an environment including radio sources as well as object detection that may be out of the visible range. The motivation comes from being able to use a system like this to monitor the capacity of a room or use it for security. For example, this could also be used in search and rescue to triangulate a radio source in a remote location with greater accuracy than GPS as the area where the system would be deployed is smaller, thus can detect the source with greater SNR. This technology can also be used to monitor heartbeat and breathing for a room with multiple people which can be useful in a hospital setting.

## 2. State of the Art & Its Limitations

Modern SDRs are used by amateur radio hobbyists and are very common. In a software defined radio (SDR), the motivation is that all the signal processing such as the demodulation is done in software rather than by dedicated hardware. This means that the only RF hardware needed is basically an A/D or D/A converter, an amplifier, and an antenna. This allows for greater flexibility of uses for the radio with a single unit. SDRs are heavily used in military and cellphone operations, where devices need to adapt to multiple different communication standards and protocols. SDRs are being used currently for spatial radar in areas in the military, security, and other scientific research fields. The flexibility of the approach allows for multiple antennas and receivers to be placed to allow for detection on a very wide spectrum.

## 3. Novelty & Rationale

I believe my approach is slightly different because it will eventually be used for object detection that would be outside of radio sources. I want to advance this project into a Masters capstone project, so while the class project might not cover this scope, I hope that eventually I am able to heartbeats and breathing in a room with multiple people. 

## 4. Potential Impact

This project, if successful, could be very useful in a security or medical field. If I can detect heartbeats and breathing in a room, it could be used to monitor multiple patients in a hospital with a single setup of distributed SDRs instead of potentially invasive individual monitors on patients. 

## 5. Challenges

There are significant challenges with this project, the first being to get GNU radio set up and running. Talking to some students in Professor Srivastava's lab, getting the GNU radio framework set up and working to transmit and receive signals is a challenge in itself to acheive in the time frame of the class. That is why the intial goal of my project is limited to being able to triangulate a radio source in 2D. The future setup for wireless detection of heartbeats and breathing will require a different set of skills with finding datasets and a model that will help us detect heartbeat and breathing from the radios transmitting and receiving signals. 

## 6. Requirements for Success

Because this project uses SDRs where all the signal processing is done in software, a signficant amount of knowledge of signal processing and communication systems will be needed. Getting GNU radio setup will be another challenge that is more on the software side. Once I move on to the breathing and heartbeat detection, I will require various forms of existing data to train a model to help detect breathing and heartbeat. In terms of resources, I currently am using 2 SDRs and 2 antennas in the 2.4-5 Ghz range to help me detect a cellphone and triangulate its location. This frequency range will allow me to detect wifi and cellular data.

## 7. Metrics of Success

For the scope of this class, the metric for success is to be able to detect presense of a cellphone or radio source and be able to triangulate that radio source's location. For the larger scope of the capstone project, my goal will be to achieve wireless detection of heartbeat and breathing so that I can detect the pulse and breathing rate of an individual.

## 8. Execution Plan

Describe the key tasks in executing your project, and in case of team project describe how will you partition the tasks.

The first main task in my project will be to get GNU radio set up and running on the B205 Mini-i SDRs that I borrowed from the lab. Once I have that successfully setup, I plan to have one transmit and one receive to make sure that these to radios are able to communicate with each other. Once that is successful, the goal will be to work on getting the location of my cellphone in a line of sight between the 2 time synchronized SDRs along a line

If that is succesful, I will get a 3rd SDR and do the triangulation in a 2d plane.

## 9. Related Work

### 9.a. Papers

List the key papers that you have identified relating to your project idea, and describe how they related to your project. Provide references (with full citation in the References section below).

Wireless breathing detection: http://eprints.gla.ac.uk/225797/
    This paper discusses how the researchers were able to use a SDR and the channel state information to detect the movements caused by breathing on a single human subject

SDR Radar: https://corescholar.libraries.wright.edu/etd_all/91/
    This paper discusses what different parameters to create an effective SDR based radar using GNU radio

UAV Triangulation of CellPhone for Search and Rescue: https://digital.wpi.edu/concern/student_works/gb19f842x
    This paper discusses how a Unmanned Aerial Vehicle (UAV) with an SDR could be used to detect a cell phone signal by finding its direction and using the orientation of the UAV itself.


### 9.b. Datasets

I will be searching for datasets in the latter half of the project for my capstone.

### 9.c. Software

I will be using the GNU Radio open source framework for my SDRs. This framework contains different blocks for common communication protocols such as bluetooth and wifi. This will make the implementation of detecting a cellular source much simpler as I will not need to do all the signal processing from scratch. This will allow me to make full use of the SDRs flexibility for detecting radio sources.

## 10. References

GNU Radio Setup: https://kb.ettus.com/Building_and_Installing_the_USRP_Open-Source_Toolchain_(UHD_and_GNU_Radio)_on_Linux


