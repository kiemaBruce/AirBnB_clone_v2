#!/usr/bin/python3
# Generates a .tgz archive

from datetime import datetime
from fabric.api import *


def do_pack():
    """Creates a .tgz archive

    Returns:
        str: the archive path if the archive has been correctly generated,
        otherwise it returns None
    """
    local('mkdir -p versions')
    now = datetime.now()
    archive_name = "web_static_"
    archive_name = ("web_static_" +
                    f"{now.year}" +
                    f"{now.month}" +
                    f"{now.day}" +
                    f"{now.hour}" +
                    f"{now.minute}" +
                    f"{now.second}" +
                    ".tgz"
                    )
    result = local(f'tar -zcvf ./versions/{archive_name} web_static')
    if result.succeeded:
        return archive_name
    return None
