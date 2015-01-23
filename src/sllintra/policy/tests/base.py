from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import unittest


class SllintraPolicyLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        """Set up Zope."""

        # Required by Products.CMFPlone:plone-content to setup defaul plone site.
        z2.installProduct(app, 'Products.PythonScripts')

        import Products.PloneFormGen
        self.loadZCML(package=Products.PloneFormGen)
        z2.installProduct(app, 'Products.PloneFormGen')

        # Load ZCML
        import plonetheme.sunburst
        self.loadZCML(package=plonetheme.sunburst)
        import sllintra.policy
        self.loadZCML(package=sllintra.policy)

    def setUpPloneSite(self, portal):
        """Set up Plone."""
        # Install into Plone site using portal_setup

        # Installs all the Plone stuff. Workflows etc. to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone')

        # Install portal content. Including the Members folder! to setup defaul plone site.
        self.applyProfile(portal, 'Products.CMFPlone:plone-content')

        self.applyProfile(portal, 'plonetheme.sunburst:default')
        self.applyProfile(portal, 'sllintra.policy:default')

    def tearDownZope(self, app):
        """Tear down Zope."""
        z2.uninstallProduct(app, 'Products.PloneFormGen')
        z2.uninstallProduct(app, 'Products.PythonScripts')


FIXTURE = SllintraPolicyLayer()
INTEGRATION_TESTING = IntegrationTesting(
    bases=(FIXTURE,), name="SllintraPolicyLayer:Integration")
FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(FIXTURE,), name="SllintraPolicyLayer:Functional")


class IntegrationTestCase(unittest.TestCase):
    """Base class for integration tests."""

    layer = INTEGRATION_TESTING


class FunctionalTestCase(unittest.TestCase):
    """Base class for functional tests."""

    layer = FUNCTIONAL_TESTING
