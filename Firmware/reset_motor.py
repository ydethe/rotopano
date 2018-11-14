import pigpio


SLP_PIN = 27
pi = pigpio.pi()
pi.set_mode(SLP_PIN, pigpio.OUTPUT)

pi.write(SLP_PIN, 0)


