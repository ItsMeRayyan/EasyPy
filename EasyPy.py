#Instructions in Instructions.md

def replace_conditions(text):
    text = text.replace("smaller than", "<")
    text = text.replace("bigger than", ">")
    text = text.replace("equal to", "==")
    return text


def translate(code):
    lines = code.splitlines()
    py = []
    indent = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue

        # ASSIGNMENT
        if line.startswith("set "):
            parts = line[4:].split(" to ")
            var = parts[0].strip()
            val = parts[1].strip()
            py.append("    " * indent + f"{var} = {val}")
            continue

        line = replace_conditions(line)

        if line.startswith("print "):
            content = line[6:]
            py.append("    " * indent + f"print({content})")

        elif line.startswith("if ") and line.endswith("{"):
            condition = line[3:-1].strip()
            py.append("    " * indent + f"if {condition}:")
            indent += 1

        elif line.startswith("while ") and line.endswith("{"):
            condition = line[6:-1].strip()
            py.append("    " * indent + f"while {condition}:")
            indent += 1

        elif line == "}":
            indent -= 1

        else:
            py.append("    " * indent + line)

    return "\n".join(py)


def run_file(filename):
    with open(filename, "r") as f:
        code = f.read()
    python_code = translate(code)
    exec(python_code)


# ---- RUN ----
run_file("test.epy")
