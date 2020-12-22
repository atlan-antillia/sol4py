# Copyright 2020-2021 antillia.com Toshiyuki Arai
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

#  CustomYolo.py
# See also: https://github.com/qqwweee/keras-yolo3

# 2019/06/23 Updated 'detect_image' method to take a parameter save_imagefilename.

# 2019/06/23 Updated to use 'draw_detail' method to draw values_list 
# which is a sorted list of values = [id, predicted_class, score, top, left, width, height, color]
# by score.
 

# encodig: utf-8

import sys
import os
import cv2
import traceback
import csv

# 
#sys.path.append('../')

#from SOL4Py.ZApplicationView import *

#from SOL4Py.ZLabeledComboBox import ZLabeledComboBox
#from SOL4Py.ZLabeledSlider   import ZLabeledSlider
#from SOL4Py.opencv.ZOpenCVImageView import ZOpenCVImageView  
#from SOL4Py.ZVerticalPane    import ZVerticalPane  
#from SOL4Py.ZCSVTableView    import *

from yolo import *

#####################################################################
#

class CustomYolo(YOLO):
  ##
  # Constructor
  def __init__(self):
    YOLO.__init__(self)


  # Draw detail information of values_list  to a target image, where values_list is a sorted list of 
  # [id, predicted_class, score, top, left, width, height, color] by the third score parameter.
  def draw_detail(self, image, values_list):
    for i in range (len(values_list)):
      [id, object, score, top, left, width, height, c] = values_list[i]

      right  = left + width
      bottom = top  + height

      label = '{}'.format(i+1)

      font = ImageFont.truetype(font='font/FiraMono-Medium.otf',
                size=np.floor(3e-2 * image.size[1] + 0.5).astype('int32'))
      thickness = (image.size[0] + image.size[1]) // 400 #300

      draw = ImageDraw.Draw(image)

      label_size = draw.textsize(label, font)

      if top - label_size[1] >= 0:
        text_origin = np.array([left, top - label_size[1]])
      else:
        text_origin = np.array([left, top + 1])

      # My kingdom for a good redistributable image drawing library.
      for i in range(thickness):
        draw.rectangle([left + i, top + i, right - i, bottom - i],
                       outline=self.colors[c])
      draw.rectangle([tuple(text_origin), tuple(text_origin + label_size)],
                     fill=self.colors[c])
      draw.text(text_origin, label, fill=(0, 0, 0), font=font)
      del draw


  # Redefined detect_image method to write a set of values
  # [id, object, score, x, y, w, h] of each object detected to 
  # a csv file of csv_filename.
  
  def detect_image(self, image, save_imagefilename,  csv_filename):
    start = timer()
 
    if self.model_image_size != (None, None):
      assert self.model_image_size[0]%32 == 0, 'Multiples of 32 required'
      assert self.model_image_size[1]%32 == 0, 'Multiples of 32 required'
      boxed_image = letterbox_image(image, tuple(reversed(self.model_image_size)))
    else:
      new_image_size = (image.width - (image.width % 32),
                        image.height - (image.height % 32))
      boxed_image = letterbox_image(image, new_image_size)

    image_data = np.array(boxed_image, dtype='float32')

    print(image_data.shape)
    image_data /= 255.
    image_data = np.expand_dims(image_data, 0)  # Add batch dimension.

    out_boxes, out_scores, out_classes = self.sess.run(
        [self.boxes, self.scores, self.classes],
        feed_dict={
            self.yolo_model.input: image_data,
            self.input_image_shape: [image.size[1], image.size[0]],
            K.learning_phase(): 0
        })

    print('Found {} boxes for {}'.format(len(out_boxes), 'img'))

    with open(csv_filename, "w") as f:
      writer = csv.writer(f, lineterminator='\n') 
      #Write a header to the csv file
      writer.writerow(["id", "object", "score", "x", "y", "w", "h"])
      values_list = []

      for i, c in reversed(list(enumerate(out_classes))):
        predicted_class = self.class_names[c]
        box   = out_boxes[i]
        score = out_scores[i]

        top, left, bottom, right = box
        top  = max(0, np.floor(top + 0.5).astype('int32'))
        left = max(0, np.floor(left + 0.5).astype('int32'))
        bottom = min(image.size[1], np.floor(bottom + 0.5).astype('int32'))
        right  = min(image.size[0], np.floor(right + 0.5).astype('int32'))
        #print(label, (left, top), (right, bottom))

        #Append a set of values [id, object, score, x, y, w, h, c ] to the values_list.
        score = round(score, 2)
        values_list.append([i, predicted_class, score, top, left, right-left, bottom-top, c])
          
      def takeThird(elem):
        return elem[2]
 
      # Sort the values_list by using the third element 'score' of the list
      values_list.sort(key=takeThird, reverse=True)  #Sort on descending order on score 

      self.draw_detail(image, values_list)
      
      for i in range (len(values_list)):
        [id, object, score, x, y, w, h, c ] = values_list[i]
        values = [i+1, object, score, x, y, w, h]
        # Write the values row to the csv file writer.
        writer.writerow(values)

    end = timer()
    print(end - start)
    image.save(save_imagefilename, quality=95)
      
    return image
        
