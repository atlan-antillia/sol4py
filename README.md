<font size=4>
<b>
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
<font size=3><b>
2.1 Basic Sample Programs
</b>
</font>
<br>
<hr>
<br>
<a name="2.1.1"><a href="http://www.antillia.com/sol4py/samples/uisamples/ApplicationView.html">2.1.1 How to use ZApplicationView?<br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/ApplicationView.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.1.2">
<a href="http://www.antillia.com/sol4py/samples/uisamples/ImageView.html">2.1.2 How to use ZImageView?<br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/ImageView.png" width="680" height="auto"  >
</a>
</a>
<br>
<br>
<br>

<a name="2.1.3">
<a href="http://www.antillia.com/sol4py/samples/uisamples/LabeledComboBox.html">2.1.3 How to use ZLabeledComboBox?<br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/LabeledComboBox.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.1.4">
<a href="http://www.antillia.com/sol4py/samples/uisamples/LabeledSlider.html">2.1.4 How to use ZLabeledSlider?<br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/LabeledSlider.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.1.5">
<a href="http://www.antillia.com/sol4py/samples/uisamples/ScrolledImageView.html">2.1.5 How to use ZScrolledImageView?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/ScrolledImageView.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.1.6">
<a href="http://www.antillia.com/sol4py/samples/uisamples/ColorPositioner.html">2.1.6 How to use ZColorPositioner?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/ColorPositioner.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<br>
<a name="2.1.7">
<a href="http://www.antillia.com/sol4py/samples/uisamples/FolderBrowser.html">2.1.7 How to use FolderBrowser?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/FolderBrowser.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<br>

<a name="2.1.8">
<a href="http://www.antillia.com/sol4py/samples/uisamples/TabbedWindow.html">2.1.8 How to use TabbedWindow?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/uisamples/TabbedWindow.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<br>
<a name="2.2.1">
<a href="http://www.antillia.com/sol4py/samples/opencv/OpenCVImageView.html">2.2.1 How to use ZOpenCVImageView?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/OpenCVImageView.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.2.2">
<a href="http://www.antillia.com/sol4py/samples/opencv/BoxFilter.html">2.2.2 How to use cv2.boxFilter?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/BoxFilter.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.2.3">
<a href="http://www.antillia.com/sol4py/samples/opencv/AdaptiveImageThresholding.html">2.2.3 How to use cv2.adaptiveThreshold?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/AdaptiveImageThresholding.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.4">
<a href="http://www.antillia.com/sol4py/samples/opencv/AKAZEFeatureDetector.html">2.2.4 How to use cv2.AKAZE feature detector?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/AKAZEFeatureDetector.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.5">
<a href="http://www.antillia.com/sol4py/samples/opencv/ImageStitcher.html">2.2.5 How to use cv2.createStitcher?<br><br>
In OpenCV-4.0.0 and 4.1.0, this sample program didn't work well by a stitcher bug. 
In OpenCV-4.2.0 the bug has been fixed, and this runs well.<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/ImageStitcher.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.6">
<a href="http://www.antillia.com/sol4py/samples/opencv/ImageSharpening.html">2.2.6 How to use cv2.GaussianBlur and cv2.addWeighted?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/ImageSharpening.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.7">
<a href="http://www.antillia.com/sol4py/samples/opencv/ImageMorphing.html">2.2.7 How to use cv2.getStructuringElement and cv2.morphologyEx?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/ImageMorphing.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.8">
<a href="http://www.antillia.com/sol4py/samples/opencv/FlannBasedMatcher.html">2.2.8 How to use cv2.FlannBasedMatcher?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/FlannBasedMatcher.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.9">
<a href="http://www.antillia.com/sol4py/samples/opencv/NonPhotorealisticRendering.html">2.2.9 How to use cv2.edgePreservingFilter, cv2.detailEnhance and cv2.pencilSketch?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/NonPhotorealisticRendering.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.10">
<a href="http://www.antillia.com/sol4py/samples/opencv/ObjectDetectorByCacadeClassifier.html">2.2.10 How to use cv2.CascadeClassifier to detect faces?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/ObjectDetectorByCacadeClassifier.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.11">
<a href="http://www.antillia.com/sol4py/samples/opencv/HOGPeopleDetector.html">2.2.11 How to use cv2.HOGDescriptor to detect pedestrians?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/HOGPeopleDetector.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.12">
<a href="http://www.antillia.com/sol4py/samples/opencv/VideoFilePlayer.html">2.2.12 How to use cv2.VideoCapture to display video files?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/VideoFilePlayer.png" width="680" height="auto"  >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.13">
<a href="http://www.antillia.com/sol4py/samples/plot/ScrolledPlottingArea.html">2.2.13 How to use a scrolled plotting area to draw a figure of matplotlib and seaborn?<br><br>
<img src="http://www.antillia.com/sol4py/samples/plot/ScrolledPlottingArea.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.2.14">
<a href="http://www.antillia.com/sol4py/samples/opencv/ImageGaussianNoiseInjector.html">2.2.14 How to inject the Gaussian noise to an image of OpenCV?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opencv/ImageGaussianNoiseInjector_1.png" width="680" height="auto"  >
</a>
</a>
<br>
<br>
<br>
<a name="2.3.1">
<a href="http://www.antillia.com/sol4py/samples/cnn/CIFARClassifier.html">2.3.1 How to use CIFAR-10 and CIFAR-100 datasets on cnn model for image classification?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/CIFAR.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.3.2">
<a href="http://www.antillia.com/sol4py/samples/cnn/MNISTClassifier.html">2.3.2 How to use MNIST and FashionMNIS datasets on cnn model for image classification?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/MNIST.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.3.3">
<a href="http://www.antillia.com/sol4py/samples/cnn/VGG16Classifier.html">2.3.3 How to use VGG16 cnn model for image classification?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/VGG16_6.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.3.4">
<a href="http://www.antillia.com/sol4py/samples/cnn/InceptionV3Classifier.html">2.3.4 How to use inception-v3 cnn model for image classification?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/Inception-v3-1.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.4.1">
<a href="http://www.antillia.com/sol4py/samples/ml/DecisionTreeClassifier.html">2.4.1 How to use DecisionTreeClassifier?<br><br>
<img src="http://www.antillia.com/sol4py/samples/ml/DecisionTreeClassifier2.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.4.2">
<a href="http://www.antillia.com/sol4py/samples/ml/LightGBMClassifier.html">2.4.2 How to use LightGBMClassifiers?<br><br>
<img src="http://www.antillia.com/sol4py/samples/ml/LightGBMClassifier.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>

<a name="2.4.3">
<a href="http://www.antillia.com/sol4py/samples/ml/RandomForestRegressor.html">2.4.3 How to use RandomForestRegressor?<br><br>
<img src="http://www.antillia.com/sol4py/samples/ml/RandomForestRegressor.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.4.4">
<a href="http://www.antillia.com/sol4py/samples/ml/XGBClassifier.html">2.4.4 How to use XGBClassifier?<br><br>
<img src="http://www.antillia.com/sol4py/samples/ml/XGBClassifier.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.5.1">
<a href="http://www.antillia.com/sol4py/samples/socket/CustomThreadedTCPServer.html">2.5.1 How to use CustomThreadedTCPServer?<br><br>
<img src="http://www.antillia.com/sol4py/samples/socket/CustomThreadedTCPServer.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.5.2">
<a href="http://www.antillia.com/sol4py/samples/socket/CustomThreadedUDPServer.html">2.5.2 How to use CustomThreadedUDPServer?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/socket/CustomThreadedUDPServer.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.5.3">
<a href="http://www.antillia.com/sol4py/samples/socket/CustomThreadingMixInTCPServer.html">2.5.3 How to use CustomThreadingMixInTCPServer.html?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/socket/CustomThreadingMixInTCPServer.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.5.4">
<a href="http://www.antillia.com/sol4py/samples/socket/CustomThreadingMixInUDPServer.html">2.5.4 How to use CustomThreadingMixInUDPServer?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/socket/CustomThreadingMixInUDPServer.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.5.5">
<a href="http://www.antillia.com/sol4py/samples/socket/NonblockingTCPServerThread.html">2.5.5 How to use NonblockingTCPServerThread?</a><br><br>
<img src="http://www.antillia.com/sol4py/samples/socket/NonblockingTCPServerThread.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.6.1">
<a href="http://www.antillia.com/sol4py/samples/oracle/InsertIntoTable.html">2.6.1 How to insert data into a table of Oracle12C?</a><br><br>
</a>
<br>
<br>
<br>
<a name="2.6.2">
<a href="http://www.antillia.com/sol4py/samples/oracle/SelectFromTable.html">2.6.2 How to select records from a table of Oracle12C ?</a><br><br>
</a>
<br>
<br>
<br>
<a name="2.7.1">
<a href="http://www.antillia.com/sol4py/samples/opengl/ColoredPyramid.html">2.7.1 How to render a colored pyramid in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/ColoredPyramid.png" width="680" height="auto"  >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.2">
<a href="http://www.antillia.com/sol4py/samples/opengl/CubeRotationByTimerThread.html">2.7.2 How to rotate a cube by timer thread in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/CubeRotationByTimerThread.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.3">
<a href="http://www.antillia.com/sol4py/samples/opengl/MaterializedTorusesRotationByKeyInput.html">2.7.3 How to rotate multiple materialized toruses in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/MaterializedTorusesRotationByKeyInput.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.4">
<a href="http://www.antillia.com/sol4py/samples/opengl/MultiJPGTexturedCubeRotationByKeyInput.html">2.7.4 How to rotate a multiple jpg textured cubes in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/MultiJPGTexturedCubeRotationByKeyInput.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.5">
<a href="http://www.antillia.com/sol4py/samples/opengl/Texture.html">2.7.5 How to map a texture in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/Texture.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.6">
<a href="http://www.antillia.com/sol4py/samples/opengl/TexturedSphereRotationByKeyInput.html">2.7.6 How to rotate a textured sphere in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/TexturedSphereRotationByKeyInput.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.7">
<a href="http://www.antillia.com/sol4py/samples/opengl/TexturedSphereWithAxisEyeAndLightPositioner.html">2.7.7 How to use axis-eye-light-positioner to render a textured sphere in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/TexturedSphereWithAxisEyeAndLightPositioner.png" width="680" height="auto"   >
</a>
<br>
<br>
<br>
<br>
<a name="2.7.8">
<a href="http://www.antillia.com/sol4py/samples/opengl/BufferedColoredRegularIcosahedron.html">2.7.8 How to render a buffered colored regular icosahedron in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/opengl/BufferedColoredRegularIcosahedron.png" width="680" height="auto" >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.9">
<a href="http://www.antillia.com/sol4py/samples/openglcv/NonPhotorealisticImagesTexturedCube.html">2.7.9 How to render a cube textured by OpenCV-NonPhotorealistic images in OpenGL?<br><br>
<img src="http://www.antillia.com/sol4py/samples/openglcv/NonPhotorealisticImagesTexturedCube.png" width="680" height="auto" >
</a>
</a>
<br>
<br>
<br>
<a name="2.7.10">
<a href="http://www.antillia.com/sol4py/samples/openglcv/OpenGLCVImageViews.html">2.7.10 How to show OpenGLView and OpenCVView on a window in SOL4Py?<br><br>
<img src="http://www.antillia.com/sol4py/samples/openglcv/OpenGLCVImageViews.png" width="680" height="auto"   >
</a>
</a>
<br>
<br>
<br>
<a name="2.8.1">
<b>

<a href="http://www.antillia.com/sol4py/samples/keras/AugmentedImagePreview.html">2.8.1 How to preview images generated by Keras ImageDataGenerator?<br><br>
<img src="http://www.antillia.com/sol4py/samples/keras/AugmentedImagePreview.png" width="680" height="auto"   >
</b>
</a>
</a>
<br>
<br>
<br>
<a name="2.8.2">
<a href="http://www.antillia.com/sol4py/samples/cnn/VegeFruitsClassifier.html">2.8.2 How to create an image classifier for your image data by using CNN?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/VegeFruitsClassifier_1.png" width="680" height="auto"   ><br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/VegeFruitsClassifier_3.png" width="680" height="auto"   ><br><br>

</b>
</a>
</a>
<br>
<br>
<br>
<a name="2.8.3">
<a href="http://www.antillia.com/sol4py/samples/cnn/TrainingProcessMonitor.html">2.8.3 How to visualize training accuracy and loss in Keras Model fitting process by using matplotlib?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/TrainingProcessMonitor-VegeFruitsModel.2.png" width="680" height="auto"   >
</b>
</a>
</a>
<br>
<br>
<br>
<br>
<a name="2.8.4">
<a href="http://www.antillia.com/sol4py/samples/cnn/MNISTDenoisingAutoEncoder.html">2.8.4 How to derive MNISTDenoisingAutoEncoder class from MNISTAutoEndoder?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/MNISTDenoisingAutoEncoder.png" width="680" height="auto"   >
</b>
</a>
</a>
<br>
<br>
<br>
<a name="2.8.5">
<a href="http://www.antillia.com/sol4py/samples/cnn/TOKYO2020_SPORT_PICTOGRAMS_Classifier.html">2.8.5 How to create PictogramClassifier to TOKYO2020-SPORT-PICTOGRAMS by using Keras ImageDataGenerator?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/PictogramClassifier.1.png" width="680" height="auto"   ><br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/PictogramClassifier.5.png" width="680" height="auto"   ><br><br>
</b>
</a>
</a>
<br>
<br>
<br>

<a name="2.8.6">
<a href="http://www.antillia.com/sol4py/samples/cnn/VegeFruitsAutoEncoder.html">2.8.6 How to apply Keras AutoEncoder to color images of VegeFruits dataset?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/VegeFruitsAutoEncoder.2.png" width="680" height="auto"   ><br><br>

</b>
</a>
</a>
<br>
<br>
<br>
<a name="3.1.1">
<a href="http://www.antillia.com/sol4py/samples/keras-yolo3/YoloObjectDetector.html">3.1.1 How to use yolo3 in Keras to detect objects in an image?<br><br>
<img src="http://www.antillia.com/sol4py/samples/keras-yolo3/YoloObjectDetector.1.png" width="680" height="auto"   >
</b>
</a>
</a>
<br>
<br>
<br>
<a name="3.1.2">
<a href="http://www.antillia.com/sol4py/samples/keras-yolo3/CustomYoloObjectDetector.html">3.1.2 How to derive CustomYoloObjectDetector class from YOLO class to display detailed information detected ?<br><br>
<img src="http://www.antillia.com/sol4py/samples/keras-yolo3/CustomYoloObjectDetector.1.png" width="680" height="auto"   ><br><br>
<img src="http://www.antillia.com/sol4py/samples/keras-yolo3/CustomYoloObjectDetector.4.png" width="680" height="auto" >
</b>
</a>
</a>
<br>
<br>
<br>
<a name="3.2.1">
<a href="http://www.antillia.com/sol4py/samples/cnn/RoadSignsClassifier.html">3.2.1 How to create RoadSignsClassifier to classify the roadsigns in an image by using Keras ImageDataGenerator?<br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/RoadSignsClassifier.3.png" width="680" height="auto"   ><br><br>
<img src="http://www.antillia.com/sol4py/samples/cnn/RoadSignsClassifier.2.png" width="680" height="auto"   ><br><br>

</b>
</a>
</a>
<br>
<br>
<br>
<a name="3.2.2">
<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchRoadSignsClassifier.html">3.2.2 How to create TorchRoadSignsClassifier to classify the roadsigns in an image by using ZImageDataGenerator and TorchRoadSignsDataset?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchRoadSignsClassifier.png" width="680" height="auto"   ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchRoadSignsClassifier.4.png" width="680" height="auto"   ><br><br>

</b>
</a>
</a>
<br>
<br>
<br>

<a name="4.1">

<a href="http://www.antillia.com/sol4py/samples/samples/FileTreeWalker.html">4.1 How to create LogWriter(ZLogger) class to write a string of format
of [datetime, log-level, filename, line-no, function, message] to multiple streams?<br><br>
<img src="http://www.antillia.com/sol4py/samples/samples/FileTreeWalker.png" width="680" height="auto"   >
</b>
</a>
</a>
<br>
<br>
<br>
<a name="5.1">

<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchInceptionV3Classifier.html">5.1 How to create TorchInceptionV3Classifier to use pretrained torch inceptionv3 model?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchInceptionV3Classifier.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchInceptionV3Classifier.2.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<br>
<a name="5.2">

<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARModel.html">5.2 How to visualize training accuracy and loss in Torch Model fitting process by using matplotlib and tqdm(progress bar)?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARModel-0_TrainingProcessProgressBar.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARModel-0_TrainingProcessMonitor.png" width="680" height="auto" ><br><br>

</b>
</a>
</a>
<br>
<br>
<br>
<a name="5.3">
<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchMNISTlassifier.html">5.3 How to create TorchMNISTClassifier by using ZTorchMNISTModel?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchMNISTClassifier.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchMNISTClassifier.2.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<br>
<a name="5.4">
<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARClassifier.html">5.4 How to create TorchCIFARClassifier by using TorchCIFARModel?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARClassifier.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchCIFARClassifier.2.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<a name="5.5">
<a href="http://www.antillia.com/sol4py/samples/torch-cnn/Torch_TOKYO2020_SPORT_PICTOGRAMS_Classifier.html">5.5 How to create TorchPictogramClassifier to TOKYO2020-SPORT-PICTOGRAMS by using ZImageDataGenerator and Torch_TOKYO2020_SPORT_PICTOGRAMS_Dataset?<br><br>

<img src="http://www.antillia.com/sol4py/samples/torch-cnn/Torch_TOKYO2020_SPORT_PICTOGRAMS_Classifier.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/Torch_TOKYO2020_SPORT_PICTOGRAMS_Classifier.2.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<a name="5.6">
<a href="http://www.antillia.com/sol4py/samples/torch-cnn/TorchVegeFruitsDenoisingAutoEncoder.html">5.6 How to create ZPILGaussianNoise and insert it into Torch image transforms Composer?<br><br>
<img src="http://www.antillia.com/sol4py/samples/torch-cnn/TorchVegeFruitsDenoisingAutoEncoder.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<br>
<a name="6.1">
<a href="http://www.antillia.com/sol4py/classes/ZCustomImageDataGenerator.html">6.1 How to create ZCustomImageDataGenerator by using Pillow image library?<br><br>
<img src="http://www.antillia.com/sol4py/classes/CustomImageDataGenerator.png" width="680" height="auto" ><br><br>
<!--
<img src="http://www.antillia.com/sol4py/samples/util/CustomImageDataGenerator.2.png" width="680" height="auto" ><br><br>
-->
</b>
</a>
</a>
<br>
<br>

<a name="6.2">

<a href="http://www.antillia.com/sol4py/samples/utils/CustomAugmentedImagePreview.html">6.2 How to preview images augmented by ZCustomImageDataGenerator?<br><br>
<img src="http://www.antillia.com/sol4py/samples/utils/CustomAugmentedImagePreview.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/utils/CustomAugmentedImagePreview.5.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<a name="6.3">
<a href="http://www.antillia.com/sol4py/samples/utils/CustomImageDataGenerator.html">6.3 How to generate and save images generated by ZCustomImageDataGenerator?<br><br>
<img src="http://www.antillia.com/sol4py/samples/utils/CustomImageDataGenerator.2.png" width="680" height="auto" ><br><br>
<img src="http://www.antillia.com/sol4py/samples/utils/CustomImageDataGenerator.3.png" width="680" height="auto" ><br><br>

<!--
<img src="http://www.antillia.com/sol4py/samples/util/CustomImageDataGenerator.2.png" width="680" height="auto" ><br><br>
-->
</b>
</a>
</a>

<!-- 2020/01/27 -->

<a name="7.1">
<a href="http://www.antillia.com/sol4py/samples/crypto/AESCipher.html">7.1 How to encrypt and decrypt strings by using ZAESCipher?<br><br>
<img src="http://www.antillia.com/sol4py/samples/crypto/AESCipher.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>

<a name="7.2">

<a href="http://www.antillia.com/sol4py/samples/crypto/AESIVEmbeddedCipher.html">7.2 How to encrypt and decrypt files by using ZAESIVEmbedeCipher?<br><br>
<img src="http://www.antillia.com/sol4py/samples/crypto/AESIVEmbeddedCipher.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>
<a name="7.3">
<a href="http://www.antillia.com/sol4py/samples/crypto/ChaCha20Cipher.html">7.3 How to encrypt and decrypt strings by using ZChaCha20Ciper?<br><br>
<img src="http://www.antillia.com/sol4py/samples/crypto/ChaCha20Cipher.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>

<br>
<br>
<a name="7.4">
<a href="http://www.antillia.com/sol4py/samples/crypto/ChaCha20NonceEmbeddedCipher.html">7.4 How to encrypt and decrypt strings by using ZChaCha20NonceEmbeddeCiper?<br><br>
<img src="http://www.antillia.com/sol4py/samples/crypto/ChaCha20NonceEmbeddedCipher.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<!-- 2020/01/28 -->

<a name="8.1">
<a href="http://www.antillia.com/sol4py/samples/mysql/EncryptDecryptPassword.html">8.1 8.1 How to encrypt and decrypt a password in a MySQL table by using ZAESIVEmbeddedCipher?<br><br>
<img src="http://www.antillia.com/sol4py/samples/mysql/EncryptDecryptPassword.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
<br>

<a name="8.2">

<a href="http://www.antillia.com/sol4py/samples/mysql/SelectFromTableThread.html">8.2 8.2 How to use ZThreadedMySQLConnection in in MySQL??<br><br>
<img src="http://www.antillia.com/sol4py/samples/mysql/SelectFromTableThread.png" width="680" height="auto" ><br><br>
</b>
</a>
</a>
<br>
