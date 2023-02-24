database = {
    "RAPIDEZ": 
    {
        "ATENCION":
        {
            "code_words":
            [
                "atención"
            ],
            "phrases":
            [
                "ágil", "ahorras tiempo", "al momento", "a la brevedad", "diligente", "disponibles en poco tiempo", "disponibles en breve",
                "en tiempo reducido", "En el/Al Momento", "Inmediata", "Instantánea", "Dinámica", "Oportuna", "Pronta",
                "prontitud", "Rápida", "Rápido tiempo de espera", "Sin demora/Con poca espera", "Sin filas largas", "Sin tiempo de espera",
            ]
        },
        "REQUERIMIENTO":
        {
            "code_words":["Gestión", "Respuesta", "Ejecución", "Asesoría", "Servicio", "Trámites", "Solicitud", "Operación", "Proceso", "Resultado",],
            "phrases":
            [
                "Ágil", "Ágil en resolver requerimiento", "Antes de lo esperado", "A la brevedad", "A tiempo",
                "Al llamar te atienden rápido", "Celeridad", "Con velocidad", "Corto plazo", "Día-semana-mes", "En breve",
                "Enseguida", "Excelente tiempo de respuesta", "Inmediata", "Poco tiempo", "Pronta", "Rápida/o",
                "Respondieron rápido al llamado", "Sin demora",
            ]
        },
        "SOLUCIONDEPROBLEMAS":
        {
            "code_words":["Cambios", "Devoluciones"],
            "phrases":
            [
                "No se demoran", "Poca espera", "Rápido", "Sin espera", "Sin pérdida de tiempo",
            ]
        },
        "TRANSACCIONCOMPRAS":
        {
            "code_words": ["venta", "cobros", "pagos", "procesos de pago", "curse"],
            "phrases":
            [
                "Ágil", "Celeridad", "Con velocidad", "Rápida/o", "Sin espera", "Poca espera", "Poca espera en cajas", "Sin filas en papeleo", "Sin filas en trámites"
            ]
        },
        "IMPLEMENTACIONDEAPOYO":
        {
            "code_words": ["Máquinas, POV"],
            "phrases":["Rápido"]
        },
        "PLATAFORMASDIGITALES":
        {
            "code_words": ["plataforma digital", "infrastructura digital", "infrastructura virtual"],
            "phrases":
            [
                "Acceso rápido", "Rapidez para efecturar trámites", "Despliega información rápida", "Rápida",
            ]
        },
        "RECEPCIONVEHICULO":
        {
            "code_words": ["recepción vehiculo"],
            "phrases": ["ágil", "rápido"]
        },
        "MANTENCIONVEHICULO":
        {
            "code_words": ["mantención vehículo", "reparación vehículo", "revisión vehículo"],
            "phrases": ["en el día", "rápido"]
        },
        "REPARTIDOR":
        {
            "code_words":["entrega", "despacho", "distribuidor", "repartidor",],
            "phrases":
            [
                "ágil", "antes de lo esperado", "celeridad", "con velocidad", "corto plazo", "corre", "dentro de 15-20 minutos", "en poco tiempo",
                "inmediato", "llega rápido", "poca espera", "pronto", "rápido", "rapidez de entrega", "tiempos de espera mínimo" , "antes de lo esperado",
            ]
        },
        "SERVICIOENGENERAL":
        {
            "code_words":["general",],
            "phrases":["rápido"]
        },
        "SERVICIOPOSTVENTA":
        {
            "code_words":["postventa",],
            "phrases": ["rápido",]
        },
        "RECEPCIONDEFACTURAS":
        {
            "code_words":["facturas",],
            "phrases": ["rápido",]
        }
    }
}

def GetDatabase():
    return database