"""Constants for deltadore_tydom integration."""
from logging import Logger, getLogger

LOGGER: Logger = getLogger(__package__)

# This is the internal name of the integration, it should also match the directory
# name for the integration.
DOMAIN = "deltadore_tydom"
NAME = "Delta Dore TYDOM"

CONF_TYDOM_PASSWORD = "tydom_password"
CONF_ZONES_HOME = "zones_home"
CONF_ZONES_AWAY = "zones_away"
