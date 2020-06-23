class Fabrica:
	public static AEstado GetConexion(tipoFabrica):
		if(TipoFabrica.equalsIgnoreCase(null)):
            return ConexionVacia()
        
        if(TipoFabrica.equalsIgnoreCase("Android")):
            return ConexionLavado()
        
        else if(TipoFabrica.equalsIgnoreCase("IOs")):
            return ConexionSecado()
        
        else return ConexionVacia()