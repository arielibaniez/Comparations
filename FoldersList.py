from smb.SMBConnection import SMBConnection

userID = 'user'
password = 'password'			#Parametros que se usan para la conexión. 
client_machine_name = 'localpcname'

server_name = 'servername'
server_ip = '0.0.0.0'

domain_name = 'domainname'

conn = SMBConnection(userID, password, client_machine_name, server_name, domain=domain_name, use_ntlm_v2=True,
                     is_direct_tcp=True)

assert conn.connect(server_ip, 139)

shares = conn.listShares()

filesList = []
for share in shares:
    if not share.isSpecial and share.name not in ['NETLOGON', 'SYSVOL']:
        sharedfiles = conn.listPath(share.name, '/')				#Recorro las carpetas y tomo los nombres de las carpetas. 
        for sharedfile in sharedfiles:
            	fileName= sharedfile.filename
        	    filesList.append(fileName)

def folderList(filesList):
    return filesList
    