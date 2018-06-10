from megara_ml import MLAssistant


if __name__ == '__main__':
    megara = MLAssistant(language='es')

    while True:
        input()
        megara.main()
