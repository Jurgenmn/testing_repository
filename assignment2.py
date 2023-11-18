def find_words(file):
    f = open(file, 'r')
    data = f.read()
    f.close()

    file_words = data.split(" ")
    nr_words = len(file_words)
    print(f"There are {nr_words} words in this file")


def main():
    file_name = input("What's the file name? ")
    find_words(file_name)


main()