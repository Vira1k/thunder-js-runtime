import sys
from py_mini_racer import MiniRacer


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py <file.js>")
        return

    filename = sys.argv[1]

    with open(filename, "r", encoding="utf-8") as f:
        js_code = f.read()

    ctx = MiniRacer()

    wrapped_code = f"""
    var output = [];

    var console = {{
        log: function(...args) {{
            output.push(args.join(" "));
        }}
    }};

    {js_code}

    JSON.stringify(output);
    """

    try:
        result = ctx.eval(wrapped_code)

        outputs = eval(result)

        for line in outputs:
            print(line)

    except Exception as e:
        print("Runtime Error:", e)


if __name__ == "__main__":
    main()