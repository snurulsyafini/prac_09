import os


def main():
    """Loop through each file in directory and move into folders the same name as the extension"""
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        try:
            os.mkdir(extension)
        except FileExistsError:
            pass

        print(f"{extension}/{filename}")
        os.rename(filename, f"{extension}/{filename}")


if __name__ == '__main__':
    main()
