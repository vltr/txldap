# Copyright (c) 2010, Silas Sewell
# All rights reserved.
#
# This file is subject to the MIT License (see LICENSE file).

from ldap import *
from twisted.internet import threads

class Connection(object):

    def __init__(self, uri, *args, **kwargs):
        self.debug = kwargs.pop('debug', False)
        self._ldap = initialize(uri, *args, **kwargs)
        if self.debug:
            self._ldap.set_option(ldap.OPT_DEBUG_LEVEL, 255)

    def add(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.add_ext_s, *args, **kwargs)

    def bind(self, who=None, cred=None, method=None):
        if who is None:
            return threads.deferToThread(self._ldap.simple_bind_s)
        elif who and cred is None:
            return threads.deferToThread(self._ldap.simple_bind_s, who)
        elif who and cred and method is None:
            return threads.deferToThread(self._ldap.simple_bind_s, who, cred)
        else:
            return threads.deferToThread(self._ldap.bind_s, who, cred, method)

    def compare(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.compare_ext_s, *args, **kwargs)

    def delete(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.delete_ext_s, *args, **kwargs)

    def modify(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.modify_ext_s, *args, **kwargs)

    def passwd(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.passwd_s, *args, **kwargs)

    def rename(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.rename_s, *args, **kwargs)

    def sasl_interactive_bind(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.sasl_interactive_bind_s, *args, **kwargs)

    def start_tls(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.start_tls_s, *args, **kwargs)

    def search(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.search_s, *args, **kwargs)

    def unbind(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.unbind_ext_s, *args, **kwargs)

    def whoami(self, *args, **kwargs):
        return threads.deferToThread(self._ldap.whoami_s, *args, **kwargs)
