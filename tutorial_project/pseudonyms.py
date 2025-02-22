import sys, random

def main():
    print("Welcome to the Benedict Cumberbatch name picker.' \n")
    print("A name fit for a Hollywood star.:\n\n")

    first = ('Blubberbutt', 'Benedict', 'Benadryl', 'Benchthis', 'Bonapart', 'Brokenbrick', 'Boppinstick', 'Benefit', 
            'Scissorkick', 'Backitup', 'Beezlebub', 'Burgerking', 'Blenderdick', 'Billiardball', 'Guiltyverdict', 
            'Beanbag', 'Carrotstick', 'Brodyquest', 'Beachbody', 'Bendylick', 'Baseballmitt', 'Bedbug', 'Bunsenburner',
            'Bengaltiger', 'Budapest', 'Handpicked')

    last = ('Calldispatch', 'Comedicmismatch', 'Cunningscratch', 'Cumberfinch', 'Humperdinck', 'Lumberlatch', 'Flubbercrack',
            'Cumberbatch', 'Bandersnatch', 'Cuttlefish', 'Slumberbelch', 'Cupboardlatch', 'Combyourthatch', 'Thundermunch',
            'Cricketbat', 'Johnnycash', 'Comelycat', 'Custardbath', 'Thundercats', 'Numbercrunch', 'Luckycatch', 'Covertrack',
            'Uptoscratch', 'Compasstrap', 'Chunkybap', 'Candygram')

    while True:
        first_name = random.choice(first)

        last_name = random.choice(last)

        print("\n\n")
        print("{} {}".format(first_name, last_name), file=sys.stderr)
        print("\n\n")
    
        try_again = input("\n\nTry again? (Press Enter else n to quit)\n")
        if try_again.lower() == "n":
            break
        
if __name__ == "__main__":
    main()

