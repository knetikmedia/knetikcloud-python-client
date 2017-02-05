# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://demo.sandbox.knetikcloud.com

    OpenAPI spec version: latest 
    Contact: support@knetik.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.reporting_usage_api import ReportingUsageApi


class TestReportingUsageApi(unittest.TestCase):
    """ ReportingUsageApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.reporting_usage_api.ReportingUsageApi()

    def tearDown(self):
        pass

    def test_get_usage_by_day_using_get(self):
        """
        Test case for get_usage_by_day_using_get

        Returns aggregated endpoint usage information by the day
        """
        pass

    def test_get_usage_by_hour_using_get(self):
        """
        Test case for get_usage_by_hour_using_get

        Returns aggregated endpoint usage information by hour
        """
        pass

    def test_get_usage_by_minute_using_get(self):
        """
        Test case for get_usage_by_minute_using_get

        Returns aggregated endpoint usage information by minute
        """
        pass

    def test_get_usage_by_month_using_get(self):
        """
        Test case for get_usage_by_month_using_get

        Returns aggregated endpoint usage information by month
        """
        pass

    def test_get_usage_by_year_using_get(self):
        """
        Test case for get_usage_by_year_using_get

        Returns aggregated endpoint usage information by year
        """
        pass


if __name__ == '__main__':
    unittest.main()
