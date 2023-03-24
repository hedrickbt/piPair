class MTGNames:
   def isTypeName (self,index,name):
      found = False
      if names[index].find(name) > -1:
         found = True
      return found
   
   def isArtifact (self,index):
      return self.isTypeName( index, 'artifacts' )
   
   def isCreature (self,index):
      return self.isTypeName( index, 'creatures' )
   
   def isEnchantment (self,index):
      return self.isTypeName( index, 'enchantments' )
   
   def isInstant (self,index):
      return self.isTypeName( index, 'instants' )
   
   def isLand (self,index):
      return self.isTypeName( index, 'lands' )
   
   def isSorcery (self,index):
      return self.isTypeName( index, 'sorcery' )
   
   def __init__(self):
      self.names = []
      self.names.append ( 'artifacts/The Machine.jpg')
      self.names.append ( 'artifacts/ak47.png')
      self.names.append ( 'artifacts/beeBeeBun.jpg')
      self.names.append ( 'artifacts/bfg.jpg')
      self.names.append ( 'artifacts/blackerLotus.jpg')
      self.names.append ( 'artifacts/blurryBeeble.jpg')
      self.names.append ( 'artifacts/captainAmericasShield.png')
      self.names.append ( 'artifacts/chaosConfetti.jpg')
      self.names.append ( 'artifacts/doItYourselfSeraph.png')
      self.names.append ( 'artifacts/doge.jpg')
      self.names.append ( 'artifacts/dragonBalls.jpg')
      self.names.append ( 'artifacts/eagleFiveWinnebago.jpg')
      self.names.append ( 'artifacts/fluxCapacitor.jpg')
      self.names.append ( 'artifacts/fodderCannon.jpg')
      self.names.append ( 'artifacts/galactus.jpg')
      self.names.append ( 'artifacts/gatlingGun.png')
      self.names.append ( 'artifacts/infinityGauntlet.png')
      self.names.append ( 'artifacts/letterBomb.jpg')
      self.names.append ( 'artifacts/limbReplacement.png')
      self.names.append ( 'artifacts/m1911.png')
      self.names.append ( 'artifacts/molotov.png')
      self.names.append ( 'artifacts/nullRod.jpg')
      self.names.append ( 'artifacts/peeweesBike.jpg')
      self.names.append ( 'artifacts/predatorTech.jpg')
      self.names.append ( 'artifacts/psychicPaper.jpg')
      self.names.append ( 'artifacts/ratchetBomb.jpg')
      self.names.append ( 'artifacts/sonicScrewdriver.jpg')
      self.names.append ( 'artifacts/staffofdomination.jpg')
      self.names.append ( 'artifacts/swordOfDungeonsAndDragons.jpg')
      self.names.append ( 'artifacts/tardis.jpg')
      self.names.append ( 'artifacts/tesseract.png')
      self.names.append ( 'artifacts/thatAss.jpg')
      self.names.append ( 'artifacts/tigerTank.png')
      self.names.append ( 'artifacts/tinman.png')
      self.names.append ( 'artifacts/urzasContactLenses.jpg')
      self.names.append ( 'creatures/agentSmith.jpg')
      self.names.append ( 'creatures/alGore.jpg')
      self.names.append ( 'creatures/americanEagle.jpg')
      self.names.append ( 'creatures/android17.png')
      self.names.append ( 'creatures/android18.png')
      self.names.append ( 'creatures/annoyingOrange.jpg')
      self.names.append ( 'creatures/arrgh.jpg')
      self.names.append ( 'creatures/arthurKingOfTheBritains.jpg')
      self.names.append ( 'creatures/barackHObama.jpg')
      self.names.append ( 'creatures/barackObama.jpg')
      self.names.append ( 'creatures/barackObamaII.jpg')
      self.names.append ( 'creatures/barfEagleFiveNavigator.jpg')
      self.names.append ( 'creatures/batman.jpg')
      self.names.append ( 'creatures/batmanII.jpg')
      self.names.append ( 'creatures/berneyStinson.jpg')
      self.names.append ( 'creatures/bernieSanders.jpg')
      self.names.append ( 'creatures/bernieSandersII.jpg')
      self.names.append ( 'creatures/bickeringGiant.jpg')
      self.names.append ( 'creatures/biffTannen.jpg')
      self.names.append ( 'creatures/blackKnight.jpg')
      self.names.append ( 'creatures/borgCube.jpg')
      self.names.append ( 'creatures/borgQueen.jpg')
      self.names.append ( 'creatures/bruceLee.jpg')
      self.names.append ( 'creatures/burninator.jpg')
      self.names.append ( 'creatures/cantinaBand.jpg')
      self.names.append ( 'creatures/captainAmerica.jfif')
      self.names.append ( 'creatures/charlesXavier.jpg')
      self.names.append ( 'creatures/cheatyFace.jpg')
      self.names.append ( 'creatures/chivalrousChevalier.jpg')
      self.names.append ( 'creatures/chuckNorris.jpg')
      self.names.append ( 'creatures/conanTheBarbarian.png')
      self.names.append ( 'creatures/conanTheLibrarian.png')
      self.names.append ( 'creatures/countTyroneRugen.jpg')
      self.names.append ( 'creatures/cowardlyLion.png')
      self.names.append ( 'creatures/daenerysStormborn.jpg')
      self.names.append ( 'creatures/darkHelmet.jpg')
      self.names.append ( 'creatures/darthSidious.jpg')
      self.names.append ( 'creatures/darthVader.jpg')
      self.names.append ( 'creatures/darylDixon.jpg')
      self.names.append ( 'creatures/deadPool.png')
      self.names.append ( 'creatures/deadPoolAgain.jpg')
      self.names.append ( 'creatures/deadPoolIII.png')
      self.names.append ( 'creatures/deadpoolFairyPrincess.jpg')
      self.names.append ( 'creatures/dickJones.png')
      self.names.append ( 'creatures/doctorEmmettBrown.jpg')
      self.names.append ( 'creatures/donkeyKong.png')
      self.names.append ( 'creatures/drHouse.jpg')
      self.names.append ( 'creatures/drStrange.jpg')
      self.names.append ( 'creatures/draxDestroyer.jpg')
      self.names.append ( 'creatures/earlOfSquirrel.jpg')
      self.names.append ( 'creatures/extremelySlowZombie.jpg')
      self.names.append ( 'creatures/fezzikTheKindlyGiant.jpg')
      self.names.append ( 'creatures/frieza.jpg')
      self.names.append ( 'creatures/gameStoreEmployee.jpg')
      self.names.append ( 'creatures/gamora.jpg')
      self.names.append ( 'creatures/gandalf.png')
      self.names.append ( 'creatures/generalGrievous.jpg')
      self.names.append ( 'creatures/georgeBushII.jpg')
      self.names.append ( 'creatures/georgeMcfly.jpg')
      self.names.append ( 'creatures/georgeWBush.jpg')
      self.names.append ( 'creatures/gilligan.png')
      self.names.append ( 'creatures/god.png')
      self.names.append ( 'creatures/godzilla.jpg')
      self.names.append ( 'creatures/gordonRamsey.jpg')
      self.names.append ( 'creatures/groot.jpg')
      self.names.append ( 'creatures/hanSolo.jpg')
      self.names.append ( 'creatures/hangman.jpg')
      self.names.append ( 'creatures/hela.png')
      self.names.append ( 'creatures/hillaryClinton.jpeg')
      self.names.append ( 'creatures/hirohito.png')
      self.names.append ( 'creatures/hitler.jpg')
      self.names.append ( 'creatures/hulk.png')
      self.names.append ( 'creatures/indianaJones.jpg')
      self.names.append ( 'creatures/infinityElemental.jpg')
      self.names.append ( 'creatures/inigoMontoya.jpg')
      self.names.append ( 'creatures/inigoMontoyaII.jpg')
      self.names.append ( 'creatures/ironMan.png')
      self.names.append ( 'creatures/ironManII.jpg')
      self.names.append ( 'creatures/itThatGetsLeftHanging.jpg')
      self.names.append ( 'creatures/jaceTheAsshole.jpg')
      self.names.append ( 'creatures/jamesKirk.png')
      self.names.append ( 'creatures/jangoFett.jpg')
      self.names.append ( 'creatures/jeanGrey.jpg')
      self.names.append ( 'creatures/johnLennon.jpg')
      self.names.append ( 'creatures/johnnyCash.jpg')
      self.names.append ( 'creatures/johnnyCombo.png')
      self.names.append ( 'creatures/josefStalin.png')
      self.names.append ( 'creatures/joshLane.jpg')
      self.names.append ( 'creatures/kanyeWest.png')
      self.names.append ( 'creatures/killerBunny.jpg')
      self.names.append ( 'creatures/kingKong.jpg')
      self.names.append ( 'creatures/kittyPryde.jpg')
      self.names.append ( 'creatures/koolAidMan.jpg')
      self.names.append ( 'creatures/krillin.jpg')
      self.names.append ( 'creatures/libyanTerrorists.jpg')
      self.names.append ( 'creatures/logan.jpg')
      self.names.append ( 'creatures/lordVoldemort.jpg')
      self.names.append ( 'creatures/magneto.jpg')
      self.names.append ( 'creatures/mario.jpg')
      self.names.append ( 'creatures/martyMcFly.jpg')
      self.names.append ( 'creatures/masterChief.png')
      self.names.append ( 'creatures/memePirate.jpeg')
      self.names.append ( 'creatures/miracleMax.jpg')
      self.names.append ( 'creatures/mrT.jpg')
      self.names.append ( 'creatures/mrTII.jpg')
      self.names.append ( 'creatures/mtgPlayer.png')
      self.names.append ( 'creatures/mysterioIllusionist.png')
      self.names.append ( 'creatures/mystique.jpg')
      self.names.append ( 'creatures/mythBusters.jpg')
      self.names.append ( 'creatures/nerdyPlayer.jpeg')
      self.names.append ( 'creatures/noviceBountyHunter.jpg')
      self.names.append ( 'creatures/obiWanKenobi.jpg')
      self.names.append ( 'creatures/oldGuard.jpg')
      self.names.append ( 'creatures/patton.png')
      self.names.append ( 'creatures/peeweeHerman.jpg')
      self.names.append ( 'creatures/pepe.jpg')
      self.names.append ( 'creatures/pikachu.png')
      self.names.append ( 'creatures/pizzaTheHutt.jpg')
      self.names.append ( 'creatures/predator.png')
      self.names.append ( 'creatures/princeHumperdinck.jpg')
      self.names.append ( 'creatures/princessButtercup.jpg')
      self.names.append ( 'creatures/princessLeia.jpg')
      self.names.append ( 'creatures/ragePlayer.jpeg')
      self.names.append ( 'creatures/raichu.jpg')
      self.names.append ( 'creatures/ralphNader.jpg')
      self.names.append ( 'creatures/redForman.jpg')
      self.names.append ( 'creatures/rickGrimes.png')
      self.names.append ( 'creatures/riddick.jfif')
      self.names.append ( 'creatures/robocop.jpg')
      self.names.append ( 'creatures/rocketRaccoon.jpg')
      self.names.append ( 'creatures/rocketTropper.jpg')
      self.names.append ( 'creatures/rodentOfUnusualSize.jpg')
      self.names.append ( 'creatures/samuelJackson.jpg')
      self.names.append ( 'creatures/santaClaus.jpg')
      self.names.append ( 'creatures/scorpionKing.png')
      self.names.append ( 'creatures/secretGamer.jpeg')
      self.names.append ( 'creatures/seleneBloodDrainer.png')
      self.names.append ( 'creatures/shermanTank.png')
      self.names.append ( 'creatures/silverSurfer.png')
      self.names.append ( 'creatures/sirBedevere.jpg')
      self.names.append ( 'creatures/sirRobin.png')
      self.names.append ( 'creatures/spaceMarineCaptain.png')
      self.names.append ( 'creatures/spiderman.jpg')
      self.names.append ( 'creatures/spidermanII.png')
      self.names.append ( 'creatures/spock.png')
      self.names.append ( 'creatures/starLord.jpg')
      self.names.append ( 'creatures/steveAustin.png')
      self.names.append ( 'creatures/stevenRogers.jpg')
      self.names.append ( 'creatures/superBattleDroid.jpg')
      self.names.append ( 'creatures/superman.jpg')
      self.names.append ( 'creatures/supermanII.jpg')
      self.names.append ( 'creatures/supermanIII.png')
      self.names.append ( 'creatures/t34Tank.jpg')
      self.names.append ( 'creatures/thanos.jpg')
      self.names.append ( 'creatures/theCollector.jpeg')
      self.names.append ( 'creatures/theJoker.jpg')
      self.names.append ( 'creatures/theOracle.jpg')
      self.names.append ( 'creatures/theSilence.jpg')
      self.names.append ( 'creatures/thor.jpg')
      self.names.append ( 'creatures/thorGodOfThunder.png')
      self.names.append ( 'creatures/thorSonOfOdin.png')
      self.names.append ( 'creatures/timmyPowerGamer.jpg')
      self.names.append ( 'creatures/toughNerd.jpeg')
      self.names.append ( 'creatures/tournamentGrinder.jpg')
      self.names.append ( 'creatures/tribble.png')
      self.names.append ( 'creatures/trooperCommander.jpg')
      self.names.append ( 'creatures/trump.jpg')
      self.names.append ( 'creatures/unwillingVolunteer.jpg')
      self.names.append ( 'creatures/vegeta.png')
      self.names.append ( 'creatures/vespaDruishPrincess.jpg')
      self.names.append ( 'creatures/vizziniSicilianMastermind.jpg')
      self.names.append ( 'creatures/vladimirPutin.jpg')
      self.names.append ( 'creatures/wallOfTrump.png')
      self.names.append ( 'creatures/warriorBug.png')
      self.names.append ( 'creatures/weepingStatue.jpg')
      self.names.append ( 'creatures/westleyMasterofEverything.jpg')
      self.names.append ( 'creatures/youngChild.jpeg')
      self.names.append ( 'enchantments/achHansRun.jpg')
      self.names.append ( 'enchantments/animateLibrary.jpg')
      self.names.append ( 'enchantments/blitzkrieg.jpg')
      self.names.append ( 'enchantments/charmSchool.jpg')
      self.names.append ( 'enchantments/curseOfTheFirePenguin.jpg')
      self.names.append ( 'enchantments/executiveOversight.png')
      self.names.append ( 'enchantments/forceMastery.jpg')
      self.names.append ( 'enchantments/hiddenProtocol.png')
      self.names.append ( 'enchantments/imposingVisage.jpg')
      self.names.append ( 'enchantments/jediMindTrick.png')
      self.names.append ( 'enchantments/lethalResponse.png')
      self.names.append ( 'enchantments/looseLips.jpg')
      self.names.append ( 'enchantments/nameDropping.jpg')
      self.names.append ( 'enchantments/oprahsKindness.jpg')
      self.names.append ( 'enchantments/privateContract.jpg')
      self.names.append ( 'enchantments/redRibbonArmy.png')
      self.names.append ( 'enchantments/stricklandsDiscipline.jpg')
      self.names.append ( 'enchantments/theCheeseStandsAlone.jpg')
      self.names.append ( 'enchantments/totalBodyProsthesis.png')
      self.names.append ( 'instants/Race.jpg')
      self.names.append ( 'instants/aestheticConsultation.jpg')
      self.names.append ( 'instants/capitolOffense.png')
      self.names.append ( 'instants/counterSpell.jpg')
      self.names.append ( 'instants/curseOfTheRetarded.jpg')
      self.names.append ( 'instants/darkRitual.jpg')
      self.names.append ( 'instants/duh.jpg')
      self.names.append ( 'instants/enchantmentUndertheSea.jpg')
      self.names.append ( 'instants/forcePush.jpg')
      self.names.append ( 'instants/gameOver.jpg')
      self.names.append ( 'instants/getALife.jpg')
      self.names.append ( 'instants/gigawattBolt.jpg')
      self.names.append ( 'instants/holyHandgrenade.jpg')
      self.names.append ( 'instants/iocanePowder.jpg')
      self.names.append ( 'instants/jediReflex.jpg')
      self.names.append ( 'instants/justDesserts.jpg')
      self.names.append ( 'instants/kanyeInterrup.jpg')
      self.names.append ( 'instants/molotov.png')
      self.names.append ( 'instants/moreOrLess.png')
      self.names.append ( 'instants/notToday.jpg')
      self.names.append ( 'instants/rickRoll.jpg')
      self.names.append ( 'instants/shotInTheArm.jpg')
      self.names.append ( 'instants/subtleInnuendo.jpg')
      self.names.append ( 'instants/sugarRush.png')
      self.names.append ( 'instants/swiftDeath.jpg')
      self.names.append ( 'instants/unplug.jpg')
      self.names.append ( 'instants/veryCrypticCommand.jpg')
      self.names.append ( 'instants/whoWhatWhenWhereWhy.jpg')
      self.names.append ( 'lands/black.jpg')
      self.names.append ( 'lands/blue.jpg')
      self.names.append ( 'lands/cliffsOfInsanity.jpg')
      self.names.append ( 'lands/deathStar.jpg')
      self.names.append ( 'lands/fireSwamp.jpg')
      self.names.append ( 'lands/green.jpg')
      self.names.append ( 'lands/pitOfDespair.jpg')
      self.names.append ( 'lands/red.jpg')
      self.names.append ( 'lands/white.jpg')
      self.names.append ( 'sorcery/Visage of the Dread Pirate.jpg')
      self.names.append ( 'sorcery/assWhuppin.png')
      self.names.append ( 'sorcery/combTheDesert.jpg')
      self.names.append ( 'sorcery/damnation.jpg')
      self.names.append ( 'sorcery/fiveFingerDiscount.jpg')
      self.names.append ( 'sorcery/hotFix.png')
      self.names.append ( 'sorcery/iKnowKungFu.jpg')
      self.names.append ( 'sorcery/inspirationalHeadBump.jpg')
      self.names.append ( 'sorcery/lastOneStanding.jpg')
      self.names.append ( 'sorcery/ludicrousSpeed.jpg')
      self.names.append ( 'sorcery/manureDump.jpg')
      self.names.append ( 'sorcery/michaelBay.jpg')
      self.names.append ( 'sorcery/naturalSpring.jpg')
      self.names.append ( 'sorcery/order66.jpg')
      self.names.append ( 'sorcery/organHarvest.png')
      self.names.append ( 'sorcery/peasants.png')
      self.names.append ( 'sorcery/ponder.jpg')
      self.names.append ( 'sorcery/powerNap.jpg')
      self.names.append ( 'sorcery/reallyEpicPunch.jpg')
      self.names.append ( 'sorcery/riseOfTheDarkRealms.jpg')
      self.names.append ( 'sorcery/scoutThePerimeter.jpg')
      self.names.append ( 'sorcery/timeWalk.jpg')
      self.names.append ( 'mtg.jpg')