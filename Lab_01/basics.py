# ===== Exercise 1: Variables and Data Types =====
print("--- Exercise 1: Variables and Data Types ---")
width = 640
height = 480
image_name = "sample.png"
is_color = True

print(width, type(width))
print(height, type(height))
print(image_name, type(image_name))
print(is_color, type(is_color))

total_pixels = width * height
print("Total pixels:", total_pixels)

# ===== Exercise 2: if, elif, and else =====
print("\n--- Exercise 2: if, elif, and else ---")
for intensity in [-1, 0, 127, 128, 255, 256]:
    if intensity < 0 or intensity > 255:
        label = "Invalid"
    elif intensity >= 128:
        label = "Bright pixel"
    else:
        label = "Dark pixel"
    print(intensity, "->", label)

# ===== Exercise 3: for and while Loops =====
print("\n--- Exercise 3: for and while Loops ---")
# for loop with threshold 128
for value in [20, 130, 255]:
    if value >= 128:
        print(value, "-> Bright pixel")
    else:
        print(value, "-> Dark pixel")

# while loop: prints 0, 1, 2 and stops before 3
counter = 0
while counter < 3:
    print(counter)
    counter = counter + 1  # update the loop counter

# ===== Exercise 4: Functions =====
print("\n--- Exercise 4: Functions ---")
def is_bright(pixel, threshold=128):
    if pixel >= threshold:
        return True
    else:
        return False

print(is_bright(127))
print(is_bright(128))
print(is_bright(200, 210))

# ===== Exercise 5: Lists and Tuples =====
print("\n--- Exercise 5: Lists and Tuples ---")
pixels = [0, 128, 255]
print("First item:", pixels[0])
pixels[1] = 150      # replace the middle item
pixels.append(64)    # add a new item at the end
print("List:", pixels)
print("Length:", len(pixels))

size = (640, 480)
width, height = size  # tuple unpacking
print("Width:", width)
print("Height:", height)
# A list is mutable, so its items can be changed in place (assignment, append).
# A tuple is immutable, so its items cannot be changed after creation.

# ===== Exercise 6: Dictionaries and Sets =====
print("\n--- Exercise 6: Dictionaries and Sets ---")
image = {"width": 640, "height": 480}
image["mode"] = "RGB"
print("Width:", image["width"])
print("Mode:", image["mode"])

labels = set(["cat", "dog", "cat", "bird"])
print("Unique labels:", len(labels))