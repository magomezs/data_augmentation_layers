import caffe
import numpy as np
import os
import sys
import cv2 as cv 
import scipy
import PIL.Image
import random as rand

class RandomCrop(caffe.Layer):
	def setup(self, bottom, top):
       		layer_params = eval(self.param_str)
        	self.crop_height = layer_params['crop_height']
        	self.crop_width = layer_params['crop_width']
                
	def reshape(self, bottom, top):
		top[0].reshape(bottom[0].num, bottom[0].channels, self.crop_height, self.crop_width)
				
	def forward(self, bottom, top):	
		height_offset=rand.randint(0, bottom[0].height-self.crop_height)
		width_offset=rand.randint(0, bottom[0].width-self.crop_width)

		for b in range (bottom[0].num):
                	data1 = np.zeros((bottom[0].height, bottom[0].width, bottom[0].channels), dtype=np.uint8)
			for c in range (bottom[0].channels):
				data1[:, :, c] = bottom[0].data[b,c,:,:] 
			img = PIL.Image.fromarray(data1, 'RGB')

			left_p=width_offset
			top_p=height_offset
			right_p=width_offset+self.crop_width
			bottom_p = height_offset+self.crop_height
                        cropped = img.crop( ( left_p, top_p, right_p, bottom_p ) )
                	data2 = np.zeros((self.crop_height, self.crop_width, 3), dtype=np.uint8)
			data2 = np.asarray( cropped, dtype=np.uint8 )
			
			for d in range (3):
				top[0].data[b, d, :, :]= data2[:, :, d] 
		 
	def backward(self, top, propagate_down, bottom):
                pass
