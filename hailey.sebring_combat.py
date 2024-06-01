import haileysebring_tbc

def main():
    hero = haileysebring_tbc.Character("Hero", 10, 50, 5, 2)
   
    monster = haileysebring_tbc.Character("Monster", 20, 30, 5, 0)

    hero.printStats()
    monster.printStats()

    while True:
        input("Press enter for another round: ")
        haileysebring_tbc.fight(hero, monster)
        if hero.hitPoints <= 0 or monster.hitPoints <= 0:
            break

if __name__ == "__main__":
    main()
