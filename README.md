1 What is SOL4Py <br>
</b>
</font>

<font size=2>
<b>1.1 SOL4Py</b>
<br>
SOL4Py is a tiny Python class library for Python, PyQt, OpenCV, and ML.<br> 
The basic class design of SOL4Py is based on that of our SOL9 C++ library.  
 In order to develop our library, we have used the latest Python3.6, PyQt5, and OpenCV-4.2.0 on Windows 10 Version 1903.
We have tested the sample programs on Windows 10 only, but you may run them on Linux environment too, provided you install required Python, 
PyQt, OpenCV modules on Linux. <br>
<br>
<br>
To develop SOL4Py library, we created a virtual environment tflow for tensorflow and installed the following libraries on <a href="https://www.python.org/downloads/windows/">python 3.6.5 (Windows x86-64 executable installer)</a>
 Prompt of Windows10 Version 1903.<br>
<br>
<table style="border: 1px solid red;">

<tr><td>
<font size=2>
; 20200224 Modified to use python 3.6.5 (64-bit) instead of Anaconda3.<br>
; Create a virtual env tflow<br>
python -m venv tflow<br>
cd tflow<br>
scripts/activate<br>
<br>
pip install opencv-python<br>
pip install PyQt5<br>
pip install pandas<br>
pip install matplotlib<br>
pip install seaborn<br>
pip install pydotplus<br>
pip install qimage2ndarray<br>
pip install sklearn<br>
pip install xgboost<br>
pip install LightGBM<br>
<font color="red">
;2020/02/24 Modified to install tensorflow==1.5.0<br>
pip install tensorflow==1.5.0<br>
</font>
pip install keras==2.2.4<br>
pip install cx_Oracle<br>
pip install pydot<br>
pip install PyOpenGL<br>
pip install graphviz<br>
<font color="red">
; https://github.com/pytorch/pytorch/issues/19406<br>
pip install torch==1.2.0+cpu torchvision==0.4.2+cpu -f https://download.pytorch.org/whl/torch_stable.html<br>
</font>
pip install pycryptodome<br>
pip install mysql-connector-python<br>
; 20200224 Maybe you have to install pillow version like this<br>
; to avoid ImportError: cannot import name 'PILLOW_VERSION'<br>
pip install pillow==6.2.1<br>
;To avoid Future warning, pip install numpy==1.16.0<br>
pip install numpy==1.16.0<br>
</font>
</table>

<br>
<br>
<b>YOLOv3:<br></b>
We have downloaded <a href="https://github.com/qqwweee/keras-yolo3">keras-yolo3</a>, 
which is a python binding of <a href="https://pjreddie.com/darknet/yolo/">YOLO: Real-Time Object Detection</a>,
and built a runtime-environment keras-yolo3 under SOL4Py-2 folder.<br><br>
See a sample program <a href="http://www.antillia.com/sol4py/samples/keras-yolo3/YoloObjectDetector.html">YoloObjectDetector</a> to detect objects in an image.<br><br>
See a sample program <a href="http://www.antillia.com/sol4py/samples/keras-yolo3/CustomYoloObjectDetector.html">CustomYoloObjectDetector.</a> 
See also an another program <a href="http://www.antillia.com/sol4py/samples/keras-yolo3/DetectedObjectHTMLFileGenerator.html">DetectedObjectHTMLFileGenerator for keras-yolo3.</a> 

</font>
<br>
<br>
<font size=2>
<b>SSD:<br></b>
We have downloaded <a href="https://github.com/SnowMasaya/ssd_keras">ssd_keras</a>, 
which is an SSD300v2 keras implementation of <a href="https://github.com/weiliu89/caffe/tree/ssd">SSD: Single Shot MultiBox Detector</a>,
and built a runtime-environment <i>ssd_keras</i> under SOL4Py-2 folder.<br><br>
See a sample program <a href="http://www.antillia.com/sol4py/samples/ssd_keras/SSDDetector.html">SSDDetector</a> to detect objects in an image.<br><br>
See also an another program <a href="http://www.antillia.com/sol4py/samples/ssd_keras/SSDDetectedObjectHTMLFileGenerator.html">SSDDetectedObjectHTMLFileGenerator for SSD300.</a> 
<br><br>
<br>
<b>YOLOv3 vs SSD:<br></b>

For comparison, please see the following three pages:<br><br>
<li><a href="http://www.antillia.com/keras-yolo3/detected.html">DetectedObjectHTMLFileGenerator for keras-yolo3</a></li><br>
<li><a href="http://www.antillia.com/yolo/detected.html">DetectedObjectHTMLFileGenerator for YOLOv3</a></li><br>

<li><a href="http://www.antillia.com/ssd/detected.html">SSDDetectedObjectHTMLFileGenerator for ssd_keras SSD300</a></li><br>

YOLOv3 seems to have a much better detection ability than SSD300 <b>apart from the processing time</b>.
</font>
<br>
<br>
<br>
<font size=2>

<b><font color ="red">NEW: Crypto classes</font></b><br>
We have implemented some wrapper classes to Cipher classes(AES and ChaCha20) of <a href="https://pycryptodome.readthedocs.io/en/latest/">pycrytodome</a> package.<br>
<br>
<b><font color ="red">NEW: Generator classes</font></b><br>
We have implemented some generator classes(ZEmailAddressGenerator, ZPasswordGenerator and ZTokenGenerator), 
By using those classes, you can generate a lot of fake personal data (personally identifiable information (PII)).
<br>
<br>
<b><font color="red">NEW: MySQLDB classes</font></b><br>
We have implemented some wrapper classes to MySQL(ZMySQLDB, ZThreadedMySQLConnection) based on mysql-connector-python.

</font>
<br>
<br>
</font>
<br>
