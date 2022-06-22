#! /usr/bin/env python3 -O
"""
    xkcd Strip 1930
    ===============

    http://xkcd.com/1930

    Calendar facts. Pretty naive implementation.

    MIT License

    Copyright (c) 2017 Alessandro Schaer

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
"""
__version__ = "1.0.0"

import json
import logging
import random

import textwrap as textwrap
import matplotlib.pyplot as pltlib

with open("config.json", "r") as fp:
    CFG = json.load(fp)["param"]

logger = logging.getLogger(__name__)
logging.basicConfig(level = logging.DEBUG if __debug__ else logging.INFO)


def setup():
    """Setup steps"""
    for kk, vv in CFG["PLTLIB_RC"].items():
        pltlib.rc(kk, **vv)

    pltlib.xkcd()


class Xkcd1930:
    """xkcd 1930 Strip Main Class Implementation"""
    FIRST_BLOCK_POOL = (
        "the ",
        "daylight ",
        "leap ",
        "Easter ",
        "Toyota Truck Month ",
        "Shark Week ",
    )

    def __init__(self):
        """Instance constructor

        Each instance is initialized with an empty statement
        """
        self.statement = None


    def generate_image(self):
        """Generate current statement image"""
        if self.statement is None:
            logger.warning(
                "Could not generate image as 'statement' is still void. "
                "Call 'Xkcd1930.generate_statement()' at least once "
                "before calling 'Xkcd1930.generate_image()'."
            )
            return

        logger.info(f"Generating image for statement: '{self.statement}'")
        wrapped_string = textwrap.wrap(self.statement, CFG["LINE_CHAR_LENGTH"])

        fig = pltlib.figure(figsize = CFG["FIG_SIZE"])
        fig_height = CFG["FIG_SIZE"][1]
        for ii, line in enumerate(wrapped_string):
            logger.debug(line)
            pltlib.text(0, 0.9 - ii * fig_height / 3, line)

        pltlib.axis('off')
        pltlib.savefig(
            "/".join([CFG["IMG_DIR"], "xkcd1930_calendar-facts_statement"])
        )
        pltlib.show()


    def generate_statement(self):
        """Generate statement and output it to the terminal"""
        self.statement = "Did you know that "
        self.append_first_block()
        self.get_second_block()
        self.get_third_block()
        self.get_fourth_block()
        logger.info(self.statement)


    def append_first_block(self):
        """Append the first block of the sentence to the current statement"""
        random_index = random.randrange(len(self.FIRST_BLOCK_POOL))
        self.statement += self.FIRST_BLOCK_POOL[random_index]

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
        block_main_parts = (
            "happens ",
            "drifts out of sync with the ",
            "might ",
        )

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

        elif random_index == 1:
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

        block_main_parts = (
            "time zone legislation in ",
            "a decree by the Pope in the 1500s",
            "magnetic field reversal",
            "an arbitrary decision by ",
        )

        random_index = random.randrange(len(block_main_parts))
        self.statement += block_main_parts[random_index]

        if random_index == 0:
            up_or_down = random.randrange(3)
            if up_or_down == 0:
                self.statement += "Indiana"
            elif up_or_down == 1:
                self.statement += "Arizona"
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

        block_main_parts = (
            "it causes a predictable increase in car accidents. ",
            "that's why we have leap seconds.",
            "scientists are really worried.",
            "it was even more extreme during the ",
            "there's a proposal to fix it, but it ",
            "it's getting worse and no one knows why.",
        )

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


def main():
    """xkcd Strip 1930 Main Function

    Generate 10 random calendar facts based on the strip's schema. The last statement is saved as
    image (JPG) in the imgs/ subdirectory.
    """
    setup()

    tester = Xkcd1930()
    for ii in range(10):
        tester.generate_statement()

    print("\n")
    tester.generate_image()


if __name__ == "__main__":
    print(__doc__)
    main()
