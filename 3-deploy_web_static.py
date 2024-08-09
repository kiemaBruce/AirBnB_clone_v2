#!/usr/bin/python3
# Creates an archive and deploys code to web servers


from fabric.api import *
import os
import sys

cwd = os.getcwd()
sys.path.append(cwd)
env.hosts = ['54.234.93.82', '52.91.150.83']
archive_path = __import__('1-pack_web_static').do_pack()
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """Creates and distributes an archive to web servers.
    """
    if archive_path is None:
        return False
    # return execute(do_deploy, archive_path)
    return do_deploy(archive_path)
