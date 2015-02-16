# -*- coding: utf-8 -*-
from Products.CMFCore.utils import getToolByName
from sllintra.policy.tests.base import IntegrationTestCase


class TestCase(IntegrationTestCase):
    """TestCase for Plone setup."""

    def setUp(self):
        self.portal = self.layer['portal']

    def test_package__installed(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.failUnless(installer.isProductInstalled('sllintra.policy'))

        from sllintra.policy.browser.interfaces import ISllintraPolicyLayer
        from plone.browserlayer import utils
        self.assertIn(ISllintraPolicyLayer, utils.registered_layers())

    def test_metadata__dependency__Products_PloneFormGen(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('PloneFormGen'))

    def test_metadata__dependency__eea_facetednavigation(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('eea.facetednavigation'))

    def test_metadata__dependency__sllintra_content(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('sllintra.content'))

    def test_metadata__dependency__sllintra_theme(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertTrue(installer.isProductInstalled('sllintra.theme'))

    def test_metadata__version(self):
        setup = getToolByName(self.portal, 'portal_setup')
        self.assertEqual(setup.getVersionForProfile('profile-sllintra.policy:default'), u'0')

    def test_setuphandlers__uninstall_package__plonetheme_classic(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        self.assertFalse(installer.isProductInstalled('plonetheme.classic'))

    def test_uninstall(self):
        installer = getToolByName(self.portal, 'portal_quickinstaller')
        installer.uninstallProducts(['sllintra.policy'])
        self.assertFalse(installer.isProductInstalled('sllintra.policy'))
