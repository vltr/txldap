txldapv2
========

txldapv2 is a Twisted wrapper for [python-ldap][docs].

Note: I'm not the original author of [txldap](https://github.com/sboneyard/txldap). I just upgraded it a bit so it can be usable again, therefore I'm calling it ```txldapv2```. I don't think it'll be published to PyPi, at least for now.

### Requirements

* [python-ldap](http://www.python-ldap.org/)
* [Twisted](http://twistedmatrix.com/)

### Install

Checkout + ```pip install``` on the directory.

### Example

```python
# -*- coding: utf-8 -*-

import txldapv2
from twisted.internet import defer


@defer.inlineCallbacks
def main():
    data = dict(
        host='your_ldap_host',
        port=389,
        account='user@domain.local',
        password='Pwd1337!!1!one!11',
        base_dn='DC=domain,DC=local',
        user_filter='(objectClass=user)',
        timeout=300,
        attr_username='sAMAccountName',
        attr_firstname='givenName',
        attr_surname='sn',
        attr_mail='mail'
    )

    ret_attrs = map(lambda (k, v): v, filter(lambda (x, y): x.startswith('attr_'), data.iteritems()))

    l = txldapv2.Connection(data.get('host'), port=data.get('port', 389), timeout=data.get('timeout', 0))
    yield l.bind(who=data.get('account'), cred=data.get('password'))

    sf = '(&%s(%s=%s))' % (data.get('user_filter'), data.get('attr_username'), 'another-user')
    results = yield l.search(data.get('base_dn'), txldapv2.SCOPE_SUBTREE, sf, ret_attrs)
    if results:
        print results
    from twisted.internet import reactor
    reactor.stop()


if __name__ == '__main__':
    main()

    from twisted.internet import reactor
    reactor.run()

```

### Licenses

This work is licensed under the MIT License (see the LICENSE file).

[docs]: http://www.python-ldap.org/doc/html/ldap.html "python-ldap documentation"
