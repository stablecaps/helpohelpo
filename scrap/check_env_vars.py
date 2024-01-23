import logging
import os
import sys

LOG = logging.getLogger(__name__)


def check_env_vars():
    """Check aws & github env variables required to run this script."""
    AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")

    if (AWS_ACCESS_KEY_ID is None) or (AWS_SECRET_ACCESS_KEY is None):
        LOG.critical("AWS access keys not set. Exiting..")
        sys.exit(0)
    LOG.info("AWS config good. Continuing...")
