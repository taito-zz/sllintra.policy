from Products.CMFCore.utils import getToolByName


def uninstall_package(context, packages):
    """Uninstall packages.

    :param packages: List of package names.
    :type packages: list
    """
    portal = context.getSite()
    installer = getToolByName(portal, 'portal_quickinstaller')
    packages = [
        package for package in packages if installer.isProductInstalled(package)
    ]
    installer.uninstallProducts(packages)


def setupVarious(context):

    if context.readDataFile('sllintra.policy_various.txt') is None:
        return

    uninstall_package(context, ['plonetheme.classic'])
