from ai.behavior_tree.enemy.behavior_tree import Selector , Action , Sequence , Invert , Timer


class Zombie:
    def __init__(self, tiempo_atacando=3):
        self.objetivo = None
        self.comportamiento = Selector([
            self.crear_secuencia_reposo(),
            self.crear_secuencia_ataque(tiempo_atacando)
        ])

    def crear_secuencia_reposo(self):
        hay_objetivo = Action(lambda: self.objetivo is not None)
        return Sequence([
            Invert(hay_objetivo),
            Action(self.patrullar)
        ])

    def crear_secuencia_ataque(self, tiempo_atacando):
        return Sequence([
            Action(self.objetivo_cerca),
            Action(self.perseguir_jugador),
            Action(self.atacar),
            Timer(tiempo_atacando, Action(self.desactivar_objetivo))
        ])

    def agregar_objetivo(self, objetivo=None):
        self.objetivo = objetivo
        print("Objetivo agregado")

    def desactivar_objetivo(self):
        self.objetivo = None
        print("Objetivo desactivado")
        return True

    def objetivo_cerca(self):
        # Lógica para determinar si el objetivo está cerca
        return True

    def patrullar(self):
        print("Patrullando...")
        # Lógica para patrullar
        return True

    def caminar(self):
        print("Caminando...")
        # Lógica para caminar
        return True

    def perseguir_jugador(self):
        print("Persiguiendo al jugador...")
        # Lógica para perseguir al jugador
        return True

    def atacar(self):
        print("Atacando al objetivo " + str(self.objetivo))
        return True

    def actualizar(self):
        self.comportamiento.run()
