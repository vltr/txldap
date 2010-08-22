import txldap
from twisted.internet import reactor

def failure(result, type):
    print '%s failure' % type
    reactor.stop()

def search_success(result, ldap):
    print result
    reactor.stop()

def bind_success(result, ldap):
    d = ldap.search(
        'ou=People,dc=example,dc=org',
        txldap.SCOPE_SUBTREE,
        'uid=silas',
    )
    d.addCallbacks(search_success, failure, [ldap], {}, ['Search'])

def main():
    ldap = txldap.Connection('ldap://localhost')
    d = ldap.bind('uid=silas,ou=People,dc=example,dc=org', 'silas')
    d.addCallbacks(bind_success, failure, [ldap], {}, ['Bind'])

if __name__ == '__main__':
    main()
    reactor.run()
