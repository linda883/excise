import logging
import pytest
import time


logfilename = time.strftime('%Y%m%d-%H%M%S')
logging.basicConfig(level=logging.DEBUG,
                    filename=logfilename+'.log',
                    filemode='a',
                    format='%(asctime)s-[line:%(lineno)d]-%(levelname)s:%(message)s'
                    )



logging.info("info")
