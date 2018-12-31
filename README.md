This repository contains caffe python layer to perform data augmentation during the training.
This layers were meant to randomly crop and modify colour in re-id person images, but can be used with other applications. 




# rectangular_random_crop
caffe python layer to randomly crop a batch of images with different sizes for crop_height and crop_width


# random_colour_modification
caffe python layer to randomly modify the RGB value of every pixel of a batch of images by adding a certaing offset value, whose maximun absolute value if given by the layer parameter modification_range




# Example in train_val.prototxt

layer{

  name: "random_crop"
  
  type: "Python"
  
  bottom: "data"
  
  top: "crop"
  
  python_param {
  
    module: "rectangular_random_crop"
    
    layer: "RandomCrop" 
    
    param_str: '{"crop_height": 120, "crop_width": 56}' 
    
  }
  
}

layer{

  name: "random_colour_modification"
  
  type: "Python"
  
  bottom: "data"
  
  top: "new_colored_data"
  
  python_param {
  
    module: "random_colour_modification"
    
    layer: "RandomColourModification" 
    
    param_str: '{"modification_range: 50}' 
    
  }
  
}
