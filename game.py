from mcpi.minecraft import Minecraft
mc = Minecraft.create()
from datetime import datetime
import time
import random
size = 30
print(mc.player.getTilePos())
x_start, y_start, z_start = mc.player.getTilePos()
stone = 4
mc.setBlocks(x_start, y_start - 1, z_start, x_start + size, y_start - 1, z_start + size, 4)
mc.setBlocks(x_start, y_start - 3, z_start, x_start + size, y_start - 3, z_start + size, 11)
for x in range(size):
    for z in range(size):
        mc.setBlock(x_start + x, y_start, z_start + z, random.choice([0, 0, 0, 171]))
    z = z_start
mc.postToChat("игра начнется через несколько секунд")
time.sleep(10)
mc.postToChat("игра началась")
while True:
    x, y, z = mc.player.getTilePos()
    if x < x_start or x > x_start + size or z < z_start or z > z_start + size:
        mc.player.setTilePos(41, 71, 589)
        break
    if mc.getBlock(x, y, z) == 171:
        mc.player.setTilePos(41, 71, 589)
        break
    if mc.getBlock(x, y, z) == 11 or mc.getBlock(x, y, z) == 10:
        break
    mc.setBlock(x, y - 1, z, 0)

mc.postToChat("игра закончена")









