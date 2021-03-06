PREFIX = 'CPyPy_'  # Python wrappers
NATIVE_PREFIX = 'CPyDef_'  # Native functions etc.
REG_PREFIX = 'cpy_r_'  # Registers
STATIC_PREFIX = 'CPyStatic_'  # Static variables (for literals etc.)
TYPE_PREFIX = 'CPyType_'  # Type object struct

ENV_ATTR_NAME = '__mypyc_env__'

MAX_SHORT_INT = (1 << 62) - 1

TOP_LEVEL_NAME = '__top_level__'  # Special function representing module top level
