from .birth import BirthCreateSerializer, BirthDetailSerializer
from .breed import BreedSerializer
from .category import CategorySerializer
from .feed import FeedSerializer
from .group import GroupDetailSerializer, GroupSerializer, GroupUserDetailSerializer
from .lots import LotsSerializer
from .permission import PermissionSerializer
from .pregnancyDiagnosis import PregnancyDiagnosisDetailSerializer, PregnancyDiagnosisSerializer
from .shearing import ShearingSerializer, ShearingDetailSerializer
from .sheep import SheepCreateNewbornSerializer, SheepDetailSerializer, SheepSerializer
from .user import (
    UserCreateSerializer,
    UserInfoSerializer,
    UserPasswordUpdateSerializer,
    UserSerializer,
    UserUpdateSerializer,
)
