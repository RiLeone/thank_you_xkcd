#!/usr/bin/env python3 -O
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
import os
import random

import textwrap
import matplotlib.pyplot as pltlib

GFG = None
logger = None
ROOT_LOCATION = os.path.dirname(os.path.abspath(__file__))


def setup():
    """Setup steps"""
    global CFG, logger

    logger = logging.getLogger(__name__)
    logging.basicConfig(level = logging.DEBUG if __debug__ else logging.INFO)
    logger.info("Setting-up environment... logger initialized")
    logger.info("Loading configuration options")
    with open("/".join([ROOT_LOCATION, "config/config.json"]), "r") as fp:
        CFG = json.load(fp)["param"]

    logger.info("Setting up matplotlib")
    for kk, vv in CFG["PLTLIB_RC"].items():
        pltlib.rc(kk, **vv)

    pltlib.xkcd()


class Xkcd1930:
    """xkcd 1930 Strip Main Class Implementation"""
    def __init__(self):
        """Instance constructor

        Each instance is initialized with an empty statement
        """
        self.statement = None


    def generate_image(self) -> bool:
        """Generate current statement image

        :return: bool. Whether image the image has been generated or not.
        """
        if self.statement is None:
            logger.warning(
                "Could not generate image as 'statement' is still void. "
                "Call 'Xkcd1930.generate_statement()' at least once "
                "before calling 'Xkcd1930.generate_image()'."
            )
            return False

        logger.info(f"Generating image for statement: '{self.statement}'")
        wrapped_string = []
        for line in self.statement.splitlines():
            wrapped_string.extend(
                textwrap.wrap(
                    line, width = CFG["LINE_CHAR_LENGTH"], replace_whitespace = False,
                )
            )

        N_LINES = len(wrapped_string)
        fig, axs = pltlib.subplots(figsize = CFG["FIG_SIZE"])
        LINE_SPACING = 1.
        TEXT_START_Y = 1.
        for ii, line in enumerate(wrapped_string):
            logger.debug(line)
            axs.text(0, TEXT_START_Y - ii * LINE_SPACING, line, va = "top")

        axs.set_ylim(
            (
                TEXT_START_Y - (N_LINES + 1) * LINE_SPACING,
                TEXT_START_Y + LINE_SPACING,
            )
        )
        axs.axis("off")
        pltlib.savefig(
            "/".join([CFG["IMG_DIR"], "xkcd1930_calendar-facts_statement"])
        )
        pltlib.close("all")
        return True


    def generate_statement(self):
        """Generate statement and output it to the terminal"""
        self.statement = "Did you know that "
        calls = (
            self.append_first_block,
            self.append_second_block,
            self.append_third_block,
            self.append_fourth_block,
            self.append_trivia_block,
        )
        for call in calls:
            call()

        logger.info(self.statement)


    def append_first_block(self):
        """Append the first block of the sentence to the current statement"""
        FIRST_BLOCK_POOL = (
            "the ",
            "daylight ",
            "leap ",
            "Easter ",
            "Toyota Truck Month ",
            "Shark Week ",
        )
        random_index = self.initiate_block(FIRST_BLOCK_POOL)

        if random_index == 0:
            case_selector = random.randrange(4)
            if case_selector == 0:
                self.add_choice_to_statement(("fall ", "spring "))
                self.statement += "equinox "

            elif case_selector == 1:
                self.add_choice_to_statement(("winter ", "summer "))
                self.add_choice_to_statement(("solstice ", "Olympics "))

            elif case_selector == 2:
                self.add_choice_to_statement(("earliest ", "latest "))
                self.add_choice_to_statement(("sunrise ", "sunset "))

            elif case_selector == 3:
                self.add_choice_to_statement(("harvest ", "super ", "blood "))
                self.statement += "moon "

        elif random_index == 1:
            self.add_choice_to_statement(("saving ", "savings "))
            self.statement += "time "

        elif random_index == 2:
            self.add_choice_to_statement(("day ", "year "))


    def append_second_block(self):
        """Append the second block of the sentence to the current statement"""
        SECOND_BLOCK_POOL = (
            "happens ",
            "drifts out of sync with the ",
            "might ",
        )
        random_index = self.initiate_block(SECOND_BLOCK_POOL)

        if random_index == 0:
            self.add_choice_to_statement(("earlier ", "later ", "at the wrong time "))
            self.statement += "every year "

        elif random_index == 1:
            self.add_choice_to_statement(
                (
                    "sun ",
                    "moon ",
                    "zodiac ",
                    "Gregorian calendar ",
                    "Mayan calendar ",
                    "Lunar calendar ",
                    "iPhone calendar ",
                    "atomic clock in Colorado ",
                )
            )

        else:
            self.add_choice_to_statement(("not happen ", "happen twice "))
            self.statement += "this year "


    def append_third_block(self):
        """Append the third block of the sentence to the current statement"""
        self.statement += "because of "
        THIRD_BLOCK_POOL = (
            "time zone legislation in ",
            "a decree by the Pope in the 1500s",
            "magnetic field reversal",
            "an arbitrary decision by ",
            "the ",
        )
        random_index = self.initiate_block(THIRD_BLOCK_POOL)

        if random_index == 0:
            self.add_choice_to_statement(("Indiana", "Arizona", "Russia"))

        elif random_index in (1, 2):
            pass

        elif random_index == 3:
            self.add_choice_to_statement(("Benjamin Franklin", "Isaac Newton", "FDR"))

        else:
            self.add_choice_to_statement(
                (
                    "precession ",
                    "libration ",
                    "nutation ",
                    "libation ",
                    "eccentricity ",
                    "obliquity ",
                )
            )
            self.statement += "of the "
            self.add_choice_to_statement(
                (
                    "Moon",
                    "Sun",
                    "Earth's axis",
                    "equator",
                    "prime meridian",
                    "International Date Line",
                    "Mason-Dixon Line"
                )
            )

        self.statement += "? "

    def append_fourth_block(self):
        """Append the fourth block of the sentence to the current statement"""
        self.statement += "Apparently "

        FOURTH_BLOCK_POOL = (
            "it causes a predictable increase in car accidents.",
            "that's why we have leap seconds.",
            "scientists are really worried.",
            "it was even more extreme during the ",
            "there's a proposal to fix it, but it ",
            "it's getting worse and no one knows why.",
        )
        random_index = self.initiate_block(FOURTH_BLOCK_POOL)

        if random_index == 3:
            self.add_choice_to_statement(
                (
                    "Bronze Age.",
                    "Ice Age.",
                    "Cretaceous.",
                    "1990s.",
                )
            )

        elif random_index == 4:
            self.add_choice_to_statement(
                (
                    "will never happen.",
                    "actually makes things worse.",
                    "is stalled in Congress.",
                    "might be unconstitutional."
                )
            )


    def append_trivia_block(self):
        """Apped the trivia block, which starts with a new line, to the current statement"""
        self.statement += "\nWhile it may seem like trivia, it "
        self.add_choice_to_statement(
            (
                "causes huge headaches for software developers.",
                "is taken advantage of by high-speed traders.",
                "triggered the 2003 Northeast Blackout.",
                "has to be corrected for by GPS satellites.",
                "is now recognized as a major cause of World War I.",
            )
        )


    def initiate_block(self, pool: tuple) -> int:
        """Initiate block

        Appends beginning of new block to statement and returns used random index

        :param pool: Pool of options starting the block
        :return: int. Chosen index
        """
        random_index = random.randrange(len(pool))
        self.statement += pool[random_index]
        return random_index


    def add_choice_to_statement(self, options: tuple):
        """Add a choice to current statement

        :param options: Available option for choice
        """
        self.statement += random.choice(options)


def main():
    """xkcd Strip 1930 Main Function

    Generate N_STATEMENTS random calendar facts based on the strip's schema.
    The last statement is saved as image (JPG) in the imgs/ subdirectory.
    """
    setup()
    statements_gen = Xkcd1930()
    for _ in range(CFG["N_STATEMENTS"]):
        statements_gen.generate_statement()

    statements_gen.generate_image()


if __name__ == "__main__":
    print(__doc__)
    main()
