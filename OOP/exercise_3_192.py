# This Exercise is to count total number of objects declared in a class.
# Logic is, we define a class variable "instance_count = 0" and we know as per concept that whenever we
# create an object it first calls INIT Method, so when there is no object declared, it will print 0.
# execute Program:1 to see this.
# Now once we create the object p1 then INIT Method would be called so we increase the class variable
# with 1 count and hence after creating p1 object, it should print total number of object as 1.
# execute Program:2 to see this.

# Hence with this Logic we can keep incrementing the class variable i.e. instance_count with 1 everytime
# when we create an object.
# See and execute Program:3 to see this.

## Program:1
# class Probes:
#     instance_count = 0 
#     def __init__(self, probe_name, launch_month, launch_year):
#         self.voyager_probe_name   = probe_name
#         self.voyager_launch_month = launch_month
#         self.voyager_launch_year  = launch_year
#         self.voyager_launch       = launch_month + ' ' + launch_year
#
# print(Probes.instance_count) # we are printing the count of object before creating object p1, p2
# p1 = Probes('voyager1', 'Sep', '1977')
# p2 = Probes('voyager2', 'Aug', '1977' )
# print(f"voyager1 was lunched in: {p1.voyager_launch}")
# print(f"voyager2 was lunched in: {p2.voyager_launch}\n")

## Program:2
# class Probes:
#     instance_count = 0 
#     def __init__(self, probe_name, launch_month, launch_year):
#         Probes.instance_count = Probes.instance_count + 1
#         self.voyager_probe_name   = probe_name
#         self.voyager_launch_month = launch_month
#         self.voyager_launch_year  = launch_year
#         self.voyager_launch       = launch_month + ' ' + launch_year
#
# p1 = Probes('voyager1', 'Sep', '1977')
# print(Probes.instance_count) # we are printing the count after ceating the object p1
# p2 = Probes('voyager2', 'Aug', '1977' )
# print(f"voyager1 was lunched in: {p1.voyager_launch}")
# print(f"voyager2 was lunched in: {p2.voyager_launch}\n")

## Program:3
# This is the Final Code.
class Probes:
    instance_count = 0 
    def __init__(self, probe_name, launch_month, launch_year):
        Probes.instance_count += 1
        self.voyager_probe_name   = probe_name
        self.voyager_launch_month = launch_month
        self.voyager_launch_year  = launch_year
        self.voyager_launch       = launch_month + ' ' + launch_year

p1 = Probes('voyager1', 'Sep', '1977')
p2 = Probes('voyager2', 'Aug', '1977' )
print(f"voyager1 was lunched in: {p1.voyager_launch}")
print(f"voyager2 was lunched in: {p2.voyager_launch}")
# print(Probes.instance_count)
# OR we can print with a message like this using f string:
print(f"Total number of objects declared are: {Probes.instance_count}")