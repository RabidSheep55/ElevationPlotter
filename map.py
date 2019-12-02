import matplotlib.pyplot as plt
import numpy as np

def main():
    l = 40             #Number of lines to plot
    threshold = 0.05    #Min height value to draw (0 to 1)
    scale = 2           #Scale line heights (for more or less line overlap)

    # Import Image
    dat = plt.imread("Data\Australia.jpg")[1:, 10:-10, 0]

    m = np.max(dat)     #Usually 225
    h = len(dat)        #Image Height
    w = len(dat[0])     #Image Width

    step = int(h / l)
    height = step * scale

    x = np.arange(0, w)

    #Draw all lines
    for i in range(0, h, step):

        #Retrieve slice data, and normalize height from 0 to 1 (/m)
        line = np.stack((x, (dat[i,:]/m))).T

        #Replace all values below threshold with None
        line[line[:,1] < threshold, :] = None

        #Plot current slice
        plt.plot(line[:, 0], line[:, 1] * height + h - i, "black")

        #We don't want to see lines that cross with this one
        plt.fill(line[:, 0], line[:, 1] * height + h - i, "White")

    plt.axis("equal")
    plt.show()

if __name__ == '__main__':
    main()
