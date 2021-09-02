import logging

#It generates logs for the test cases
class LogGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="D:\\User\\Rajeshwari\\EntityOnboarding\\Logs\\automation.log",
                            format='%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
