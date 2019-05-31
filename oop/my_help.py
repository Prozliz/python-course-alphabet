from homework import *

a = Cat(16)
'''print(a.run(1))
print(a.saturation_level)
* Implement private method _set_average_speed
      if age less or eq 7 return 12
      if age between 7(not including) and 10(including) return 9
      if age grosser than 10(not including) return 6

    * Implement method run it receives hours value
      Calculate run km per hours remember that you have average_speed value
      Than if your cat run more or eq than 25 _reduce_saturation_level with value 2
      if it runs between 25(not including) and 50(including) than _reduce_saturation_level with value 5
      if it runs between 50(not including) and 100(including) than _reduce_saturation_level with value 15
      if it runs between 100(not including) and 200(including) than _reduce_saturation_level with value 25
      if it runs more than 200(not including) than _reduce_saturation_level with value 50'''
b = House()
e = Wall(2, 4)
#print(e.number_of_rolls_of_wallpaper(2,3))
#print(b.create_wall(4,5))
b.create_wall(10,2.5)
b.create_wall(14,2.5)
b.create_wall(14,2.5)
b.create_wall(10,2.5)
b.create_window(2,3)
b.create_window(1,3)
b.create_door(3,1)
#print(b.get_number_of_rolls_of_wallpapers(0.53,10))
#print(b.get_walls_square())
print(b.get_room_square())