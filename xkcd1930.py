#! /usr/bin/env python3

"""
    xkcd Strip 1930
    ===============

    http://xkcd.com/1930

    Calendar facts. Pretty naive implementation.
"""
import random

class xkcd1930:
    def __init__(self):
        self.statement = ""

    def generate_statement(self):
        self.statement = "Did you know that "
        self.get_first_block()
        self.get_second_block()
        self.get_third_block()
        self.get_fourth_block()
        print(self.statement)

    def get_first_block(self):
        block_main_parts = ["the ",
                            "daylight ",
                            "leap ",
                            "easter ",
                            "Toyota Truck Month ",
                            "Shark Week "]

        random_index = random.randrange(len(block_main_parts))
        self.statement += block_main_parts[random_index]

        if random_index == 0:
            case_selector = random.randrange(4)
            if case_selector == 0:
                up_or_down = random.randrange(2)
                if up_or_down == 0:
                    self.statement += "fall "
                else:
                    self.statement += "spring "

                self.statement += "equinox "

            elif case_selector == 1:
                up_or_down = random.randrange(2)
                if up_or_down == 0:
                    self.statement += "winter "
                else:
                    self.statement += "summer "

                up_or_down = random.randrange(2)
                if up_or_down == 0:
                    self.statement += "soltice "
                else:
                    self.statement += "Olympics "

            elif case_selector == 2:
                up_or_down = random.randrange(2)
                if up_or_down == 0:
                    self.statement += "earliest "
                else:
                    self.statement += "latest "

                up_or_down = random.randrange(2)
                if up_or_down == 0:
                    self.statement += "sunrise "
                else:
                    self.statement += "sunset "

            elif case_selector == 3:
                up_or_down = random.randrange(3)
                if up_or_down == 0:
                    self.statement += "harvest "
                elif up_or_down == 1:
                    self.statement += "super "
                else:
                    self.statement += "blood "

                self.statement += "moon "

        elif random_index == 1:
            up_or_down = random.randrange(2)
            if up_or_down == 0:
                self.statement += "saving "
            else:
                self.statement += "savings "

            self.statement += "time "

        elif random_index == 2:
            up_or_down = random.randrange(2)
            if up_or_down == 0:
                self.statement += "day "
            else:
                self.statement += "year "

    def get_second_block(self):
        block_main_parts = ["happens ",
                            "drifts out of sync ",
                            "might "]

        random_index = random.randrange(len(block_main_parts))
        self.statement += block_main_parts[random_index]

        if random_index == 0:
            up_or_down = random.randrange(3)
            if up_or_down == 0:
                self.statement += "earlier "
            elif up_or_down == 1:
                self.statement += "later "
            else:
                self.statement += "at the wrong time "

            self.statement += "every year "

        if random_index == 1:
            up_or_down = random.randrange(5)
            if up_or_down == 0:
                self.statement += "sun "
            elif up_or_down == 1:
                self.statement += "moon "
            elif up_or_down == 2:
                self.statement += "zodiac "
            elif up_or_down == 3:
                yet_another_random_index = random.randrange(4)
                if yet_another_random_index == 0:
                    self.statement += "Gregorian "
                elif yet_another_random_index == 1:
                    self.statement += "Mayan "
                elif yet_another_random_index == 2:
                    self.statement += "Lunar "
                else:
                    self.statement += "iPhone "
                self.statement += "calendar "
            else:
                self.statement += "atomic clock in Colorado "

        else:
            up_or_down = random.randrange(2)
            if up_or_down == 0:
                self.statement += "not happen "
            else:
                self.statement += "happen twice "

            self.statement += "this year "


    def get_third_block(self):
        self.statement += "because of "

        block_main_parts = ["time zone legislation in ",
                            "a decree by the Pope in the 1500s ",
                            "magnetic field reversal ",
                            "an arbitrary decision by "]

        random_index = random.randrange(len(block_main_parts))
        self.statement += block_main_parts[random_index]

        if random_index == 0:
            up_or_down = random.randrange(3)
            if up_or_down == 0:
                self.statement += "Indiana"
                self.statement += "Benjamin Franklin"
            elif up_or_down == 1:
                self.statement += "Isaac Newton"
            elif up_or_down == 1:
                self.statement += "Arizona"
                self.statement += "Benjamin Franklin"
            elif up_or_down == 1:
                self.statement += "Isaac Newton"
            elif up_or_down == 2:
                self.statement += "Russia"

        elif random_index == 1 or random_index == 2:
            pass

        elif random_index == 3:
            up_or_down = random.randrange(3)
            if up_or_down == 0:
                self.statement += "Benjamin Franklin"
            elif up_or_down == 1:
                self.statement += "Isaac Newton"
            elif up_or_down == 2:
                self.statement += "FDR"

        else:
            up_or_down = random.randrange(6)
            if up_or_down == 0:
                self.statement += "precession "
            elif up_or_down == 1:
                self.statement += "libration "
            elif up_or_down == 2:
                self.statement += "nutation "
            elif up_or_down == 3:
                self.statement += "libation "
            elif up_or_down == 4:
                self.statement += "eccentricity "
            else:
                self.statement += "obliquity "

            self.statement += "of the "

            up_or_down = random.randrange(7)
            if up_or_down == 0:
                self.statement += "Moon"
            elif up_or_down == 1:
                self.statement += "Sun"
            elif up_or_down == 2:
                self.statement += "Earth's axis"
            elif up_or_down == 3:
                self.statement += "equator"
            elif up_or_down == 4:
                self.statement += "prime meridian"
            elif up_or_down == 5:
                self.statement += "International Date Line"
            else:
                self.statement += "Mason-Dixon Line"

        self.statement += "? "

    def get_fourth_block(self):
        self.statement += "Apparently "

        block_main_parts = ["it causes a predictable increase in car accidents. ",
                            "that's why we have leap seconds.",
                            "scientists are really worried.",
                            "it was even more extreme during the ",
                            "there's a proposal to fix it, but it ",
                            "it's getting worse and no one knows why."]

        random_index = random.randrange(len(block_main_parts))
        self.statement += block_main_parts[random_index]

        if random_index == 3:
            up_or_down = random.randrange(4)
            if up_or_down == 0:
                self.statement += "Bronze Age."
            elif up_or_down == 1:
                self.statement += "Ice Age."
            elif up_or_down == 2:
                self.statement += "Cretaceous"
            else:
                self.statement += "1990s."

        elif random_index == 4:
            up_or_down = random.randrange(4)
            if up_or_down == 0:
                self.statement += "will never happen."
            elif up_or_down == 1:
                self.statement += "actually makes things worse."
            elif up_or_down == 2:
                self.statement += "is stalled in Congress."
            else:
                self.statement += "might be unconstitutional."

if __name__ == "__main__":
    print("\n")
    tester = xkcd1930()
    for ii in range(10):
        tester.generate_statement()
    print("\n")
