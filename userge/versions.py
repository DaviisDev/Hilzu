# pylint: disable=missing-module-docstring
#
# Copyright (C) 2020-2022 by UsergeTeam@Github, < https://github.com/UsergeTeam >.
#
# This file is part of < https://github.com/UsergeTeam/Userge > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/UsergeTeam/Userge/blob/master/LICENSE >
#
# All rights reserved.

from sys import version_info

from hydrogram import __version__ as __pyro_version__  # noqa

from loader import __version__ as __loader_version__  # noqa
from loader.userge import api


__hilzu_version__ = "1.2.1"
__python_version__ = f"{version_info[0]}.{version_info[1]}.{version_info[2]}"
__license__ = "[GNU GPL v3.0](https://github.com/daviisdev/Hilzu/blob/master/LICENSE)"
__copyright__ = "[daviisdev](https://github.com/daviisdev)"


def get_version() -> str:
    return __hilzu_version__


async def get_full_version() -> str:
    core = await api.get_core()
    ver = f"{get_version()}-build.{core.count}"

    return ver + '@' + core.branch
