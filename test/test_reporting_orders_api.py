# coding: utf-8

"""
    Knetik Platform API Documentation Latest

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: Latest
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.reporting_orders_api import ReportingOrdersApi


class TestReportingOrdersApi(unittest.TestCase):
    """ ReportingOrdersApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.reporting_orders_api.ReportingOrdersApi()

    def tearDown(self):
        pass

    def test_get_daily_invoices_using_get(self):
        """
        Test case for get_daily_invoices_using_get

        Retrieve invoice counts aggregated by time ranges
        """
        pass


if __name__ == '__main__':
    unittest.main()
