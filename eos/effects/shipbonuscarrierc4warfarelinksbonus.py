# shipBonusCarrierC4WarfareLinksBonus
#
# Used by:
# Ship: Chimera
type = "passive"
def handler(fit, src, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Shield Command Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusCarrierC4"), skill="Caldari Carrier")
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Information Command Specialist"), "commandBonus", src.getModifiedItemAttr("shipBonusCarrierC4"), skill="Caldari Carrier")
