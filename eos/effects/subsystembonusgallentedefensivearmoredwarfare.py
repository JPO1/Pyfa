# subSystemBonusGallenteDefensiveArmoredWarfare
#
# Used by:
# Subsystem: Proteus Defensive - Warfare Processor
type = "passive"
def handler(fit, module, context):
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Armored Command Specialist"),
                                  "commandBonus", module.getModifiedItemAttr("subsystemBonusGallenteDefensive"), skill="Gallente Defensive Systems")
