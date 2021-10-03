from terminal import Terminal
import FileReader


def main():
    with Terminal() as terminal:
        while True:
            char = terminal.get_character()
            print(char)
            if char == 'q':
                return


if __name__ == '__main__':
    main()
