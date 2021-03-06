from xml.dom import minidom

net_xml = minidom.parse("network_objects.xml")

NetworkObjectsTag = net_xml.getElementsByTagName("network_objects")[0]

# Pull individual network objects
NetworkObjectTag = NetworkObjectsTag.getElementsByTagName("network_object")

for network_object in NetworkObjectTag:
    name = network_object.getElementsByTagName("Name")[0].firstChild.data
    class_name = network_object.getElementsByTagName("Class_Name")[0].firstChild.data
    color = network_object.getElementsByTagName("color")[0].firstChild.data
    ipElement = network_object.getElementsByTagName("ipaddr")
    if ipElement:    
        ipElement = network_object.getElementsByTagName("ipaddr")[0]
        ipaddr = ipElement.firstChild.data
    maskElement = network_object.getElementsByTagName("netmask")
    if maskElement:
        maskElement = network_object.getElementsByTagName("netmask")[0]
        netmask = maskElement.firstChild.data
    #address_ranges
    ipaddr_firstElement = network_object.getElementsByTagName("ipaddr_first")
    if ipaddr_firstElement:
        ipaddr_firstElement = network_object.getElementsByTagName("ipaddr_first")[0]
        ipaddr_first = ipaddr_firstElement.firstChild.data
    ipaddr_lastElement = network_object.getElementsByTagName("ipaddr_last")
    if ipaddr_lastElement:
        ipaddr_lastElement = network_object.getElementsByTagName("ipaddr_last")[0]
        ipaddr_last = ipaddr_lastElement.firstChild.data    
    if ipaddr_firstElement:
        print(name,class_name,ipaddr,netmask,ipaddr_first,ipaddr_last,color)
    else:
            print(name,class_name,ipaddr,netmask,color)
