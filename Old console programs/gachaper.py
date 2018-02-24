# -*- coding: utf-8 -*-

import sys, random

AVG_TRIALS = 10

def main(part):
    cnt = 0
    for i in range(0, AVG_TRIALS):
        cnt += getCompGachaCount(part)
    comp_times = cnt / AVG_TRIALS
    cnt = 0.00
    for i in range(0, AVG_TRIALS):
        cnt += getSuperRareOdds(comp_times)
    s_rare_odds = cnt / AVG_TRIALS

    return (comp_times, s_rare_odds)
def getCompGachaCount(part):
    p = (int)(part)
    list = [False] * p  
    comp = [True] * p   
    cnt = 0
    while(list != comp):
        i = random.randint(0, part - 1)
        list[i] = True
        cnt += 1

    return cnt
def getSuperRareOdds(times):
    i = 0
    odds = 0.1
    while(True):
        i += 1
        if (random.random() <= odds):
            odds -= 0.01
            i = 0
            continue
        if times <= i:
            return odds
argv = sys.argv
argc = len(argv)
if (argc != 3):
    print 'usage: python %s [part] [trials]' % argv[0]
    quit()

part = (int)(argv[1])
AVG_TRIALS = (int)(argv[2])

timesum = 0.0
s_raresum = 0.0
for i in range(0, AVG_TRIALS):
    times, s_rare = main(part)
    timesum += times
    s_raresum += s_rare

print "試行 %d回" % AVG_TRIALS
print "ガチャコンプ平均回数 %f回" % (float)(timesum / AVG_TRIALS)
print "対応スーパーレア平均確率 %g" % (float)(s_raresum / AVG_TRIALS)
