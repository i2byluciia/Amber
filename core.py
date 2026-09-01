from memory import remember_persistent, recall_persistent

def process_input(user_input):
    if user_input.lower().startswith("recuerda que "):
        memory = user_input[12:]
        remember_persistent(memory)
        return "Lo recordaré."

    if user_input.lower() == "¿qué recuerdas?":
        memories = recall_persistent()

        if not memories:
            return "No recuerdo nada todavía."

        response = "Recuerdo:\n"

        for memory in memories:
            response += f"- {memory[1]}\n"

        return response


def generate_response(user_input):
    return f"You said '{user_input}'"