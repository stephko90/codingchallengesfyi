import sys, os

def main(argv):
    print(argv)
    ## todo make sure argv is input properly
    fname = argv[-1]
    fp = open(fname, 'r')
    if "-c" in argv:
        fstats = os.stat(fname)
        print("{} {}".format(fstats.st_size, fname))
    elif "-l" in argv:
        lines = len(fp.readlines())
        print("{} {}".format(lines, fname))
    elif "-w" in argv or "-m" in argv:
        size = 0
        words = 0
        for line in fp.readlines():
            size += len(line)+1
            if line.isspace(): continue
            splits = line.split(" ")
            words += len(splits)-splits.count('')
        print("{} {}".format(size, fname))
        print("{} {}".format(words, fname))
        # for i in range(0,100):
        #     line = fp.readline()
        #     if line.isspace(): continue
        #     splits = line.split(" ")
        #     print(splits)
        #     words = len(splits)-splits.count('')
        #     print(words)
        #     print(line)
        # print(len(line))


    fp.close()
    # try:
    #     opts, args = getopt.getopt(argv, "hc:")
    #     print("{} {}".format(opts, args))
    # except getopt.GetoptError:
    #     print('wc.py <file> <headers>')
    #     sys.exit(2)
    # for opt, arg in opts:
    #     print("{} {}".format(opt, args))

if __name__ == "__main__":
    main(sys.argv[1:])