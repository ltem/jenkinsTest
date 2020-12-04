
def main():
    f = open("test.txt","w+")

    for i in range(10):
        f.write("Line: %d\r\n" % (i+1))

    f.close()


if __name__ == "__main__":
    main()
