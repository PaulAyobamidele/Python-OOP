class TV:
    def __init__(self, brand, location):
        self.brand = brand
        self.location = location
        self.isOn = False
        self.isMuted = False

        self.channelList = [2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 14]
        self.nChannels = len(self.channelList)
        self.channelIndex = 0
        self.VOLUME_MINIMUM = 0
        self.VOLUME_MAXIMUM = 100
        self.volume = self.VOLUME_MAXIMUM

    def power(self):
        self.isOn = not self.isOn  # toggle

    def volumeUp(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume < self.VOLUME_MAXIMUM:
            self.volume = self.volume + 1

    def volumeDown(self):
        if not self.isOn:
            return
        if self.isMuted:
            self.isMuted = False
        if self.volume > self.VOLUME_MINIMUM:
            self.volume = self.volume - 1

    def channelUp(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex + 1
        if self.channelIndex > self.nChannels:
            self.channelIndex = 0

    def channelDown(self):
        if not self.isOn:
            return
        self.channelIndex = self.channelIndex - 1
        if self.channelIndex < 0:
            self.channelIndex = self.nChannels - 1

    def mute(self):
        if not self.isOn:
            return
        self.isMuted = not self.isMuted

    def setChannel(self, newChannel):
        if not self.isOn:
            return
        if newChannel in self.channelList:
            self.channelIndex = self.channelList.index(newChannel)
        else:
            raise ValueError("Channel not available")

    def showInfo(self):
        if not self.isOn:
            return
        print()
        print("TV Status:")
        if self.isOn:
            print("  Power: ON")
            print(" Channel:", self.channelList[self.channelIndex])
            if self.isMuted:
                print(" Volume is:", self.volume, "(sound is muted)")
            else:
                print(" Volume is:", self.volume)
        else:
            print("  Power: OFF")


# Testing out our code
if __name__ == "__main__":
    oTV = TV()
    oTV.power()
    oTV.showInfo()

    oTV.channelUp()
    oTV.channelUp()
    oTV.volumeUp()
    oTV.volumeUp()
    oTV.showInfo()

    oTV.power()
    oTV.mute()
    oTV.showInfo()
    oTV.power()
    oTV.showInfo()

    # Lower the volume, mute the sound, show status
    oTV.volumeDown()
    oTV.mute()
    oTV.showInfo()
    # Change the channel to 11, mute the sound, show status
    oTV.setChannel(12)
    oTV.mute()
    oTV.showInfo()


oTV1 = TV()
oTV2 = TV()


oTV1.power()
oTV2.power()


oTV1.volumeUp()
oTV1.volumeUp()


oTV2.volumeUp()
oTV2.volumeUp()
oTV2.volumeUp()

oTV2.volumeUp()

oTV2.volumeUp()
oTV2.volumeUp()


oTV2.setChannel(12)
oTV2.mute()


oTV1.showInfo()
oTV2.showInfo()


oTV1 = TV("Samsung", "Living Room")
oTV2 = TV("LG", "Bedroom")
oTV1.power()
