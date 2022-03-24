import load_data as ld

input_directory = 'adni/'


def main():
    data = ld.load_data()
    print(data)


if __name__ == "__main__":
    main()
