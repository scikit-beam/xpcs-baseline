#ifndef XPCS_COMPLEX__H
#define XPCS_COMPLEX__H

#include <complex>
typedef std::complex<float> complex_t;
const complex_t COMPLX_J(0, 1);
const complex_t COMPLX_ZERO(0, 0);

#if HAVE_CUDA
#include <cuComplex.h>

#define CUDAFY __inline__ __host__ __device__
typedef cuFloatComplex cucomplex_t;

CUDAFY cucomplex_t operator+(const cucomplex_t &lhs , const cucomplex_t &rhs) {
	return make_cuFloatComplex(lhs.x + rhs.x, lhs.y + rhs.y);
}

CUDAFY cucomplex_t operator+(const cucomplex_t &lhs , float rhs) {
	return make_cuFloatComplex(lhs.x + rhs, lhs.y);
}

CUDAFY cucomplex_t operator*(const cucomplex_t &lhs , const cucomplex_t &rhs) {
	return cuCmulf(lhs, rhs);
}

CUDAFY cucomplex_t operator*(const cucomplex_t &lhs , float rhs) {
	return make_cuFloatComplex(rhs * lhs.x, rhs * lhs.y);
}

CUDAFY cucomplex_t Cexpf (const cucomplex_t  &arg) {
   cucomplex_t res;
   float s, c;
   float e = expf(arg.x);
   sincosf(arg.y, &s, &c);
   res.x = c * e;
   res.y = s * e;
   return res;
}
#endif // HAVE_CUDA

#endif // XPCS_COMPLEX__H
