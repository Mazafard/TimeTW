#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
import jdatetime
import autho as ao


auth = tweepy.OAuthHandler(ao.CONSUMER_KEY, ao.CONSUMER_SECRET)
auth.set_access_token(ao.ACCESS_KEY, ao.ACCESS_SECRET)
api = tweepy.API(auth)


def tweet(f):
    api.update_status(f)


def increase(l):
    return all(x == y-1 for x, y in zip(l, l[1:]))


def decrease(l):
    return all(x == y+1 for x, y in zip(l, l[1:]))



def equal(l):
    return all(x == y + 12 or x+12 == y or x == y for x, y in zip(l, l[1:]))


def check(t):
    h, h1, h2 = t.hour, t.hour / 10, t.hour % 10
    m, m1, m2 = t.minute, t.minute / 10, t.minute % 10
    num = [h1, h2, m1, m2]
    num2 = [h, m]

    a = decrease(num)
    b = increase(num)
    c = equal(num2)
    f = str(h1) + str(h2) + ':' + str(m1)+str(m2)
    n = ' \nTime is Expensive \n #Motime'

    if a or b or c:
        stat = ''
        if a:
            stat = 'Decrease \n'
        if b:
             stat = 'Increase \n'
        if c:
            stat = 'Equal \n'
        tweet(stat+f+n)
        print 'yes'
        print f, t, h, h1, h2, m, m1, m2, 'a:', a, 'b:', b, 'c:', c
    else:
        print 'no'
        print f, t, h, h1, h2, m, m1, m2, 'a:', a, 'b:', b, 'c:', c

a = jdatetime.datetime.now()


check(a)
