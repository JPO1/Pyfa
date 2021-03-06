# siegeModeEffect6
#
# Used by:
# Variations of module: Siege Module I (2 of 2)
type = "active"
runTime = "early"


def handler(fit, module, context):
    # Turrets
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Turret") or \
                                              mod.item.requiresSkill("Capital Hybrid Turret") or \
                                              mod.item.requiresSkill("Capital Projectile Turret"),
                                  "damageMultiplier", module.getModifiedItemAttr("damageMultiplierBonus"))

    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Energy Turret") or \
                                              mod.item.requiresSkill("Capital Hybrid Turret") or \
                                              mod.item.requiresSkill("Capital Projectile Turret"),
                                  "trackingSpeed", module.getModifiedItemAttr("trackingSpeedBonus"))

    # Missiles
    for type in ("kinetic", "thermal", "explosive", "em"):
        fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("XL Torpedoes") or \
                                                    mod.charge.requiresSkill("XL Cruise Missiles"),
                                        "%sDamage" % type, module.getModifiedItemAttr("damageMultiplierBonus"))

    fit.modules.filteredChargeBoost(lambda mod: mod.charge.requiresSkill("XL Torpedoes") or \
                                                mod.charge.requiresSkill("XL Cruise Missiles"),
                                    "aoeVelocity", module.getModifiedItemAttr("aoeVelocityBonus"))

    # Shield Boosters
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Operation"),
                                  "duration", module.getModifiedItemAttr("shieldBonusDurationBonus"),
                                  stackingPenalties=True)
    fit.modules.filteredItemBoost(lambda mod: mod.item.requiresSkill("Capital Shield Operation"),
                                  "shieldBonus", module.getModifiedItemAttr("shieldBoostMultiplier"),
                                  stackingPenalties=True)

    # Armor Reppers
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "armorDamageAmount", module.getModifiedItemAttr("armorDamageAmountBonus"),
                                  stackingPenalties=True)
    fit.modules.filteredItemBoost(lambda mod: mod.item.group.name == "Armor Repair Unit",
                                  "duration", module.getModifiedItemAttr("armorDamageDurationBonus"),
                                  stackingPenalties=True)

    # Speed penalty
    fit.ship.boostItemAttr("maxVelocity", module.getModifiedItemAttr("speedFactor"))

    # Mass
    fit.ship.multiplyItemAttr("mass", module.getModifiedItemAttr("siegeMassMultiplier"))

    # Scan resolution
    fit.ship.multiplyItemAttr("scanResolution", module.getModifiedItemAttr("scanResolutionMultiplier"),
                              stackingPenalties=True)

    # Max locked targets
    fit.ship.forceItemAttr("maxLockedTargets", module.getModifiedItemAttr("maxLockedTargets"))

    # Block Hostile EWAR and friendly effects
    fit.ship.forceItemAttr("disallowOffensiveModifiers", module.getModifiedItemAttr("disallowOffensiveModifiers"))
    fit.ship.forceItemAttr("disallowAssistance", module.getModifiedItemAttr("disallowAssistance"))
