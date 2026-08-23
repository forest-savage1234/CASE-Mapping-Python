from datetime import datetime
from typing import Any, Dict, List, Optional, Union
from warnings import warn

from cdo_local_uuid import local_uuid

from ..base import Facet, UcoInherentCharacterizationThing, UcoObject
from .action import Action
from .core import Relationship
from .identity import Identity
from .location import Location
from .types import Dictionary
