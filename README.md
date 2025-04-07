# Bicycle_Occlusion_Level
This projects aims to detect bicycle parts and analyse the visibility and occlusion level of the bicycle as a whole.

# Annotation
The image dataset for this project can be found in Roboflow. The dataset will be available to public from April 18, 2025. All annotations are manually done by the author using the segmentation concept.

# Model Training
Annotated images from roboflow were used to train a segmentation based model. The inference results from the model can be viewed using a project workflow or by directly using the trained model from roboflow.
An example weight from the training was provided and a PartsBasedDetection.py code to run the workflow.

# Methodology
To run this code, you must first run the model and extract the results in json format from inference. The code will use the image path as an input:

	path = "Your Local File path"
	filename = path + "detection_result.json"

It will then use the file and extract predictions and bounding box data to analyse the visibility level of each bicycle parts.
Example input image and json result is provided for reference.

# Output
The algorithm will output information such as bicycle parts visibility level and occlusion level of the bicycle as a whole.


  
  
  



# Author
*** Angelique Mangubat *** Master Thesis *** Connected Autonomous Vehicle *** Atlantic Technological University, Sligo *** 
