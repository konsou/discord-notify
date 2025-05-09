from enum import Enum


class MessageLevel(Enum):
    INFO = "info"
    ERROR = "error"


WEBHOOK_ENV_NAME = {
    MessageLevel.INFO: "WEBHOOK_URL",
    MessageLevel.ERROR: "WEBHOOK_URL_ERROR",
}
