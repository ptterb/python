import pygame.mixer
from time import sleep
from sys import exit

pygame.mixer.init(48000, -16, 1, 1024)
soundA = pygame.mixer.Sound("/usr/share/sounds/alsa/Front_Center.wav")

soundChannelA = pygame.mixer.Channel(1)

print "Soundboard Ready."

soundChannelA.play(soundA)
sleep(1)
soundChannelA.play(soundA)
sleep(1)

exit()
