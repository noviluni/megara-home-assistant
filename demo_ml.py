from megara_ml import Assistant


if __name__ == '__main__':
    megara = Assistant(language='es')

    while True:
        input()
        megara.main()
