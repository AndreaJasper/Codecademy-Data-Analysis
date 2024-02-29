paintings = ["The Two Fridas", "My Dress Hangs Here", "Tree of Hope", "Self Portrait With Monkeys"]
dates = [1939, 1933, 1946, 1940]
paintings = list(zip(paintings, dates))
# print(paintings)

additional_paintings = ["The Broken Column", "THe Wounded Deer", "Me and My Doll"]
additional_dates = [1944, 1946, 1937]
additional_paintings = list(zip(additional_paintings, additional_dates))

paintings.extend(additional_paintings)
# print(paintings)

# print(len(paintings))

audio_tour_number = list(range(1, 8))
# print(audio_tour_number)

master_list = list(zip(audio_tour_number, paintings))
print(master_list)