Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import numpy
>>> import numpy as np
>>> dir(np)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_distributor_init', '_globals', '_import_tools', '_mat', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'bench', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'prod', 'product', 'promote_types', 'ptp', 'put', 'putmask', 'pv', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> np_dir = dir(np)
>>> len(np_dir)
611
>>> list_1 = []
>>> arr_1 = np.array()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    arr_1 = np.array()
TypeError: Required argument 'object' (pos 1) not found
>>> arr_1 = np.array([])
>>> list_1
[]
>>> arr_1
array([], dtype=float64)
>>> import sys
>>> sys.getsizeof(list_1)
64
>>> sys.getsizeof(arr_1)
96
>>> for i in range(1000):
	list_1.append(i)

	
>>> for i in range(1000):
	arr_1.append(i)

	
Traceback (most recent call last):
  File "<pyshell#17>", line 2, in <module>
    arr_1.append(i)
AttributeError: 'numpy.ndarray' object has no attribute 'append'
>>> arr_1 = np.array([i for i in range(1000))
		 
SyntaxError: invalid syntax
>>> arr_1 = np.array([i for i in range(1000)])
>>> len(list_1)
1000
>>> len(arr_1)
1000
>>> sys.getsizeof(list_1)
9024
>>> sys.getsizeof(arr_1)
4096
>>> a = [2,3,4,5]
>>> b = [6,5,4,3]
>>> a+b
[2, 3, 4, 5, 6, 5, 4, 3]
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(100)
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>> arr_2 = np.array([1,2,3,4,5,'Hi','Bye'])
>>> print(arr_2)
['1' '2' '3' '4' '5' 'Hi' 'Bye']
>>> arr_2 = np.array([1,2,3,4,5,'Hi','Bye',10.5])
>>> print(arr_2)
['1' '2' '3' '4' '5' 'Hi' 'Bye' '10.5']
>>> arr_2 = np.array([1,2,3,4,5,10.5])
>>> print(arr_2)
[  1.    2.    3.    4.    5.   10.5]
>>> np.arange(10)
array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> np.arange(10,50)
array([10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,
       27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43,
       44, 45, 46, 47, 48, 49])
>>> np.arange(10,51,2)
array([10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42,
       44, 46, 48, 50])
>>> np.linspace(5)
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    np.linspace(5)
TypeError: linspace() missing 1 required positional argument: 'stop'
>>> np.linspace(1,6)
array([ 1.        ,  1.10204082,  1.20408163,  1.30612245,  1.40816327,
        1.51020408,  1.6122449 ,  1.71428571,  1.81632653,  1.91836735,
        2.02040816,  2.12244898,  2.2244898 ,  2.32653061,  2.42857143,
        2.53061224,  2.63265306,  2.73469388,  2.83673469,  2.93877551,
        3.04081633,  3.14285714,  3.24489796,  3.34693878,  3.44897959,
        3.55102041,  3.65306122,  3.75510204,  3.85714286,  3.95918367,
        4.06122449,  4.16326531,  4.26530612,  4.36734694,  4.46938776,
        4.57142857,  4.67346939,  4.7755102 ,  4.87755102,  4.97959184,
        5.08163265,  5.18367347,  5.28571429,  5.3877551 ,  5.48979592,
        5.59183673,  5.69387755,  5.79591837,  5.89795918,  6.        ])
>>> len(np.linspace(1,5))
50
>>> np.linspace(1,5,10)
array([ 1.        ,  1.44444444,  1.88888889,  2.33333333,  2.77777778,
        3.22222222,  3.66666667,  4.11111111,  4.55555556,  5.        ])
>>> np.linspace(1,5,10,False)
array([ 1. ,  1.4,  1.8,  2.2,  2.6,  3. ,  3.4,  3.8,  4.2,  4.6])
>>> np.linspace(1,5,10,False,True)
(array([ 1. ,  1.4,  1.8,  2.2,  2.6,  3. ,  3.4,  3.8,  4.2,  4.6]), 0.40000000000000002)
>>> np.random
<module 'numpy.random' from 'C:\\Python36\\lib\\site-packages\\numpy\\random\\__init__.py'>
>>> np.random.random(10)
array([ 0.96171146,  0.26647629,  0.87418948,  0.27367578,  0.4901476 ,
        0.68352019,  0.14334226,  0.47563421,  0.67430555,  0.80699048])
>>> np.random.random(10,12)
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    np.random.random(10,12)
  File "mtrand.pyx", line 814, in mtrand.RandomState.random_sample
TypeError: random_sample() takes at most 1 positional argument (2 given)
>>> np.random.random([10,20])
array([[ 0.80779758,  0.29255853,  0.76792742,  0.14497677,  0.88507861,
         0.08210091,  0.06948662,  0.01345827,  0.29362007,  0.43309256,
         0.88749582,  0.82046552,  0.24979038,  0.53907413,  0.74913396,
         0.94113203,  0.93538892,  0.51044128,  0.24054112,  0.95455524],
       [ 0.90877764,  0.33110871,  0.71987725,  0.41765231,  0.74169873,
         0.62930317,  0.30436711,  0.08060943,  0.80020406,  0.07593998,
         0.19249182,  0.01248421,  0.69421309,  0.87907123,  0.78640295,
         0.0702344 ,  0.88137344,  0.2677047 ,  0.40199771,  0.81477239],
       [ 0.34402092,  0.68296165,  0.66382733,  0.29851164,  0.19662011,
         0.72734628,  0.48088915,  0.57286762,  0.1682498 ,  0.45289791,
         0.55003187,  0.21282613,  0.42787553,  0.56987818,  0.43622082,
         0.90470846,  0.95931939,  0.66104091,  0.94297695,  0.60953587],
       [ 0.36704117,  0.98856368,  0.45331363,  0.94728152,  0.63043164,
         0.34782673,  0.46474082,  0.73228762,  0.04244   ,  0.20278364,
         0.26649858,  0.28024349,  0.94009871,  0.04116445,  0.57076936,
         0.35462211,  0.49171687,  0.89383559,  0.60948066,  0.61964364],
       [ 0.25964828,  0.47611725,  0.11662116,  0.28025654,  0.54990356,
         0.9746993 ,  0.91288317,  0.42966067,  0.25462337,  0.93835593,
         0.1175908 ,  0.51880406,  0.497492  ,  0.31585231,  0.19050678,
         0.51892607,  0.1003208 ,  0.41372306,  0.404139  ,  0.06880655],
       [ 0.71271426,  0.8883006 ,  0.67054599,  0.66009835,  0.88964488,
         0.2893572 ,  0.50676082,  0.39595663,  0.64178503,  0.92837783,
         0.36369758,  0.863597  ,  0.94799903,  0.98976158,  0.67006995,
         0.06749391,  0.08508152,  0.35676306,  0.96919849,  0.13154136],
       [ 0.03692997,  0.88400581,  0.93515493,  0.14655546,  0.53672278,
         0.88456994,  0.5333354 ,  0.13463362,  0.53797506,  0.15683237,
         0.86052189,  0.23664155,  0.53868777,  0.54463303,  0.32805178,
         0.94473889,  0.56426666,  0.08139199,  0.06046652,  0.64897423],
       [ 0.21710417,  0.84551751,  0.04544612,  0.08798441,  0.11662142,
         0.61814995,  0.48238642,  0.27031886,  0.39499076,  0.53897419,
         0.71860715,  0.10090662,  0.16820549,  0.6584904 ,  0.82493305,
         0.09957474,  0.24053333,  0.58752431,  0.11695121,  0.79603912],
       [ 0.08551983,  0.78499977,  0.45751343,  0.12481486,  0.03554531,
         0.04551677,  0.21593045,  0.70462096,  0.67033666,  0.39576014,
         0.98983127,  0.75828582,  0.47106475,  0.94062205,  0.15368134,
         0.42590743,  0.8939055 ,  0.27685396,  0.61483995,  0.11236017],
       [ 0.93309911,  0.35481638,  0.20255998,  0.63202871,  0.77322133,
         0.27303632,  0.74733684,  0.05176407,  0.29183052,  0.51768588,
         0.81470258,  0.06208873,  0.49499493,  0.50347163,  0.48259527,
         0.23614617,  0.7160107 ,  0.48357107,  0.43756223,  0.15498386]])
>>> x = np.random.random([10,20])
>>> len(x)
10
>>> x = np.random.random([10,2])
>>> x
array([[ 0.00289397,  0.82781535],
       [ 0.25027898,  0.8555541 ],
       [ 0.2048835 ,  0.28837092],
       [ 0.74029487,  0.83685794],
       [ 0.44185155,  0.37300685],
       [ 0.70564554,  0.40144604],
       [ 0.54904456,  0.04196221],
       [ 0.94616332,  0.57383018],
       [ 0.55443777,  0.19371236],
       [ 0.05595423,  0.4049904 ]])
>>> x = np.random.random([10,2,1])
>>> x
array([[[ 0.25742127],
        [ 0.52706038]],

       [[ 0.01851033],
        [ 0.24280267]],

       [[ 0.21357438],
        [ 0.93230909]],

       [[ 0.87047704],
        [ 0.18786174]],

       [[ 0.37281144],
        [ 0.15903563]],

       [[ 0.31409697],
        [ 0.80674489]],

       [[ 0.2040859 ],
        [ 0.44464751]],

       [[ 0.51336284],
        [ 0.06810015]],

       [[ 0.28832843],
        [ 0.41948265]],

       [[ 0.6307757 ],
        [ 0.61493888]]])
>>> np.random.random(10) * 20
array([  0.39454239,   5.5141256 ,  11.45076386,   8.47954467,
        15.20259668,  12.78186284,  17.53208188,   7.06771269,
         4.10163606,   7.43109598])
>>> np.random.randint(10)
7
>>> np.random.randint([0,10])
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    np.random.randint([0,10])
  File "mtrand.pyx", line 981, in mtrand.RandomState.randint
TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'
>>> np.random.randint(0,10)
5
>>> np.random.randint(10,20)
13
>>> np.random.randint(10,20,5)
array([16, 14, 19, 19, 13])
>>> x = np.array([[1,2,3],[4,5,6],[7,8,9]])
>>> y = [[1,2,3],[4,5,6],[7,8,9]]
>>> print(x)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> print(y)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> x.transpose
<built-in method transpose of numpy.ndarray object at 0x000001B149C95C10>
>>> x.transpose()
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
>>> np.ndarray(5)
array([  2.12199579e-314,   6.36598737e-314,   1.06099790e-313,
         1.48539705e-313,   1.90979621e-313])
>>> np.ndarray(5, buffer = np.array([1,2,3,4,5]))
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    np.ndarray(5, buffer = np.array([1,2,3,4,5]))
TypeError: buffer is too small for requested array
>>> np.ndarray((5,), buffer = np.array([1,2,3,4,5]))
Traceback (most recent call last):
  File "<pyshell#70>", line 1, in <module>
    np.ndarray((5,), buffer = np.array([1,2,3,4,5]))
TypeError: buffer is too small for requested array
>>> np.ndarray((2,), buffer = np.array([1,2,3,]))
Traceback (most recent call last):
  File "<pyshell#71>", line 1, in <module>
    np.ndarray((2,), buffer = np.array([1,2,3,]))
TypeError: buffer is too small for requested array
>>> 
KeyboardInterrupt
>>> np.ndarray((2,), buffer=np.array([1,2,3]))
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    np.ndarray((2,), buffer=np.array([1,2,3]))
TypeError: buffer is too small for requested array
>>> np.ndarray((2,), buffer=np.array([1,2,3]), offset=np.int_().itemsize)
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    np.ndarray((2,), buffer=np.array([1,2,3]), offset=np.int_().itemsize)
TypeError: buffer is too small for requested array
>>> np.ndarray(5)
array([  2.12199579e-314,   6.36598737e-314,   1.06099790e-313,
         1.48539705e-313,   1.90979621e-313])
>>> np.ndarray([5,2])
array([[  0.39454239,   5.5141256 ],
       [ 11.45076386,   8.47954467],
       [ 15.20259668,  12.78186284],
       [ 17.53208188,   7.06771269],
       [  4.10163606,   7.43109598]])
>>> np.ndarray([5,1])
array([[  2.12199579e-314],
       [  6.36598737e-314],
       [  1.06099790e-313],
       [  1.48539705e-313],
       [  1.90979621e-313]])
>>> np.ndarray([5,2])
array([[  0.39454239,   5.5141256 ],
       [ 11.45076386,   8.47954467],
       [ 15.20259668,  12.78186284],
       [ 17.53208188,   7.06771269],
       [  4.10163606,   7.43109598]])
>>> np.ndarray([5,2,1])
array([[[  0.39454239],
        [  5.5141256 ]],

       [[ 11.45076386],
        [  8.47954467]],

       [[ 15.20259668],
        [ 12.78186284]],

       [[ 17.53208188],
        [  7.06771269]],

       [[  4.10163606],
        [  7.43109598]]])
>>> np.ndarray([5,2,3])
array([[[  9.19427913e-312,   9.19427600e-312,   6.95319417e-310],
        [  6.95319417e-310,   6.95319417e-310,   6.95319417e-310]],

       [[  6.95319417e-310,   6.95319417e-310,   6.95319417e-310],
        [  6.95319417e-310,   6.95319417e-310,   6.95319417e-310]],

       [[  6.95319417e-310,   6.95319417e-310,   6.95319417e-310],
        [  6.95319417e-310,   6.95319417e-310,   6.95319417e-310]],

       [[  6.95319417e-310,   6.95319417e-310,   6.95319417e-310],
        [  6.95319417e-310,   6.95319417e-310,   0.00000000e+000]],

       [[  6.95319417e-310,   6.95319417e-310,   0.00000000e+000],
        [  6.95319416e-310,  -3.93825686e+170,   2.12199579e-314]]])
>>> np.ndarray([5,2,3], dtype='int64')
array([[[    1860942735328,     1860942180480,       41204743904],
        [                0,             34304,       41204743492]],

       [[                0,     1860942670928,                 0],
        [                0,                 0,     1860942283856]],

       [[                5,   140733939322880,              4096],
        [                5,   140733939357884,                 2]],

       [[                0,                 0,            270336],
        [                0,                -1,                 0]],

       [[22518393277644867, 31244169099083897, 25895929788956782],
        [32369948744220740, 34340411021394012, 31525394966446189]]], dtype=int64)
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x.shape
(3, 3)
>>> x.ndim
2
>>> x.ravel
<built-in method ravel of numpy.ndarray object at 0x000001B149C95C10>
>>> x.ravel()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x.flatten()
array([1, 2, 3, 4, 5, 6, 7, 8, 9])
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x.ravel('F')
array([1, 4, 7, 2, 5, 8, 3, 6, 9])
>>> np.ones(5)
array([ 1.,  1.,  1.,  1.,  1.])
>>> np.ones([5,2])
array([[ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.],
       [ 1.,  1.]])
>>> np.ones([5,2,5])
array([[[ 1.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.,  1.]],

       [[ 1.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.,  1.]],

       [[ 1.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.,  1.]],

       [[ 1.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.,  1.]],

       [[ 1.,  1.,  1.,  1.,  1.],
        [ 1.,  1.,  1.,  1.,  1.]]])
>>> np.zeros([5,2,5])
array([[[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]],

       [[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]],

       [[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]],

       [[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]],

       [[ 0.,  0.,  0.,  0.,  0.],
        [ 0.,  0.,  0.,  0.,  0.]]])
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x.mean
<built-in method mean of numpy.ndarray object at 0x000001B149C95C10>
>>> x.mean()
5.0
>>> x.std()
2.5819888974716112
>>> x.max()
9
>>> x.min()
1
>>> x.T()
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    x.T()
TypeError: 'numpy.ndarray' object is not callable
>>> x.T
array([[1, 4, 7],
       [2, 5, 8],
       [3, 6, 9]])
>>> x
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> x.any
<built-in method any of numpy.ndarray object at 0x000001B149C95C10>
>>> x.any()
True
>>> x.all()
True
>>> a = [1,2,3,4,5,6]
>>> all(a)
True
>>> any(a)
True
>>> a = 5
>>> any(a)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    any(a)
TypeError: 'int' object is not iterable
>>> 
