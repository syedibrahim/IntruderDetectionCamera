# Intelligent-facial-recognition-system-for-surveillance-and-Intruder-Detection

**Pre-requisites:**
1. Follow these steps to setup Twilio Account and get your <br>
   twilio ID and Auth-Token, along with twilio phone Number <br>
   [Click Here](https://www.twilio.com/docs/sms/quickstart/python)
2. Follow the instructions and add the above mentioned details in <br>
   send_sms.py that is already created.
3. Follow instructions given in **PyImageSearch** to install Opencv <br>
   on Raspberry PI [Click Here](https://www.pyimagesearch.com/2019/09/16/install-opencv-4-on-raspberry-pi-4-and-raspbian-buster/)
4. Additionally use **pip** to install dlib and numpy

**To run the program:**
1. Clone this repository
   
2. Run **Main.py** file <br>
   `python main.py`
3. To save new face encoding <br>
   `python save_new_face.py -f image.jpg -n "ibrahim"` <br>
                     OR<br>
   `python save_new_face.py -f image.png -n "ibrahim"`
