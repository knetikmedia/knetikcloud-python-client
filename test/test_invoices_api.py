# coding: utf-8

"""
    Knetik Platform API Documentation latest 

    This is the spec for the Knetik API.  Use this in conjunction with the documentation found at https://knetikcloud.com

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
from swagger_client.apis.invoices_api import InvoicesApi


class TestInvoicesApi(unittest.TestCase):
    """ InvoicesApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.invoices_api.InvoicesApi()

    def tearDown(self):
        pass

    def test_create_invoice(self):
        """
        Test case for create_invoice

        Create an invoice
        """
        pass

    def test_get_ful_fillment_statuses(self):
        """
        Test case for get_ful_fillment_statuses

        Lists available fulfillment statuses
        """
        pass

    def test_get_invoice(self):
        """
        Test case for get_invoice

        Retrieve an invoice
        """
        pass

    def test_get_invoice_logs(self):
        """
        Test case for get_invoice_logs

        List invoice logs
        """
        pass

    def test_get_invoices(self):
        """
        Test case for get_invoices

        Retrieve invoices
        """
        pass

    def test_get_payment_statuses(self):
        """
        Test case for get_payment_statuses

        Lists available payment statuses
        """
        pass

    def test_pay_invoice(self):
        """
        Test case for pay_invoice

        Trigger payment of an invoice
        """
        pass

    def test_set_external_ref(self):
        """
        Test case for set_external_ref

        Set the external reference of an invoice
        """
        pass

    def test_set_invoice_item_fulfillment_status(self):
        """
        Test case for set_invoice_item_fulfillment_status

        Set the fulfillment status of an invoice item
        """
        pass

    def test_set_order_notes(self):
        """
        Test case for set_order_notes

        Set the order notes of an invoice
        """
        pass

    def test_set_payment_status(self):
        """
        Test case for set_payment_status

        Set the payment status of an invoice
        """
        pass

    def test_update_billing_info(self):
        """
        Test case for update_billing_info

        Set or update billing info
        """
        pass


if __name__ == '__main__':
    unittest.main()
