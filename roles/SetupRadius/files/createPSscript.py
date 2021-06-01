from jinja2 import Environment, FileSystemLoader, Template
import yaml

#Set file root to ansible root
ENV = Environment(loader=FileSystemLoader('./'))

#Get the template from the DHCP role template folder
template = ENV.get_template("./roles/SetupRadius/templates/radius.j2")

#write to file and save it at the role/script folder.
with open("./roles/SetupRadius/files/final_radius.ps1", "w") as file:
    file.write(template.render())

