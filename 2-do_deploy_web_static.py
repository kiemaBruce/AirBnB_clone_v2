#!/usr/bin/python3
# Distributes an archive to web servers

from fabric.api import *


env.user = 'ubuntu'
env.hosts = ['54.234.93.82', '52.91.150.83']


def do_deploy(archive_path):
    """ Deploys an archive to web_servers

    Args:
        archive_path (str): path to the archive that's to be deployed to web
                            servers.
    Returns:
        bool: True if all operations have been done correctly, otherwise
              returns False.
    """
    archive_name = archive_path.split(sep='/')[-1]
    remote_location = f"/tmp/{archive_name}"
    try:
        # upload the archive
        put(local_path=archive_path, remote_path=remote_location)
        # create directory
        dir_name = (
                    f"/data/web_static/releases/" +
                    f"{archive_name.split(sep='.')[0]}")
        run(f'sudo mkdir -p {dir_name}')
        local(f'sudo mkdir -p {dir_name}')
        # extract
        run(f"sudo tar -xzf /tmp/{archive_name} -C {dir_name}")
        local(f"sudo tar -xzf /tmp/{archive_name} -C {dir_name}")
        # delete archive
        run(f'sudo rm -f /tmp/{archive_name}')
        local(f'sudo rm -f /tmp/{archive_name}')
        # move files to outer directory
        current = (
                f"/data/web_static/releases/" +
                f"{archive_name.split(sep='.')[0]}/web_static/*")
        new = f"/data/web_static/releases/{archive_name.split(sep='.')[0]}"
        run(f"sudo mv {current} {new}")
        local(f"sudo mv {current} {new}")
        # delete the old (inner) directory
        run(f'sudo rm -rf {new}/web_static')
        local(f'sudo rm -rf {new}/web_static')
        # delete old symbolic link
        run('sudo rm -f /data/web_static/current')
        local('sudo rm -f /data/web_static/current')
        # create new symbolic link
        run(f'ln -s {dir_name} /data/web_static/current')
        local(f'ln -s {dir_name} /data/web_static/current')
    except Exception as e:
        return False
    else:
        return True
