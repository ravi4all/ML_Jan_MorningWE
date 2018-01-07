Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print("Hello")
Hello
>>> a = 10
>>> a = 10.5
>>> type(a)
<class 'float'>
>>> a = "Hello"
>>> type(a)
<class 'str'>
>>> a = True
>>> type(a)
<class 'bool'>
>>> for i in range(0,10):
	print(i)

	
0
1
2
3
4
5
6
7
8
9
>>> a = "Hello World"
>>> a[:]
'Hello World'
>>> a[0:]
'Hello World'
>>> a[:50]
'Hello World'
>>> a[0]
'H'
>>> a[0:6]
'Hello '
>>> a[:0]
''
>>> a[-1]
'd'
>>> a[:-1]
'Hello Worl'
>>> a[0:10:2]
'HloWr'
>>> a[::2]
'HloWrd'
>>> a[::-1]
'dlroW olleH'
>>> a = [1,2,3,4,5,6,7,8.5,'Hello',True]
>>> a[0] = "Bye"
>>> a
['Bye', 2, 3, 4, 5, 6, 7, 8.5, 'Hello', True]
>>> b = (1,2,3,4,5,6,7,8.5,'Hello',True)
>>> b[0]
1
>>> b[0:5]
(1, 2, 3, 4, 5)
>>> a
['Bye', 2, 3, 4, 5, 6, 7, 8.5, 'Hello', True]
>>> b
(1, 2, 3, 4, 5, 6, 7, 8.5, 'Hello', True)
>>> b[0] = "Bye"
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    b[0] = "Bye"
TypeError: 'tuple' object does not support item assignment
>>> c = {}
>>> type(c)
<class 'dict'>
>>> c = {1,2}
>>> type(c)
<class 'set'>
>>> d = {"id" : 1, "name" : "Ram", "age" : 17}
>>> d[0]
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    d[0]
KeyError: 0
>>> d['id']
1
>>> d['name']
'Ram'
>>> for data in d:
	print(data)

	
id
name
age
>>> d.values()
dict_values([1, 'Ram', 17])
>>> d.keys()
dict_keys(['id', 'name', 'age'])
>>> d.items()
dict_items([('id', 1), ('name', 'Ram'), ('age', 17)])
>>> for data in d.items():
	print(data)

	
('id', 1)
('name', 'Ram')
('age', 17)
>>> c
{1, 2}
>>> c = {1,2,3,4}
>>> e = {5,4,6,2}
>>> c.intersection(e)
{2, 4}
>>> c.union(e)
{1, 2, 3, 4, 5, 6}
>>> a
['Bye', 2, 3, 4, 5, 6, 7, 8.5, 'Hello', True]
>>> a = [ 2, 3, 4, 2, 6, 7, 2, 5, 3, 2]
>>> s = { 2, 3, 4, 2, 6, 7, 2, 5, 3, 2}
>>> s
{2, 3, 4, 5, 6, 7}
>>> a
[2, 3, 4, 2, 6, 7, 2, 5, 3, 2]
>>> set(a)
{2, 3, 4, 5, 6, 7}
>>> listset(a)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    listset(a)
NameError: name 'listset' is not defined
>>> list(set(a))
[2, 3, 4, 5, 6, 7]
>>> a = "10"
>>> a = '10'
>>> a = 'Hello'
>>> for i in range(5):
	print(a)

	
Hello
Hello
Hello
Hello
Hello
>>> print(a*5)
HelloHelloHelloHelloHello
>>> print(a+'\n'*5)
Hello





>>> a = "Hello\n"
>>> print(a*5)
Hello
Hello
Hello
Hello
Hello

>>> num_1 = input("Enter first num : ")
Enter first num : 12
>>> num_2 = input("Enter second num : ")
Enter second num : 13
>>> num_1 + num_2
'1213'
>>> int(num_1) + int(num_2)
25
>>> int(num_1 + num_2)
1213
>>> import random
>>> random.random(0,10)
Traceback (most recent call last):
  File "<pyshell#78>", line 1, in <module>
    random.random(0,10)
TypeError: random() takes no arguments (2 given)
>>> random.random()
0.010283335088384193
>>> random.random()
0.4129131323251445
>>> random.random()
0.4143730528824068
>>> random.random()
0.5405882970523783
>>> random.random()
0.5761313299385693
>>> random.random() * 10
0.9030255011274413
>>> random.random() * 10
7.90816743267273
>>> random.random() * 10
9.930413855602469
>>> random.random() * 10
7.216785237567114
>>> random.randint(0,10)
0
>>> random.randint(0,10)
5
>>> random.randint(0,10)
9
>>> random.randint(0,10)
10
>>> pygame.init()
Traceback (most recent call last):
  File "<pyshell#92>", line 1, in <module>
    pygame.init()
NameError: name 'pygame' is not defined
>>> import numpy
>>> dir(numpy)
['ALLOW_THREADS', 'AxisError', 'BUFSIZE', 'CLIP', 'ComplexWarning', 'DataSource', 'ERR_CALL', 'ERR_DEFAULT', 'ERR_IGNORE', 'ERR_LOG', 'ERR_PRINT', 'ERR_RAISE', 'ERR_WARN', 'FLOATING_POINT_SUPPORT', 'FPE_DIVIDEBYZERO', 'FPE_INVALID', 'FPE_OVERFLOW', 'FPE_UNDERFLOW', 'False_', 'Inf', 'Infinity', 'MAXDIMS', 'MAY_SHARE_BOUNDS', 'MAY_SHARE_EXACT', 'MachAr', 'ModuleDeprecationWarning', 'NAN', 'NINF', 'NZERO', 'NaN', 'PINF', 'PZERO', 'PackageLoader', 'RAISE', 'RankWarning', 'SHIFT_DIVIDEBYZERO', 'SHIFT_INVALID', 'SHIFT_OVERFLOW', 'SHIFT_UNDERFLOW', 'ScalarType', 'Tester', 'TooHardError', 'True_', 'UFUNC_BUFSIZE_DEFAULT', 'UFUNC_PYVALS_NAME', 'VisibleDeprecationWarning', 'WRAP', '_NoValue', '__NUMPY_SETUP__', '__all__', '__builtins__', '__cached__', '__config__', '__doc__', '__file__', '__git_revision__', '__loader__', '__name__', '__package__', '__path__', '__spec__', '__version__', '_distributor_init', '_globals', '_import_tools', '_mat', 'abs', 'absolute', 'absolute_import', 'add', 'add_docstring', 'add_newdoc', 'add_newdoc_ufunc', 'add_newdocs', 'alen', 'all', 'allclose', 'alltrue', 'amax', 'amin', 'angle', 'any', 'append', 'apply_along_axis', 'apply_over_axes', 'arange', 'arccos', 'arccosh', 'arcsin', 'arcsinh', 'arctan', 'arctan2', 'arctanh', 'argmax', 'argmin', 'argpartition', 'argsort', 'argwhere', 'around', 'array', 'array2string', 'array_equal', 'array_equiv', 'array_repr', 'array_split', 'array_str', 'asanyarray', 'asarray', 'asarray_chkfinite', 'ascontiguousarray', 'asfarray', 'asfortranarray', 'asmatrix', 'asscalar', 'atleast_1d', 'atleast_2d', 'atleast_3d', 'average', 'bartlett', 'base_repr', 'bench', 'binary_repr', 'bincount', 'bitwise_and', 'bitwise_not', 'bitwise_or', 'bitwise_xor', 'blackman', 'block', 'bmat', 'bool', 'bool8', 'bool_', 'broadcast', 'broadcast_arrays', 'broadcast_to', 'busday_count', 'busday_offset', 'busdaycalendar', 'byte', 'byte_bounds', 'bytes0', 'bytes_', 'c_', 'can_cast', 'cast', 'cbrt', 'cdouble', 'ceil', 'cfloat', 'char', 'character', 'chararray', 'choose', 'clip', 'clongdouble', 'clongfloat', 'column_stack', 'common_type', 'compare_chararrays', 'compat', 'complex', 'complex128', 'complex64', 'complex_', 'complexfloating', 'compress', 'concatenate', 'conj', 'conjugate', 'convolve', 'copy', 'copysign', 'copyto', 'core', 'corrcoef', 'correlate', 'cos', 'cosh', 'count_nonzero', 'cov', 'cross', 'csingle', 'ctypeslib', 'cumprod', 'cumproduct', 'cumsum', 'datetime64', 'datetime_as_string', 'datetime_data', 'deg2rad', 'degrees', 'delete', 'deprecate', 'deprecate_with_doc', 'diag', 'diag_indices', 'diag_indices_from', 'diagflat', 'diagonal', 'diff', 'digitize', 'disp', 'divide', 'division', 'divmod', 'dot', 'double', 'dsplit', 'dstack', 'dtype', 'e', 'ediff1d', 'einsum', 'einsum_path', 'emath', 'empty', 'empty_like', 'equal', 'errstate', 'euler_gamma', 'exp', 'exp2', 'expand_dims', 'expm1', 'extract', 'eye', 'fabs', 'fastCopyAndTranspose', 'fft', 'fill_diagonal', 'find_common_type', 'finfo', 'fix', 'flatiter', 'flatnonzero', 'flexible', 'flip', 'fliplr', 'flipud', 'float', 'float16', 'float32', 'float64', 'float_', 'float_power', 'floating', 'floor', 'floor_divide', 'fmax', 'fmin', 'fmod', 'format_parser', 'frexp', 'frombuffer', 'fromfile', 'fromfunction', 'fromiter', 'frompyfunc', 'fromregex', 'fromstring', 'full', 'full_like', 'fv', 'generic', 'genfromtxt', 'geomspace', 'get_array_wrap', 'get_include', 'get_printoptions', 'getbufsize', 'geterr', 'geterrcall', 'geterrobj', 'gradient', 'greater', 'greater_equal', 'half', 'hamming', 'hanning', 'heaviside', 'histogram', 'histogram2d', 'histogramdd', 'hsplit', 'hstack', 'hypot', 'i0', 'identity', 'iinfo', 'imag', 'in1d', 'index_exp', 'indices', 'inexact', 'inf', 'info', 'infty', 'inner', 'insert', 'int', 'int0', 'int16', 'int32', 'int64', 'int8', 'int_', 'int_asbuffer', 'intc', 'integer', 'interp', 'intersect1d', 'intp', 'invert', 'ipmt', 'irr', 'is_busday', 'isclose', 'iscomplex', 'iscomplexobj', 'isfinite', 'isfortran', 'isin', 'isinf', 'isnan', 'isnat', 'isneginf', 'isposinf', 'isreal', 'isrealobj', 'isscalar', 'issctype', 'issubclass_', 'issubdtype', 'issubsctype', 'iterable', 'ix_', 'kaiser', 'kron', 'ldexp', 'left_shift', 'less', 'less_equal', 'lexsort', 'lib', 'linalg', 'linspace', 'little_endian', 'load', 'loads', 'loadtxt', 'log', 'log10', 'log1p', 'log2', 'logaddexp', 'logaddexp2', 'logical_and', 'logical_not', 'logical_or', 'logical_xor', 'logspace', 'long', 'longcomplex', 'longdouble', 'longfloat', 'longlong', 'lookfor', 'ma', 'mafromtxt', 'mask_indices', 'mat', 'math', 'matmul', 'matrix', 'matrixlib', 'max', 'maximum', 'maximum_sctype', 'may_share_memory', 'mean', 'median', 'memmap', 'meshgrid', 'mgrid', 'min', 'min_scalar_type', 'minimum', 'mintypecode', 'mirr', 'mod', 'modf', 'moveaxis', 'msort', 'multiply', 'nan', 'nan_to_num', 'nanargmax', 'nanargmin', 'nancumprod', 'nancumsum', 'nanmax', 'nanmean', 'nanmedian', 'nanmin', 'nanpercentile', 'nanprod', 'nanstd', 'nansum', 'nanvar', 'nbytes', 'ndarray', 'ndenumerate', 'ndfromtxt', 'ndim', 'ndindex', 'nditer', 'negative', 'nested_iters', 'newaxis', 'nextafter', 'nonzero', 'not_equal', 'nper', 'npv', 'numarray', 'number', 'obj2sctype', 'object', 'object0', 'object_', 'ogrid', 'oldnumeric', 'ones', 'ones_like', 'outer', 'packbits', 'pad', 'partition', 'percentile', 'pi', 'piecewise', 'pkgload', 'place', 'pmt', 'poly', 'poly1d', 'polyadd', 'polyder', 'polydiv', 'polyfit', 'polyint', 'polymul', 'polynomial', 'polysub', 'polyval', 'positive', 'power', 'ppmt', 'print_function', 'prod', 'product', 'promote_types', 'ptp', 'put', 'putmask', 'pv', 'r_', 'rad2deg', 'radians', 'random', 'rank', 'rate', 'ravel', 'ravel_multi_index', 'real', 'real_if_close', 'rec', 'recarray', 'recfromcsv', 'recfromtxt', 'reciprocal', 'record', 'remainder', 'repeat', 'require', 'reshape', 'resize', 'result_type', 'right_shift', 'rint', 'roll', 'rollaxis', 'roots', 'rot90', 'round', 'round_', 'row_stack', 's_', 'safe_eval', 'save', 'savetxt', 'savez', 'savez_compressed', 'sctype2char', 'sctypeDict', 'sctypeNA', 'sctypes', 'searchsorted', 'select', 'set_numeric_ops', 'set_printoptions', 'set_string_function', 'setbufsize', 'setdiff1d', 'seterr', 'seterrcall', 'seterrobj', 'setxor1d', 'shape', 'shares_memory', 'short', 'show_config', 'sign', 'signbit', 'signedinteger', 'sin', 'sinc', 'single', 'singlecomplex', 'sinh', 'size', 'sometrue', 'sort', 'sort_complex', 'source', 'spacing', 'split', 'sqrt', 'square', 'squeeze', 'stack', 'std', 'str', 'str0', 'str_', 'string_', 'subtract', 'sum', 'swapaxes', 'sys', 'take', 'tan', 'tanh', 'tensordot', 'test', 'testing', 'tile', 'timedelta64', 'trace', 'tracemalloc_domain', 'transpose', 'trapz', 'tri', 'tril', 'tril_indices', 'tril_indices_from', 'trim_zeros', 'triu', 'triu_indices', 'triu_indices_from', 'true_divide', 'trunc', 'typeDict', 'typeNA', 'typecodes', 'typename', 'ubyte', 'ufunc', 'uint', 'uint0', 'uint16', 'uint32', 'uint64', 'uint8', 'uintc', 'uintp', 'ulonglong', 'unicode', 'unicode_', 'union1d', 'unique', 'unpackbits', 'unravel_index', 'unsignedinteger', 'unwrap', 'ushort', 'vander', 'var', 'vdot', 'vectorize', 'version', 'void', 'void0', 'vsplit', 'vstack', 'warnings', 'where', 'who', 'zeros', 'zeros_like']
>>> dir(random)
['BPF', 'LOG4', 'NV_MAGICCONST', 'RECIP_BPF', 'Random', 'SG_MAGICCONST', 'SystemRandom', 'TWOPI', '_BuiltinMethodType', '_MethodType', '_Sequence', '_Set', '__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_acos', '_bisect', '_ceil', '_cos', '_e', '_exp', '_inst', '_itertools', '_log', '_pi', '_random', '_sha512', '_sin', '_sqrt', '_test', '_test_generator', '_urandom', '_warn', 'betavariate', 'choice', 'choices', 'expovariate', 'gammavariate', 'gauss', 'getrandbits', 'getstate', 'lognormvariate', 'normalvariate', 'paretovariate', 'randint', 'random', 'randrange', 'sample', 'seed', 'setstate', 'shuffle', 'triangular', 'uniform', 'vonmisesvariate', 'weibullvariate']
>>> a = [1,2,3,4,5,6,]
>>> a = [[1,2,3], [4,5,6], [7,8,9]]
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> print(a)
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> for matrix in a:
	print(matrix)

	
[1, 2, 3]
[4, 5, 6]
[7, 8, 9]
>>> a[0][2]
3
>>> a[1][1]
5
>>> np_arr = numpy.array([1,2,3,4,5,6])
>>> np_arr
array([1, 2, 3, 4, 5, 6])
>>> print(np_arr)
[1 2 3 4 5 6]
>>> s = "Hello"
>>> s
'Hello'
>>> print(s)
Hello
>>> s = "Hello\n"
>>> s
'Hello\n'
>>> s = "Hello\nWorld"
>>> s
'Hello\nWorld'
>>> print(s)
Hello
World
>>> np_arr
array([1, 2, 3, 4, 5, 6])
>>> print(np_arr)
[1 2 3 4 5 6]
>>> np_arr = numpy.array([[1,2,3],[4,5,6], [7,8,9])
		     
SyntaxError: invalid syntax
>>> np_arr = numpy.array([[1,2,3],[4,5,6], [7,8,9]])
>>> np_arr
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> print(np_arr)
[[1 2 3]
 [4 5 6]
 [7 8 9]]
>>> np_arr[0]
array([1, 2, 3])
>>> np_arr[0][1]
2
>>> np_arr[0:2]
array([[1, 2, 3],
       [4, 5, 6]])
>>> np_arr[0:3]
array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]])
>>> np_arr[0:2][0:2]
array([[1, 2, 3],
       [4, 5, 6]])
>>> np_arr[0:2][0]
array([1, 2, 3])
>>> a
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
>>> import sys
>>> sys.getsizeof(a)
88
>>> sys.getsizeof(np_arr)
148
>>> a = [i for i in range(0,100)]
>>> a
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
>>> np_arr = numpy.array([i for i in range(0,100)])
>>> np_arr
array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16,
       17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33,
       34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
       51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,
       68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84,
       85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99])
>>> sys.getsizeof(a)
912
>>> sys.getsizeof(np_arr)
496
>>> a = [i for i in range(1000000)]
>>> np_arr = numpy.array([i for i in range(1000000)])
>>> sys.getsizeof(a)
8697464
>>> sys.getsizeof(np_arr)
4000096
>>> import pandas
>>> data = {'id' : [1,2,3,4,5,6,7,8], 'name' : ['Ram', 'Shyam', 'Amit', 'Ajay', 'Ravi', 'Anuj', 'Akash', 'Sumit', 'Pooja']}
>>> pandas.Series(data)
id                               [1, 2, 3, 4, 5, 6, 7, 8]
name    [Ram, Shyam, Amit, Ajay, Ravi, Anuj, Akash, Su...
dtype: object
>>> print(pandas.Series(data))
id                               [1, 2, 3, 4, 5, 6, 7, 8]
name    [Ram, Shyam, Amit, Ajay, Ravi, Anuj, Akash, Su...
dtype: object
>>> pandas.DataFrame(data)
Traceback (most recent call last):
  File "<pyshell#146>", line 1, in <module>
    pandas.DataFrame(data)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 275, in __init__
    mgr = self._init_dict(data, index, columns, dtype=dtype)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 411, in _init_dict
    return _arrays_to_mgr(arrays, data_names, index, columns, dtype=dtype)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 5496, in _arrays_to_mgr
    index = extract_index(arrays)
  File "C:\Python36\lib\site-packages\pandas\core\frame.py", line 5544, in extract_index
    raise ValueError('arrays must all be same length')
ValueError: arrays must all be same length
>>> data = {'id' : [1,2,3,4,5,6,7,8], 'name' : ['Ram', 'Shyam', 'Amit', 'Ajay', 'Ravi', 'Anuj', 'Akash', 'Sumit']}
>>> pandas.DataFrame(data)
   id   name
0   1    Ram
1   2  Shyam
2   3   Amit
3   4   Ajay
4   5   Ravi
5   6   Anuj
6   7  Akash
7   8  Sumit
>>> data = {'id' : [1,2,3,4,5,6,7,8], 'name' : ['Ram', 'Shyam', 'Amit', 'Ajay', 'Ravi', 'Anuj', 'Akash', 'Sumit'], 'age' : [16,17,18,23,25,21,27,28]}
>>> pandas.DataFrame(data)
   age  id   name
0   16   1    Ram
1   17   2  Shyam
2   18   3   Amit
3   23   4   Ajay
4   25   5   Ravi
5   21   6   Anuj
6   27   7  Akash
7   28   8  Sumit
>>> 
