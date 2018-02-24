def choose(candidates, probabilities):
    probabilities = [sum(probabilities[:x+1]) for x in range(len(probabilities))]
    if probabilities[-1] > 1.0:
        probabilities = [x/probabilities[-1] for x in probabilities]
        rand = random.random()
        for candidate, probability in zip(candidates, probabilities):
            if rand < probability:
                return candidate
candidates = [u'5”{',u'10”{',u'30”{',u'50”{',u'100”{',u'300”{',7]
probabilities = [0.3, 0.2, 0.15, 0.125, 0.125, 0.09, 0.01]
a = choose([u'5”{',u'10”{',u'30”{',u'50”{',u'100”{',u'300”{',7], [0.3, 0.2, 0.15, 0.125, 0.125, 0.09, 0.01])
print a
