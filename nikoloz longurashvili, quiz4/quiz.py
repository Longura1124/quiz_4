from os.path import split
# 1
# female = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[4] == "female":
#             female += 1
# print("female:", female)

# 2
# male = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[4] == "male":
#             male += 1
# print("male", male)

# 3
# survived_female = 0
# womp_womp = 0
# precent = 0
# total_female = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[4] == "female":
#             total_female += 1
#         if fields[1] == "1" and fields[4] == "female":
#             survived_female += 1
#         else:
#             if fields[1] == "0" and fields[4] == "female":
#                 womp_womp += 1
#
# precent = survived_female / total_female * 100
#
# print("female's that survived", survived_female)
# print("didnt survive (female)", womp_womp)
# print("precent of females's that survived",precent)

# 4
# womp_womp2 = 0
# survived_male = 0
# total_male = 0
# precent = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[4] == "male":
#             total_male += 1
#         if fields[1] == "1" and fields[4] == "male":
#             survived_male += 1
#         else:
#             if fields[1] == "0" and fields[4] == "male":
#                 womp_womp2 += 1
# precent = survived_male / total_male * 100
# print("male's that survived", survived_male)
# print("didnt survive(male)", womp_womp2)
# print("precent of man that survived",precent)

# 5
# first_class = 0
# second_class = 0
# third_class = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[2] == "1":
#             first_class += 1
#         elif fields[2] == "2":
#             second_class += 1
#         else:
#             third_class += 1
# print("First class:", first_class,"Seconds class:", second_class, "Third class:", third_class)

# 6
# first_class_price = 0
# first_class_count = 0
# with open("titanic.txt", "r") as titanic:
#     for line in titanic:
#         fields = line.strip().split(",")
#         if fields[2] == "1":
#             first_class_price +
