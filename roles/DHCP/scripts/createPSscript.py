from jinja2 import Environment, FileSystemLoader, Template
import yaml
from ansible.plugins.filter import ipaddr

#Set file root to ansible root
ENV = Environment(loader=FileSystemLoader('./'))

#Add the ipaddr filter to the environment during troubleshooting.
#f = ipaddr.FilterModule()
#ENV.filters.update(f.filters())

#Load the 2 used group vars YAML files
with open("./group_vars/VibDisSW/VibDisSW.yml") as inputfile:
    scope1 =  yaml.full_load(inputfile)
with open("./group_vars/RosDisSW/RosDisSW.yml") as inputfile:
    scope2 =  yaml.full_load(inputfile)

#Get the template from the DHCP role template folder
template = ENV.get_template("./roles/DHCP/templates/dhcp.j2")

#write to file and save it at the role/script folder.
with open("./roles/DHCP/files/final_dhcp.ps1", "w") as file:
    file.write(template.render(scope1=scope1,scope2=scope2))

