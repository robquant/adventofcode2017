cythonize -3 day5.pyx
$CC -O3 -shared -fPIC $(pkg-config --cflags --libs python3) -o day5.so day5.c
python3 -m timeit -n 1 -c 'import day5; day5.main()'
