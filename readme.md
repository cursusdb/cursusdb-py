## CursusDB Python Native Client Package
Will soon be available on PyPI.

Importing package
``` 
from cursusdb import Client
```

Using 
``` 
# host/fqdn, port, db username, db password, TLS ?
c = Client("0.0.0.0", 7681, "username", "password", False)
print(c.connect())

print(c.query("ping;"))
c.close()
```
