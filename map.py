import matplotlib.pyplot as plt
import numpy as np
import re

def main():
    l = 150 #Number of lines to plot
    threshold = 0.001 #Min height value to draw (0 to 1)
    scale = 2.8 #Scale line heights (for more or less line overlap)
    thickness = 0.3 #Line thickness
    res = 1000 #Resolution of output image (in dpi)

    # Import Image
    f = r"Data\UK.png" #### <-- Path to heightmap image
    print("Importing image")
    dat = plt.imread(f)[10:-10, 10:-10]   #Sometimes the edges cause problems
    if len(dat.shape) > 2:                #If the image has more than 1 color
        dat = dat[:, :, 0]                #Use only the red channel

    m = np.max(dat)     #Usually 225 (used for normalizing)
    h = len(dat)        #Image Height
    w = len(dat[0])     #Image Width

    step = int(h / l)
    height = step * scale

    x = np.arange(0, w) #Used to plot all

    #Draw all lines
    print("Drawing lines")
    for i in range(0, h, step):

        #Retrieve slice data, and normalize height from 0 to 1 (/m)
        #Zip and transpose into a 2 by width matrix containing
        #x and y values together (useful when we need to remove some later)
        line = np.stack((x, (dat[i,:]/m))).T

        #Replace all values below threshold with None
        line[line[:,1] < threshold, :] = None

        #Plot current slice
        plt.plot(line[:, 0], line[:, 1] * height + h - i, "black", linewidth=thickness)

        #We don't want to see lines that cross with this one
        plt.fill(line[:, 0], line[:, 1] * height + h - i, "White")

    #Pyplot settings
    plt.axis("equal")
    plt.xticks([])
    plt.yticks([])
    plt.axis('off')

    #Save to file and view
    print("Saving image")
    # plt.savefig(re.sub("Data", "Images", f), dpi=res, bbox_inches='tight')
    plt.savefig(re.sub(r"\\(\w+)\.", r"\\\1-graphic.", f), dpi=res, bbox_inches='tight')
    plt.show()


if __name__ == '__main__':
    main()
