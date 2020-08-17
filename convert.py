# convert mnist/fashion mnist into csv file
# modified the code from https://pjreddie.com/projects/mnist-in-csv/

def convert(imgf, labelf, outimgf, outlabelf, n):
    f = open(imgf, "rb")
    l = open(labelf, "rb")
    o = open(outimgf, "w")
    ol = open(outlabelf, "w")

    f.read(16)
    l.read(8)
    images = []

    labels = []
    for i in range(n):
        label = []
        label.append(ord(l.read(1)))

        image = []
        for j in range(28*28):
            image.append(ord(f.read(1)))
        images.append(image)
        labels.append(label)

    for image in images:
        o.write(",".join(str(pix) for pix in image)+"\n")

    for label in labels:
        ol.write(",".join(str(pix) for pix in label)+"\n")

    f.close()
    l.close()
    o.close()
    ol.close()

convert("train-images-idx3-ubyte", "train-labels-idx1-ubyte",
        "images_train.csv", "labels_train.csv", 60000)
convert("t10k-images-idx3-ubyte", "t10k-labels-idx1-ubyte",
        "images_test.csv", "labels_test.csv", 10000)
