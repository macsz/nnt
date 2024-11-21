import logging

from rich.logging import RichHandler


logging.basicConfig(
    level="INFO",
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)],
)

log = logging.getLogger("rich")

loggers_3rd_party = ["PIL", "fvcore.nn.jit_analysis", "matplotlib.font_manager"]
for logger_3rd_party in loggers_3rd_party:
    logging.getLogger(logger_3rd_party).setLevel(logging.ERROR)
