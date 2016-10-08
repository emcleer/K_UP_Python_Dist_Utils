
import pyodbc

# dvr = 'DRIVER={{SQL Server}}'
dvr = 'DRIVER={{SQL Server Native Client 10.0}}'
uid = 'UID=kryan'
app = 'APP=Python27'
trs = 'Trusted_Connection=yes'
cstr = '{0};{{0}};{{1}};{1};{2};{3}'.format(dvr, uid, trs, app)

def _connect(server, database):
    conn = pyodbc.connect(cstr.format(server, database))
    curs = conn.cursor()
    return conn, curs

def connect_to_mscrm():
    return _connect('SERVER=KPSQL03', 'DATABASE=KeaneCRM_MSCRM')

def connect_to_keastone():
    return connect_to_mscrm()

def connect_to_dw():
    return _connect('SERVER=KPRPT01', 'DATABASE=KeaneDW')

def connect_to_kenio(db='KENIO'):
    return _connect('SERVER=KPSQL07', 'DATABASE={0}'.format(db))

def connect_to_kfin(db='KFIN'):
    return _connect('SERVER=KPSQL07', 'DATABASE={0}'.format(db))

def connect_to_khold(db='KHOLD'):
    return _connect('SERVER=KPSQL07', 'DATABASE={0}'.format(db))
