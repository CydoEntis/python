if __name__ == '__main__':
    zipCode = input()
    try:
        # check if zip code is an integer value
        int(zipCode)
        print(f'Your zip code is {zipCode}.')
    except ValueError:
        print('Please use numeric digits for the zip code.')