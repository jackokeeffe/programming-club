#More Advanced Example

# Each tile is 3x3 and costs $0.14
# Cover 120x120 area
# 120/3 = # of tiles
# ((120 * 120)//(3*3))*0.14

# Floor size and tile size must be the same units (maybe you could optimize this?)
floor_size = input("Floor Size (4x7): ")
tile_size = input("Tile Size (4x7): ")
tile_cost = float(input("Tile Cost (0.14): "))

floor_x = int(floor_size.split("x")[0])
floor_y = int(floor_size.split("x")[1])
floor_area = floor_x * floor_y

# Usually the same (but for safety)
tile_x = int(tile_size.split("x")[0])
tile_y = int(tile_size.split("x")[1])
tile_area = tile_x * tile_y

# // because you cannot buy half a tile
cost = ((floor_area)//(tile_area))*tile_cost
#num_tiles = (floor_area)//(tile_area)
#cost = num_tile * tile_cost

# Don't display a trillion decimal places
print(str(cost).split(".")[0] + "." + str(cost).split(".")[1][:2])

# or use round()
print(round(cost))
print(cost)

# Check: https://www.calculator.net/tile-calculator.html