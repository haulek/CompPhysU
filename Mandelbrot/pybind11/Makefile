imanc.so: imanc.cc
	g++-12 `python3 -m pybind11 --includes` -undefined dynamic_lookup -O3 -fopenmp -shared -std=c++11 -fPIC imanc.cc -o imanc.so
clean:
	rm imanc.so
