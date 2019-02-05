#include <pybind11/pybind11.h>

PYBIND11_MODULE(montecarlopi, m) {
    m.doc() = "Monte Carlo calculation of pi in C++ with a pybind11 binding to Python";
    m.def("pi", &MonteCarloPi, "Estimates \\pi using the Monte Carlo method using specified number of samples.");
}
