# eliteBonusCommandShipArmoredCS3
#
# Used by:
# Ships from group: Command Ship (4 of 8)
type = "passive"
def handler(fit, ship, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Armored Command Specialist"),
                                  "commandBonus", ship.getModifiedItemAttr("eliteBonusCommandShips3"), skill="Command Ships")
