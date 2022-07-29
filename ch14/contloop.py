counter = 0
while counter <= 10:
    if counter % 2 == 0:
        counter += 1
        continue  # this will skip to the next iteration of the loop
    print("The odd counter is: " + str(counter))
    counter += 1

count = 1
while count <= 5:
    if count % 2 == 0:
        break # this will completely stop looping
    print("The count is: " + str(count))
    count += 1

