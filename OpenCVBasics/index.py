import cv2
from imutils import paths
from cbir.hsvdescriptor import HSVdescriptor

desc = HSVdescriptor((4,6,3))
output = open('./ukbench_features/index.csv','w')

image_paths = list(paths.list_images('./UKBench_dataset/ukbench/'))
#print(image_paths)
for img in sorted(image_paths):
    print(img)
    filename = img[img.rfind("/") + 1:]
    image = cv2.imread(img)

    features = desc.describe(image)
    features = [str(x) for x in features]
    output.write("{},{}\n".format(filename, ",".join(features)))

output.close()
