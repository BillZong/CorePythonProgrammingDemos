#!/usr/bin/env python

"""Number tests."""

a = 0
print id(a)
del a

print repr(123432342342343234234)
print str(123432342342343234234)

print repr(2 << 32)
print repr(2 << 64)
print repr(2 << 128)

aComplex = -38.2 - 1.234j
print aComplex
print aComplex.conjugate()
print aComplex.real
print aComplex.imag


print 5.52 / 2
print 5.52 // 2
print 1 / 2

print 5.2 % 2
print (5.2 + 2j) % 2
