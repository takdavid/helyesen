# -*- encoding: utf-8 -*-

import helyesen.az as az
import helyesen.naknek as naknek

print naknek.say(az.say(u'szolgáltatás')).encode('utf-8')
print naknek.say(az.say(u'áramszolgáltatás')).encode('utf-8')

