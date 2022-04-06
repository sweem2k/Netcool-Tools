# Marquell D 4/4/22
# Pull all the unproccesed alerts from Netcool using the REST API
# https://www.ibm.com/docs/en/netcoolomnibus/8.1?topic=SSSHTQ_8.1.0/com.ibm.netcool_OMNIbus.doc_8.1.0/omnibus/wip/api/reference/omn_api_http_eg_jsonrowsetget.html
# https://www.ibm.com/docs/en/SSNFET_9.2.0/com.ibm.netcool_OMNIbus.doc_7.4.0/omn_pdf_api_http_master.pdf
# https://www.ibm.com/docs/fi/nnm/9.2.0?topic=SSNFET_9.2.0/com.ibm.netcool_OMNIbus.doc_7.4.0/omnibus/wip/api/reference/omn_api_http_queryparameters.html


import sys
import requests
import urllib.parse
from requests.auth import HTTPBasicAuth
import json

def nc_unproc():

    #Netcool URL 
    #url = 'http://810-monitoringlab01.custcbb.local:8080/objectserver/restapi/alerts/status'
    url = 'http://810-object01.ldap.custcbb.local:8080/objectserver/restapi/alerts/status'

    #username
    username = "rest.api"
    #pass
    password = "rest"


    #Set the header information.
    #headers = {'Accept': 'application/json','Host': '810-monitoringlab01.custcbb.local'}
    headers = {'Accept': 'application/json','Host': '810-object01.ldap.custcbb.local'}

    # uuencode/ URI encoded characters
    # %3D =
    # %27 '
    # %2C ,
    # %20 space
    #filter on the Acknowledge = 0 
    #nc_filter = "?filter=Acknowledged%3D0ANDSeverity%20>4"

    #using urllib.parse.quote to encode the query these have to be on a single line or it wont encode correctly
    nc_filter = "?filter=" + urllib.parse.quote("(Severity > 4 AND Node != '810-object01.ldap.custcbb.local' AND Node != '810-webgui02.ldap.custcbb.local' AND Summary NOT LIKE 'Real Error: Port: 22 responded successfully' AND SMCReference NOT LIKE 'IA:' AND SMCReference NOT LIKE 'TT:' AND SMCReference NOT LIKE 'CC:')")
    nc_filter += urllib.parse.quote(" OR ( Severity > 4 AND Node != '810-object01.ldap.custcbb.local' AND Node != '810-webgui02.ldap.custcbb.local' AND Summary NOT LIKE 'Real Error: Port: 22 responded successfully' AND SMCReference LIKE 'CC:' AND Acknowledged = 0)")
    #print(nc_filter)


    # field name list Severity, Count, Flashing, SMC, Node, Acknowledged, Customer, Summary, Manager, FirstOccurrence, LastOccurrence
    #nc_filter_col = "&collist=Severity%2CTally%2CFlash%2CSMCReference%2CNode%2CAcknowledged%2CCustomer%2CSummary%2CManager%2CFirstOccurrence%2CLastOccurrence"
    nc_filter_col = "&collist=" + urllib.parse.quote("Severity,Tally,Flash,SMCReference,Node,Acknowledged,Customer,Summary,Manager,FirstOccurrence,LastOccurrence")

    #combine nc filter and nc colum list
    nc_fil = str(nc_filter) + str(nc_filter_col)
    #nc_fil = str(nc_filter) 
    url += str(nc_fil)

    try:
        #sent the GET request to pull all unproccesed alerts.
        response = requests.get(url, headers=headers, auth = HTTPBasicAuth(username, password))
        #print(response.status_code)
        return(json.loads(response.text))
    except:
        return(1) 
    #print(f"error:{response}")


    ####DEBUG###   
    #print(response.text)
    #print(response.status_code)
    #print(url)