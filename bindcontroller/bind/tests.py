from django.test import TestCase
from dns import zone
import dns.resolver
import dns.query
import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *

from bind.models import Zone


class LibraryTests(TestCase):

    def test_load_zone_file(self):

        original_zone_text = open('bind/data/testzones/db.bindcontroller.com').read()
        print(original_zone_text)
        z = zone.from_file('bind/data/testzones/db.bindcontroller.com')
        loaded_zone_text = z.to_text()
        self.assertNotEquals(original_zone_text, loaded_zone_text)

    def transfer(self):

        domain = "dnspython.org"
        print("Getting NS records for", domain)
        answers = dns.resolver.query(domain, 'NS')
        ns = []
        for rdata in answers:
            n = str(rdata)
            print("Found name server:", n)
            ns.append(n)

        for n in ns:
            print("\nTrying a zone transfer for %s from name server %s" % (domain, n))
            try:
                z = dns.zone.from_xfr(dns.query.xfr(n, domain))
            except DNSException:
                print("Broke!")


class ModelTests(TestCase):

    def test_zone(self):

        z = Zone()
        f = open('bind/data/testzones/db.bindcontroller.com')
        z.data = f.read()
        f.seek(0)
        self.assertEquals(z.data, f.read())