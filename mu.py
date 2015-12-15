from ten_thousands_things import Dog, MU


class Master:
    def has_buddha_nature(self, obj):
        if obj == Dog:
            return MU


class Monk:
    def ask(self, master):
        print('Monk:   Does a dog have a Buddha-nature or not?')
        return master.has_buddha_nature(Dog)


def main():
    master = Master()
    monk = Monk()

    answer = monk.ask(master)
    print('Master: ' + str(answer))


if __name__ == '__main__':
    main()