#Task 1: Validating Calculations
#volume of a cube minus a cylinder
#volume of a cone = (pi)r^2 h/3
#volume of a cylinder = (pi) r^2 h
PI = 3.1415925359
cone_radius = 4.23 #radius of the cone
cone_height = 7 #height of the cone
cylinder_radius = 1.3 #radius of the cylinder
cylinder_height = .9 #height of the cylinder
area_no_paren = PI * cone_height / 3 * cone_radius ** 2 - PI * cylinder_radius ** 2 * cylinder_height #formula without parenthesis
print("The area of the cone minus the cylinder is " + str(area_no_paren) + " square units when not using parenthesis")

area_paren = PI * ((cone_radius ** 2) * (cone_height / 3)) - (PI * (cylinder_radius ** 2) * cylinder_height) #formula with parenthesis
print("The area of the cone minus the cylinder  is " + str(area_paren) + " square units when using parenthesis")

if area_no_paren == area_paren:
    print("They match!")
else:
    print("They don't match")

#Task 2: Mix and Match
# make sure a rectangular prism fits inside a cube. expression to be used: rec_length * rec_width * rec_depth < cube_edges **3 and rec_lenth < cube_edges and rec_width < cube_edges and rec_depth < cube edges
rec_length = 3.0 #length of the rectangular prism
rec_width = 4.2 #width/height of the rectangular prism
rec_depth = 5.3 #depth of the rectangular prism
cube_edges = 6.0 #the size of the egdes of our cube
#prediction: it will fit
if rec_length * rec_width * rec_depth < cube_edges **3 and rec_length < cube_edges and rec_width < cube_edges and rec_depth < cube_edges:
    print("The rectangular prism fits inside the cube")
else:
    print("The rectangular prism will not fit inside the cube")
