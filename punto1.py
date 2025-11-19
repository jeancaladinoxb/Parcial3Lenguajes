class Nodo:
    def __init__(self, trad=""):
        self.trad = trad


def Expr(valor):
    nodo = Nodo()
    nodo.trad = str(valor)
    return nodo


def Campos(id, rcampos):
    nodo = Nodo()
    nodo.trad = id + rcampos.trad
    return nodo

def RCampos(lista_ids):
    if not lista_ids:
        return Nodo("")  
    trad = ""
    for item in lista_ids:
        trad += ", " + item
    return Nodo(trad)

def Condicion(expr=None):
    if expr is None:
        return Nodo("")  
    return Nodo(" WHERE " + expr.trad)

def Select(campos, tabla, condicion):
    nodo = Nodo()
    nodo.trad = "SELECT " + campos.trad + " FROM " + tabla + condicion.trad
    return nodo

def Lista(expresiones):
    nodo = Nodo()
    nodo.trad = ", ".join([e.trad for e in expresiones])
    return nodo

def Insert(tabla, lista):
    nodo = Nodo()
    nodo.trad = f"INSERT INTO {tabla} VALUES ({lista.trad})"
    return nodo


def Asignaciones(pares):
    nodo = Nodo()
    asigns = []
    for identificador, expr in pares:
        asigns.append(f"{identificador} = {expr.trad}")
    nodo.trad = ", ".join(asigns)
    return nodo

def Update(tabla, asigns, condicion):
    nodo = Nodo()
    nodo.trad = f"UPDATE {tabla} SET {asigns.trad}{condicion.trad}"
    return nodo

def Delete(tabla, condicion):
    nodo = Nodo()
    nodo.trad = f"DELETE FROM {tabla}{condicion.trad}"
    return nodo

def Q(nodo):
    return nodo.trad


if __name__ == "__main__":
    campos = Campos("nombre", RCampos(["edad"]))
    cond = Condicion(Expr("edad > 20"))
    consulta_select = Select(campos, "Usuarios", cond)
    print("SELECT →", Q(consulta_select))

    lista = Lista([Expr(1), Expr("'Jeancarlo'"), Expr(22)])
    consulta_insert = Insert("Usuarios", lista)
    print("INSERT →", Q(consulta_insert))

    asigns = Asignaciones([
        ("nombre", Expr("'Jeancarlo'")),
        ("edad", Expr(22))
    ])
    cond2 = Condicion(Expr("id = 1"))
    consulta_update = Update("Usuarios", asigns, cond2)
    print("UPDATE →", Q(consulta_update))

    cond3 = Condicion(Expr("id = 1"))
    consulta_delete = Delete("Usuarios", cond3)
    print("DELETE →", Q(consulta_delete))
