from memory import (
    remember_persistent,
    recall_persistent,
    set_preference,
    get_preference
)


def process_input(user_input):

    if user_input.lower().startswith("mi preferencia "):
        preference = user_input[15:]  # antes: [14:] -> dejaba un espacio al inicio de "key"
        key, value = preference.split(" es ", 1)

        set_preference(key, value)

        return "He guardado tu preferencia."

    if user_input.lower().startswith("cuál es mi preferencia "):
        key = user_input[len("cuál es mi preferencia "):]

        preference = get_preference(key)

        if preference is None:
            return "No tengo esa preferencia guardada."

        return f"Tu preferencia para {key} es {preference}."

    if user_input.lower().startswith("recuerda que "):
        memory = user_input[13:]  # antes: [12:] -> dejaba un espacio al inicio del recuerdo

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