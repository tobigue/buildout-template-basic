import logging
import logging.handlers

import options


root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)

formatter = logging.Formatter(' - '.join(['[%(asctime)s',
                                          '%(relativeCreated).3f]',
                                          '%(name)s',
                                          '%(levelname)s',
                                          '%(message)s']))

logfile_handler = logging.handlers.TimedRotatingFileHandler(options.logfile,
    when='midnight', interval=1, backupCount=10)
logfile_handler.setLevel(logging.INFO)
logfile_handler.setFormatter(formatter)
root_logger.addHandler(logfile_handler)
