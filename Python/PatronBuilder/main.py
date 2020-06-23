from Director import *
from SqlConcreteBuilder import *
from OracleConcreteBuilder import *

conexion = Conector()
 
sqlconexion = SqlBuilder()
oracleconexion = OracleBuilder()

conexion.setConexionBuilder(sqlconexion)
conexion.makeConexion()

conexionRealizada = conexion.getConexion()

print(conexionRealizada.getServidor())
print(conexionRealizada.getNombreBD())

