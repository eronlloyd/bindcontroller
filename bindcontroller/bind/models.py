from django.db import models
from dns import zone
import dns.resolver
import dns.query
import dns.zone
from dns.exception import DNSException
from dns.rdataclass import *
from dns.rdatatype import *


class Zone(models.Model):
    data = models.TextField()
