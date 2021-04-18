from typing import Dict

import yaml


def get_config() -> Dict:
    from pkg_resources import resource_stream

    return yaml.load(
        resource_stream("power_consumption", "config.yaml"), Loader=yaml.SafeLoader
    )
