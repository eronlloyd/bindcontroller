$TTL	86400
$ORIGIN bindcontroller.com.
@  1D  IN  SOA ns1.bindcontroller.com. hostmaster.bindcontroller.com. (
			      2017102901 ; serial
			      3H ; refresh
			      15 ; retry
			      1w ; expire
			      3h ; nxdomain ttl
			     )
       IN  NS     ns1.bindcontroller.com.
       IN  NS     ns2.bindcontroller.com.
       IN  MX  10 mail.bindcontroller.com.
ns1    IN  A      192.168.0.1
www    IN  A      192.168.0.2
ftp    IN  CNAME  www.example.com.
desktop1   IN  A      192.168.0.3
desktop2   IN  A      192.168.0.4