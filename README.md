# rectangular_random_crop
caffe python layer to randomly crop a batch of images with different sizes for crop_height and crop_width




EXAMPLE O USE IN train_val.prototxt

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
