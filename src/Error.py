from enum import Enum


class Error(Enum):
    FileNotFound = 0
    LabelUsedButNoDefine = 1
    AccessUndefinedMemory = 2
    IllegalRegisterIndex = 3
