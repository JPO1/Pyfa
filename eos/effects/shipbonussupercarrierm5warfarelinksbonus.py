# shipBonusSupercarrierM5WarfareLinksBonus
#
# Used by:
# Ship: Hel
type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Skirmish Command Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusSupercarrierM5"), skill="Minmatar Carrier")
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Command Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusSupercarrierM5"), skill="Minmatar Carrier")
