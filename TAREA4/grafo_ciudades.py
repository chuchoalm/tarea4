class GrafoNoDirigido:
    def __init__(self):
        """Inicializa el grafo con una lista de adyacencia vacía"""
        self.lista_adyacencia = {}
    
    def agregar_nodo(self, ciudad):
        """
        Agrega una ciudad (nodo) al grafo
        
        Args:
            ciudad: Nombre de la ciudad a agregar
        """
        if ciudad not in self.lista_adyacencia:
            self.lista_adyacencia[ciudad] = []
            print(f"✓ Ciudad '{ciudad}' agregada exitosamente")
        else:
            print(f"⚠ La ciudad '{ciudad}' ya existe en el grafo")
    
    def agregar_conexion(self, ciudad1, ciudad2, peso=None):
        """
        Agrega una conexión bidireccional entre dos ciudades
        
        Args:
            ciudad1: Primera ciudad
            ciudad2: Segunda ciudad
            peso: Peso opcional de la arista (distancia o costo)
        """
        # Verificar que ambas ciudades existan
        if ciudad1 not in self.lista_adyacencia:
            print(f"✗ Error: La ciudad '{ciudad1}' no existe")
            return
        if ciudad2 not in self.lista_adyacencia:
            print(f"✗ Error: La ciudad '{ciudad2}' no existe")
            return
        
        # Agregar conexión bidireccional
        if peso is not None:
            self.lista_adyacencia[ciudad1].append((ciudad2, peso))
            self.lista_adyacencia[ciudad2].append((ciudad1, peso))
            print(f"✓ Conexión agregada: {ciudad1} -- {ciudad2} (peso: {peso})")
        else:
            self.lista_adyacencia[ciudad1].append(ciudad2)
            self.lista_adyacencia[ciudad2].append(ciudad1)
            print(f"✓ Conexión agregada: {ciudad1} -- {ciudad2}")
    
    def visualizar_lista_adyacencia(self):
        """Muestra la lista de adyacencia del grafo"""
        print("\n" + "="*50)
        print("LISTA DE ADYACENCIA")
        print("="*50)
        
        if not self.lista_adyacencia:
            print("El grafo está vacío")
            return
        
        for ciudad, conexiones in sorted(self.lista_adyacencia.items()):
            if conexiones:
                conexiones_str = ", ".join(
                    f"{c[0]} (peso: {c[1]})" if isinstance(c, tuple) else str(c)
                    for c in conexiones
                )
                print(f"{ciudad} -> [{conexiones_str}]")
            else:
                print(f"{ciudad} -> []")
        print("="*50 + "\n")
    
    def generar_graphviz(self, nombre_archivo="grafo"):
        """
        Genera código Graphviz para visualizar el grafo
        
        Args:
            nombre_archivo: Nombre del archivo de salida
        """
        conexiones_agregadas = set()
        
        codigo_dot = "graph G {\n"
        codigo_dot += "    // Configuración del grafo\n"
        codigo_dot += "    node [shape=circle, style=filled, fillcolor=lightblue, fontname=Arial];\n"
        codigo_dot += "    edge [fontname=Arial];\n\n"
        codigo_dot += "    // Nodos\n"
        
        # Agregar nodos
        for ciudad in sorted(self.lista_adyacencia.keys()):
            codigo_dot += f'    "{ciudad}";\n'
        
        codigo_dot += "\n    // Aristas\n"
        
        # Agregar aristas (evitando duplicados)
        for ciudad1, conexiones in sorted(self.lista_adyacencia.items()):
            for conexion in conexiones:
                if isinstance(conexion, tuple):
                    ciudad2, peso = conexion
                    arista = tuple(sorted([ciudad1, ciudad2]))
                    if arista not in conexiones_agregadas:
                        conexiones_agregadas.add(arista)
                        codigo_dot += f'    "{ciudad1}" -- "{ciudad2}" [label="{peso}"];\n'
                else:
                    ciudad2 = conexion
                    arista = tuple(sorted([ciudad1, ciudad2]))
                    if arista not in conexiones_agregadas:
                        conexiones_agregadas.add(arista)
                        codigo_dot += f'    "{ciudad1}" -- "{ciudad2}";\n'
        
        codigo_dot += "}\n"
        
        # Guardar en archivo
        with open(f"{nombre_archivo}.dot", "w", encoding="utf-8") as f:
            f.write(codigo_dot)
        
        print(f"✓ Archivo '{nombre_archivo}.dot' generado exitosamente")
      
        
        return codigo_dot


# Ejemplo de uso
if __name__ == "__main__":
    # Crear el grafo
    grafo = GrafoNoDirigido()
    
    print("="*50)
    print("CREACIÓN DEL GRAFO DE CIUDADES")
    print("="*50 + "\n")
    
    # Agregar ciudades (nodos)
    print("1. Agregando ciudades...")
    grafo.agregar_nodo("A")
    grafo.agregar_nodo("B")
    grafo.agregar_nodo("C")
    grafo.agregar_nodo("D")
    
    print("\n2. Agregando conexiones...")
    # Agregar conexiones (aristas)
    grafo.agregar_conexion("A", "B", 10)
    grafo.agregar_conexion("A", "C", 15)
    grafo.agregar_conexion("B", "D", 20)
    
    # Visualizar la lista de adyacencia
    grafo.visualizar_lista_adyacencia()
    
    # Generar archivo Graphviz
    print("3. Generando visualización...")
    codigo = grafo.generar_graphviz("grafo_ciudades")
    
    print("\n" + "="*50)
    print("CÓDIGO GRAPHVIZ GENERADO")
    print("="*50)
    print(codigo)
    
    # Ejemplo adicional: agregar más ciudades
    print("\n" + "="*50)
    print("EJEMPLO EXTENDIDO")
    print("="*50 + "\n")
    
    grafo.agregar_nodo("E")
    grafo.agregar_conexion("C", "E", 25)
    grafo.agregar_conexion("D", "E", 30)
    
    grafo.visualizar_lista_adyacencia()
    grafo.generar_graphviz("grafo_ciudades_extendido")