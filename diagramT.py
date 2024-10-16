class Program:
    def __init__(self, name, language):
        self.name = name
        self.language = language

class Interpreter:
    def __init__(self, base_language, target_language):
        self.base_language = base_language
        self.target_language = target_language

class Translator:
    def __init__(self, base_language, source_language, destination_language):
        self.base_language = base_language
        self.source_language = source_language
        self.destination_language = destination_language

class Simulator:
    def __init__(self):
        self.programs = {}
        self.interpreters = []
        self.translators = []

    def define_program(self, name, language):
        if name in self.programs:
            print(f"Error: El programa '{name}' ya está definido.")
        else:
            self.programs[name] = Program(name, language)
            print(f"Se definió el programa '{name}', ejecutable en '{language}'")

    def define_interpreter(self, base_language, target_language):
        interpreter = Interpreter(base_language, target_language)
        self.interpreters.append(interpreter)
        print(f"Se definió un intérprete para '{target_language}', escrito en '{base_language}'")

    def define_translator(self, base_language, source_language, destination_language):
        translator = Translator(base_language, source_language, destination_language)
        self.translators.append(translator)
        print(f"Se definió un traductor de '{source_language}' hacia '{destination_language}', escrito en '{base_language}'")

    def can_execute(self, name):
        if name not in self.programs:
            print(f"Error: El programa '{name}' no está definido.")
            return

        program_language = self.programs[name].language
        if program_language == "LOCAL":
            print(f"Sí, es posible ejecutar el programa '{name}'")
            return

        # Revisar si es posible ejecutar a través de intérpretes o traductores
        if self._can_interpret_or_translate(program_language, "LOCAL"):
            print(f"Sí, es posible ejecutar el programa '{name}'")
        else:
            print(f"No es posible ejecutar el programa '{name}'")

    def _can_interpret_or_translate(self, source_language, target_language):
        if source_language == target_language:
            return True

        for interpreter in self.interpreters:
            if interpreter.base_language == target_language and interpreter.target_language == source_language:
                return True

        for translator in self.translators:
            if translator.destination_language == target_language and translator.source_language == source_language:
                return True

        return False

    def run(self):
        while True:
            action = input("$> ").strip().split()

            if not action:
                continue

            if action[0] == "DEFINIR":
                if action[1] == "PROGRAMA":
                    self.define_program(action[2], action[3])
                elif action[1] == "INTERPRETE":
                    self.define_interpreter(action[2], action[3])
                elif action[1] == "TRADUCTOR":
                    self.define_translator(action[2], action[3], action[4])
            elif action[0] == "EJECUTABLE":
                self.can_execute(action[1])
            elif action[0] == "SALIR":
                break
            else:
                print("Comando no reconocido.")

if __name__ == "__main__":
    simulator = Simulator()
    simulator.run()
