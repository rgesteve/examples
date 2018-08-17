#include <pybind11/pybind11.h>

#include <iostream>
#include <future>
#include <random>
#include <chrono>

using namespace std;

bool inUnitCircle(double x, double y)
{
    if ((x*x + y*y) < 1.0) {
        return true;
    }
    return false;
}

double MonteCarloPi(long int reps)
{
    long int count = 0;
    unsigned int seed = (unsigned int)chrono::system_clock::now().time_since_epoch().count();
    default_random_engine engine(seed);
    uniform_real_distribution<double> rand(0,1);

    for (long int i = 0; i < reps; i++) {
        if (inUnitCircle(rand(engine), rand(engine))) {
            count++;
        }
    }

    return (double(count) / double(reps)) * 4.0;
}

PYBIND11_MODULE(montecarlopi, m) {
    m.doc() = "Monte Carlo calculation of pi in C++ with a pybind11 binding to Python";
    m.def("pi", &MonteCarloPi, "Estimates \\pi using the Monte Carlo method using specified number of samples.");
}