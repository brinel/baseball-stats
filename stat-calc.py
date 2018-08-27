"""
This program will calculate a baseball player's
offensive statistics based on several inputs from
the user
"""

def player_stats():
    print "Hi! Provide the requested inputs and I'll tell you the player's season stats"
    player = str(raw_input("What is the player's name? "))
    PA = int(raw_input("How many plate appearances has %s had? " % player))
    SING = int(raw_input("How many singles has %s hit? " % player))
    while SING > PA:
        print "He can't have more singles than plate appearances dumdum... try again."
        SING = int(raw_input("How many singles has %s hit? " % player))
    DOUB = int(raw_input("How many doubles has %s hit? " % player))
    while DOUB > (PA - SING):
        print "He can't have more hits than plate appearances... try again."
        DOUB = int(raw_input("How many doubles has %s hit? " % player))
    TRIP = int(raw_input("How many triples has %s hit? " % player))
    while TRIP > (PA - SING - DOUB):
        print "He can't have more hits than plate appearances... try again."
        TRIP = int(raw_input("How many triples has %s hit? " % player))
    HR = int(raw_input("How many home runs has %s hit? " % player))
    while HR > (PA - SING - DOUB - TRIP):
        print "He can't have more hits than plate appearances... try again."
        HR = int(raw_input("How many home runs has %s hit? " % player))
    BB = int(raw_input("How many times has %s been walked? " % player))
    while BB > (PA - SING - DOUB - TRIP - HR):
        print "He can't have more hits and walks than plate appearances... try again."
        BB = int(raw_input("How many times has %s been walked? " % player))
    HBP = int(raw_input("How many times has %s been hit by a pitch? " % player))
    while HBP > (PA - SING - DOUB - TRIP - HR - BB):
        print "He can't have more times on base than plate appearances... try again."
        HBP = int(raw_input("How many times has %s been hit by a pitch? " % player))
    SAC = int(raw_input("How many sacrifices (bunts + flies) has %s had? " % player))
    while SAC > (PA - SING - DOUB - TRIP - HR - BB - SAC):
        print "He can't have more times on base and sacrifices than plate appearances... try again."
        SAC = int (raw_input("How many sacrifices (bunts + flies) has %s had? "))
    print PA, SING, DOUB, TRIP, HR, BB, HBP, SAC
    AVG = float(SING + DOUB + TRIP + HR) / float(PA - BB - HBP - SAC)
    OBP = float(SING + DOUB + TRIP + HR + BB + HBP) / float(PA)
    SLG = float((1 * SING) + (2 * DOUB) + (3 * TRIP) + (4 * HR)) / float(PA - BB - HBP - SAC)
    OPS = OBP + SLG
    print "Alright! Here are %s's ratios for the season: " % player
    print "%s's batting average is %10.3f" % (player, AVG)
    print "%s's on base percentage is %10.3f" % (player, OBP)
    print "%s's slugging percentage is %10.3f" % (player, SLG)
    print "%s's on base plus slugging in %10.3f" % (player, OPS)

player_stats()
