"""Top-level package for chaosxargs"""
from typing import List

from chaoslib.discovery.discover import (
    discover_actions,
    discover_activities,
    discover_probes,
    initialize_discovery_result,
)
from chaoslib.types import DiscoveredActivities, Discovery
from logzero import logger

name = "chaosxargs"
__author__ = """Manuel Castellin"""
__email__ = "manuel@castellinconsulting.com"
__version__ = "0.0.1"
__all__ = [
    "discover",
    "__version__",
]


def discover(discover_system: bool = True) -> Discovery:
    # pylint: disable=unused-argument
    discovery = initialize_discovery_result("chaosxargs", __version__, "chaosxargs")
    discovery["activities"].extend(load_exported_activities())
    return discovery


def load_exported_activities() -> List[DiscoveredActivities]:
    """
    Extract metadata from actions and probes exposed by this extension.
    """
    activities = []
    activities.extend(discover_activities("chaosxargs.control", "control"))

    return activities
