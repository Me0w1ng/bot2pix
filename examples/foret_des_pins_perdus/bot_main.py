import atexit
import datetime
import os
from core.bot import ResourceFarmer


def tearDown(thread):
    thread.interrupt()
    thread.join()


if __name__ == "__main__":
    from core import Zone, env
    import logging

    work_dir = os.path.dirname(os.path.abspath(__file__))

    log_file = os.path.join(work_dir, 'bot.log')
    logging.basicConfig(filename=log_file,
                        level=logging.INFO,
                        format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
                        datefmt='%Y-%m-%d:%H:%M:%S')

    patterns_dir = os.path.join(work_dir, "patterns")
    saves_dir = os.path.join(work_dir, 'saves')
    now = datetime.datetime.now()

    spell = {
        "range": 13,
        "nbr": 4,
        "shortcut": "z"
    }

    character_name = "John-shooter"

    zone_file_path = os.path.join(saves_dir, "frifri_30_11_2020.yaml")
    otomai = Zone("otomai")
    zone_zaap_coords = (-78, -41)

    otomai.loadFromFile(zone_file_path, patterns_dir)

    bot = ResourceFarmer(otomai, zone_zaap_coords, spell, work_dir, character_name)
    bot.mapChangeTimeOut = 12
    bot.memoTime = 60 * 5
    bot.famPatternThreshold = 0.75

    atexit.register(tearDown, bot)
    bot.start()
    bot.join()
    env.focusIDEWindow()
