import os


def main():
    """Sort files into specific folders named by user by extension"""
    extension_categories = {}
    os.chdir('FilesToSort')
    for filename in os.listdir('.'):
        if os.path.isdir(filename):
            continue

        extension = filename.split('.')[-1]

        if extension not in extension_categories:
            category = input(f"What category would you like to sort {extension} files into? ")
            extension_categories[extension] = category

            try:
                os.mkdir(category)
            except FileExistsError:
                pass

        os.rename(filename, f"{extension_categories[extension]}/{filename}")


if __name__ == '__main__':
    main()
