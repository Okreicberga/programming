# PRogram stores a sudent name and a list of her courses and grades ina dict
# PRogram output student's data
# Author: Olga Kreicberga 

student = {
    "name":"MAry",
    "modules": [
        {
            "courseName":"Programming",
            "grade": 45
        },
        {
            "courseName":"History",
            "grade":99

        }
    ]
}
print ("Student: {}".format(student["name"]))
for module in student ["modules"]:
    print("\t {} \t: {}".format (module["courseName"], module ["grade"]))