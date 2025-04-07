import json

# Constants
count = 0
vis_level = 0
wheel_visibility = 0
vis_level_f = 0
vis_level_h = 0
occlusion_level = 0
wheel_count = 0

# Precompute constants
occlusion_thresholds = [0.3, 0.5]
visibility_thresholds = [0.7, 1.0]
occlusion_messages = ["less than 30%", "less than 50%"]
visibility_messages = ["more than 50%", "more than 70%"]


path = "D:/ATU/dataset/AngeliqueDataset/test_image/"
filename = path + "test1_result.json"

with open(filename) as user_file:
    inference = json.load(user_file)

# Iterate through the JSON array
for prediction in inference["predictions"]:
    visibility_temp = 0
    visibility_temp2 = 0
    image_class = prediction["class"]
    image_confidence = prediction["confidence"]

    if image_class == "wheel":
        image_width = prediction["width"]
        image_height = prediction["height"]
        width_height_ratio = image_width / image_height

        if width_height_ratio <= 0.5:
            print(f"Prediction [{count + 1}] is a [{image_class}] with [{image_confidence:.2%}] confidence and partially occluded")
            visibility_temp = occlusion_thresholds[0] if width_height_ratio < 0.3 else occlusion_thresholds[1]
            occlusion_level = occlusion_messages[0] if visibility_temp == occlusion_thresholds[0] else occlusion_messages[1]
            print(f"The [{image_class}] has occlusion {occlusion_level}")
        else:
            print(f"Prediction [{count + 1}] is a [{image_class}] with [{image_confidence:.2%}] confidence and fully visible")
            visibility_temp = visibility_thresholds[1] if width_height_ratio > 0.7 else visibility_thresholds[0]
            visibility_level = visibility_messages[1] if visibility_temp == visibility_thresholds[1] else visibility_messages[0]
            print(f"The [{image_class}] has visibility {visibility_level}")

        visibility_temp2 = 0.41 * visibility_temp
        print(f"Wheel count [{wheel_count}], size is [{image_width}]x[{image_height}] with visibility [{visibility_temp2:.2%}]")

        wheel_count += 1
        wheel_visibility += visibility_temp2

    elif image_class in ["frame", "handlebar"]:
        print(f"Prediction [{count + 1}] is a [{image_class}] with [{image_confidence:.2%}] confidence")
        if image_class == "frame":
            vis_level_f = 1
        elif image_class == "handlebar":
            vis_level_h = 1

    count += 1

# Calculate visibility levels
frame_visibility = 0.17 * vis_level_f
handlebar_visibility = 0.01 * vis_level_h
vis_level = wheel_visibility + frame_visibility + handlebar_visibility
occlusion_level = 1 - vis_level

# Print visibility levels
print(f"Wheel = [{wheel_visibility:.2%}], Frame = [{frame_visibility:.0%}], Handlebar = [{handlebar_visibility:.0%}]")
print(f"Bicycle visibility level = [{vis_level:.2%}]")
print(f"Bicycle occlusion level = [{occlusion_level:.2%}]")