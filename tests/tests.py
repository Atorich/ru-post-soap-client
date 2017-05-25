# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import
from future import standard_library
standard_library.install_aliases()
from past.builtins import basestring
from builtins import *
import unittest

from ruspost_soap.client import RuPostClient, MakeTicketException
from . import test_data


class RuPostClientTest(unittest.TestCase):
    def test_fail_auth(self):
        if not test_data.TRACKS:
            raise AssertionError('Не заданы номера треков для теста')

        client = RuPostClient('login', 'pass')

        self.assertRaises(MakeTicketException, client.make_ticket, test_data.TRACKS)

    def test_ticket_creation(self):
        """
        Внесите в test_data номера треков для теста.
        """
        if not test_data.TRACKS:
            raise AssertionError('Не заданы номера треков для теста')

        client = RuPostClient()

        answer = client.make_ticket(test_data.TRACKS)

        ticket_number = list(answer.keys())[0]
        tracks = list(answer.values())[0]

        self.assertTrue(isinstance(ticket_number, basestring))
        self.assertTrue(set(test_data.TRACKS) >= set(tracks))

        print(u'Тикет: {0} используйте в списке TICKETS в `test_data`'.format(
            ticket_number))

    def test_track_request(self):
        """
        Внесите в test_data номер тикета полученный в тесте
        self.test_ticket_creation.
        """
        if not test_data.TICKETS:
            raise AssertionError('Не заданы номера тикетов для теста')

        client = RuPostClient()

        answer = client.get_tracks(test_data.TICKETS)

        self.assertTrue(isinstance(answer, dict))

        print(u'\n\nОТВЕТ по тикетам:\n{0}\n\n'.format(answer))


if __name__ == '__main__':
    unittest.main()
