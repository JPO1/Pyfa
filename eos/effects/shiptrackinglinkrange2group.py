# shipTrackingLinkRange2Group
#
# Used by:
# Ship: Oneiros
type = "passive"


def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Remote Tracking Computer",
                                  "maxRange", ship.getModifiedItemAttr("shipBonusGC2"), skill="Gallente Cruiser")
