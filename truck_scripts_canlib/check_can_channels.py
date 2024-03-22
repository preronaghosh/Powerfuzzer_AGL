from canlib import canlib

num_channels = canlib.getNumberOfChannels()
print("Found {} channels".format(num_channels))
for ch in range(num_channels):
    chd = canlib.ChannelData(ch)
    print("{}  {} ({} / {})".format(ch,chd.channel_name,chd.card_upc_no,chd.card_serial_no))

