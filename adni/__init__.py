import load_data
import hdf5_to_csv

input_directory = 'adni/ADNI_radiomicFeatures.csv'


def main():
    data = load_data(input_directory)


if __name__ == "__main__":
    main()
