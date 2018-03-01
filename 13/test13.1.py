#!/usr/bin/env python
# encoding: UTF-8

"""Demo 13.1 for chapter 13."""


class AddrBookEntry(object):
    """Address book entry class."""

    def __init__(self, nm, ph):
        u"""构造器."""
        self.name = nm
        self.phone = ph
        print("Created instance of {0}".format(self.name))

    def update_phone(self, newph):
        u"""更新电话."""
        self.phone = newph
        print("Updated phone# for: {0}".format(self.name))


john = AddrBookEntry('John Doe', '403-234-2145')
jane = AddrBookEntry('Jane Doe', '403-234-2144')
john.update_phone('13811111112')


class EmplAddrBookEntry(AddrBookEntry):
    """Employee Address Book Entry class."""

    def __init__(self, nm, ph, eid, em):
        u"""构造器."""
        AddrBookEntry.__init__(self, nm, ph)
        self.empid = eid
        self.email = em

    def update_email(self, newem):
        u"""更新电子邮件."""
        self.email = newem
        print("Updated e-mail address for: {0}".format(self.name))

bill = EmplAddrBookEntry('Bill Zong', '13898765432', 26, 'billzong@163.com')
bill.update_email('billzong@126.com')
bill.update_phone('13512345678')
print("{0}'s employee identifier is {1}".format(bill.name, bill.empid))
