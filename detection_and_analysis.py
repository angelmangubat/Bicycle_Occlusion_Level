import json

count = 0
vis_level = 0
vis_level_w = 0
vis_level_f = 0
vis_level_h = 0
occlusion_level = 0
wheel_count = 0

path = "Your Local File path"
filename = path + "detection_result.json"

# with open(filename) as user_file:
#    file_contents = user_file.read()
# print(file_contents)

with open(filename) as user_file:
    inference = json.load(user_file)

# Iterate through the JSON array
for _predictions in inference["predictions"]:
    vis_level_w_temp = 0
    vis_level_w_temp2 = 0
    im_class = _predictions["class"]
    im_confidence = _predictions["confidence"]

    if im_class == "wheel":
        im_x = _predictions["width"]
        im_y = _predictions["height"]

        if im_x <= 0.5 * im_y:
            print(
                "Prediction [{}] is a [{}] with [{:.2%}] confidence and partially occluded".format(count + 1, im_class,
                                                                                                   im_confidence))
            if im_x < 0.3 * im_y:
                print("The [{}] has occlusion less than 30%".format(im_class))
                vis_level_w_temp = 0.3
            else:
                print("The [{}] has occlusion less than 50%".format(im_class))
                vis_level_w_temp = 0.5
        else:
            print("Prediction [{}] is a [{}] with [{:.2%}] confidence and fully visible".format(count + 1, im_class,
                                                                                                im_confidence))
            if im_x > 0.7 * im_y:
                print("The [{}] has visibility more than 70%".format(im_class))
                vis_level_w_temp = 1
            else:
                print("The [{}] has visibility more than 50%".format(im_class))
                vis_level_w_temp = 0.7
        print("Wheel count [{}], size is [{}]x[{}] with visibility [{:.2%}]".format(wheel_count, im_x, im_y,
                                                                                    0.41 * vis_level_w_temp))
        vis_level_w_temp2 = 0.41 * vis_level_w_temp

        wheel_count = wheel_count + 1
        # Combine wheel visibility level
        vis_level_w = vis_level_w + vis_level_w_temp2
        # print("Total Wheel visibility = [{:.2%}]".format(vis_level_w))

    elif im_class == "frame":
        print("Prediction [{}] is a [{}] with [{:.2%}] confidence".format(count + 1, im_class, im_confidence))
        vis_level_f = 1

    elif im_class == "handlebar":
        print("Prediction [{}] is a [{}] with [{:.2%}] confidence".format(count + 1, im_class, im_confidence))
        vis_level_h = 1

    count = count + 1

print(
    "Wheel = [{:.2%}], Frame = [{:.0%}], Handlebar = [{:.0%}]".format(vis_level_w, 0.17 * vis_level_f,
                                                                      0.01 * vis_level_h))
vis_level = vis_level_w + 0.17 * vis_level_f + 0.01 * vis_level_h
occlusion_level = 1 - vis_level
print("Bicycle visibility level = [{:.2%}]".format(vis_level))
print("Bicycle occlusion level = [{:.2%}]".format(occlusion_level))
