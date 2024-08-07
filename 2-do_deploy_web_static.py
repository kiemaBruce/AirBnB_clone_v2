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
    exit_statuses = []  # To keep track of all commands
    archive_name = archive_path.split(sep='/')[-1]
    remote_location = f"/tmp/{archive_name}"
    # upload the archive
    res = put(local_path=archive_path, remote_path=remote_location)
    if res.failed:
        return False
    dir_name = f"/data/web_static/releases/{archive_name.split(sep='.')[0]}"
    # create directory
    res = run(f'sudo mkdir -p {dir_name}', warn_only=True)
    exit_statuses.append(res.failed)
    # extract
    res = run(
                f"sudo tar -xzf /tmp/{archive_name} -C {dir_name}",
                warn_only=True
              )
    exit_statuses.append(res.failed)
    # delete archive
    res = run(f'sudo rm -f /tmp/{archive_name}', warn_only=True)
    exit_statuses.append(res.failed)
    # move files to outer archive
    current = (
            f"/data/web_static/releases/" +
            f"{archive_name.split(sep='.')[0]}/web_static/*")
    new = f"/data/web_static/releases/{archive_name.split(sep='.')[0]}"
    run(f"sudo mv {current} {new}")
    run(f'sudo rm -rf {new}/web_static')  # delete the old (inner) directory
    # delete symbolic link
    res = run('sudo rm -f /data/web_static/current', warn_only=True)
    exit_statuses.append(res.failed)
    res = run(f'ln -s {dir_name} /data/web_static/current', warn_only=True)
    exit_statuses.append(res.failed)
    for exit_status in exit_statuses:
        if exit_status:
            return False
    return True
