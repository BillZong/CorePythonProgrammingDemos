#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.1 for chapter 13."""


class HotelRoomCalc(object):
    """Hotel room rate calculator."""

    def __init__(self, rt, sales=0.085, rm=0.1):
        """Class HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%."""
        self.roomRate = rt
        self.salesTax = sales
        self.roomTax = rm

    def calc_total(self, days=1):
        """Calculate total: default to daily rate."""
        daily = round((self.roomRate *
                      (1 + self.roomTax + self.salesTax)), 2)
        return float(days) * daily

print HotelRoomCalc.__init__.__doc__

sfo = HotelRoomCalc(299)
print sfo.calc_total()
print sfo.calc_total(2)

sea = HotelRoomCalc(189, 0.086, 0.058)
print sea.calc_total()
print sea.calc_total(4)

wasWkDay = HotelRoomCalc(169, 0.045, 0.02)
wasWkEnd = HotelRoomCalc(119, 0.045, 0.02)
print wasWkDay.calc_total(5) + wasWkEnd.calc_total()
