from megara import Assistant


if __name__ == '__main__':
    megara = Assistant(language='es')

    while True:
        input()
        megara.main()

    # while True:
    #     megara.main()

    # while True:
    #     megara.main_training()

    # while True:
    #     if megara.wating_keyword():
    #         megara.main()
