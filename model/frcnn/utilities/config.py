import math


class Config:
	"""Save the parameters for training process"""

	def __init__(self):
		# Display bar-progress in Terminal
		self.verbose = True
		# setting for data augmentation
		self.data_augmentation = False
		# training
		self.num_epochs = 5
		self.epoch_length = 32
		self.learning_rate = 0.00001
		self.use_gpu = False
		# anchor box scales
		self.anchor_box_scales = [128, 256, 512]
		# anchor box ratios
		self.anchor_box_ratios = [
			[1, 1],
			[1./math.sqrt(2), 2./math.sqrt(2)],
			[2./math.sqrt(2), 1./math.sqrt(2)]
		]
		# size to resize the smallest side of the image
		self.im_size = 600
		# image channel-wise mean to subtract
		self.img_channel_mean = [103.939, 116.779, 123.68]
		self.img_scaling_factor = 1.0
		# number of ROIs at once
		self.num_rois = 32
		# stride at the RPN (stride = number of pixels to sliding for anchors)
		self.rpn_stride = 16
		# get an equal count of classes of the samples
		self.balanced_classes = False
		# scaling the stdev
		self.std_scaling = 4.0
		self.classifier_regr_std = [8.0, 8.0, 4.0, 4.0]
		# overlaps for RPN
		self.rpn_min_overlap = 0.3
		self.rpn_max_overlap = 0.7
		# overlaps for classifier ROIs
		self.classifier_min_overlap = 0.1
		self.classifier_max_overlap = 0.5
		# Persistence for configuration parameters
		self.config_file_path = "config.pickle"
		# Automatically generated by the parser
		self.class_mapping = None
		# Weights
		self.weights_output_path = "model_frcnn.hdf5"
		self.weights_input_path = "model_frcnn.hdf5"
