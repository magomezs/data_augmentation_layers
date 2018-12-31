import caffe
import numpy as np
import os
import sys
import cv2 as cv 
import scipy
import PIL.Image
import random as rand
import colorsys


class RandomColourModification(caffe.Layer):
	def setup(self, bottom, top):
       		layer_params = eval(self.param_str)
        	self.color_variation = layer_params['colour_variation_range']
                
	def reshape(self, bottom, top):
		top[0].reshape(bottom[0].num, bottom[0].channels, bottom[0].height, bottom[0].width)
		
	def forward(self, bottom, top):	
                for b in range (bottom[0].num):
			color_offset=np.float32(rand.randint(-self.color_variation, self.color_variation))
			top[0].data[b, :, :, :] = np.clip(bottom[0].data[b,:,:,:]+ color_offset, 0, 255)

	def backward(self, top, propagate_down, bottom):
                pass



