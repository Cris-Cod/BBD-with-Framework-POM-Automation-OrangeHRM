import logging

import pytest



@pytest.mark.usefixtures("setup")
class BaseClass:


    def loggen(self):
        logger = logging.getLogger()
        fileHandler = logging.FileHandler('./Logs/logfile.log', mode='w')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        logger.setLevel(logging.ERROR)

        return logger