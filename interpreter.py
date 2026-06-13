class Interpreter:
    def __init__(self):
        self.env = {}
        self.functions = {}

    def evaluate_expression(self, expr):
        expr = expr.strip()

        # function call
        if "(" in expr and ")" in expr:
            func_name = expr[:expr.find("(")].strip()

            if func_name in self.functions:
                arg_string = expr[
                    expr.find("(")+1:
                    expr.rfind(")")
                ]

                args = []

                if arg_string:
                    args = [
                        self.evaluate_expression(a.strip())
                        for a in arg_string.split(",")
                    ]

                return self.call_function(
                    func_name,
                    args
                )

        # Math.floor()
        if expr.startswith("Math.floor("):
            inner = expr[len("Math.floor("):-1]

            return int(
                self.evaluate_expression(inner)
            )

        # ===
        if "===" in expr:
            left, right = expr.split("===")

            return (
                self.evaluate_expression(left.strip())
                ==
                self.evaluate_expression(right.strip())
            )

        # <=
        if "<=" in expr:
            left, right = expr.split("<=")

            return (
                self.evaluate_expression(left.strip())
                <=
                self.evaluate_expression(right.strip())
            )

        # >
        if ">" in expr:
            left, right = expr.split(">")

            return (
                self.evaluate_expression(left.strip())
                >
                self.evaluate_expression(right.strip())
            )

        # **
        if "**" in expr:
            left, right = expr.split("**")

            left_val = self.evaluate_expression(
                left.strip()
            )

            right_val = self.evaluate_expression(
                right.strip()
            )

            return int(left_val) ** int(right_val)

        # %
        if "%" in expr:
            left, right = expr.split("%")

            left_val = self.evaluate_expression(
                left.strip()
            )

            right_val = self.evaluate_expression(
                right.strip()
            )

            return int(float(left_val)) % int(float(right_val))

        # /
        if "/" in expr:
            left, right = expr.split("/")

            return float(
                self.evaluate_expression(left.strip())
                /
                self.evaluate_expression(right.strip())
            )

        # +
        if "+" in expr:
            parts = expr.split("+")

            values = [
                self.evaluate_expression(
                    p.strip()
                )
                for p in parts
            ]

            if any(
                isinstance(v, str)
                for v in values
            ):
                return "".join(
                    str(v)
                    for v in values
                )

            return sum(values)

        # boolean
        if expr == "true":
            return True

        if expr == "false":
            return False

        # variable
        if expr in self.env:
            return self.env[expr]

        # number
        try:
            return int(expr)
        except:
            pass

        # string
        if (
            expr.startswith('"')
            and expr.endswith('"')
        ) or (
            expr.startswith("'")
            and expr.endswith("'")
        ):
            return expr[1:-1]

        return expr

    def execute_console_log(self, line):
        expr = line[
            line.find("(")+1:
            line.rfind(")")
        ]

        result = self.evaluate_expression(expr)

        if result is True:
            print("true")
        elif result is False:
            print("false")
        else:
            print(result)

    def execute_block(self, block_lines):
        i = 0

        while i < len(block_lines):
            line = block_lines[i].strip()

            # let
            if line.startswith("let "):
                line = (
                    line.replace("let ", "")
                    .replace(";", "")
                )

                var_name, value = line.split("=", 1)

                self.env[
                    var_name.strip()
                ] = self.evaluate_expression(
                    value.strip()
                )

            # +=
            elif "+=" in line:
                var_name, value = (
                    line.replace(";", "")
                    .split("+=")
                )

                current = self.env.get(
                    var_name.strip(),
                    0
                )

                self.env[
                    var_name.strip()
                ] = (
                    current +
                    self.evaluate_expression(
                        value.strip()
                    )
                )

            # reassignment
            elif (
                "=" in line
                and "==" not in line
                and not line.startswith("while")
            ):
                line = line.replace(";", "")

                var_name, value = (
                    line.split("=", 1)
                )

                self.env[
                    var_name.strip()
                ] = self.evaluate_expression(
                    value.strip()
                )

            # while
            elif line.startswith("while"):
                condition = line[
                    line.find("(")+1:
                    line.find(")")
                ]

                loop_block = []

                i += 1

                while (
                    i < len(block_lines)
                    and "}" not in block_lines[i]
                ):
                    loop_block.append(
                        block_lines[i]
                    )
                    i += 1

                while self.evaluate_expression(
                    condition
                ):
                    result = self.execute_block(
                        loop_block
                    )

                    if result is not None:
                        return result

            # return
            elif line.startswith("return"):
                expr = (
                    line.replace(
                        "return", ""
                    )
                    .replace(";", "")
                    .strip()
                )

                return self.evaluate_expression(
                    expr
                )

            # console.log
            elif "console.log" in line:
                self.execute_console_log(
                    line
                )

            i += 1

    def call_function(self, name, args):
        params, body = self.functions[name]

        backup_env = self.env.copy()

        for p, a in zip(params, args):
            self.env[p] = a

        result = self.execute_block(body)

        self.env = backup_env

        return result

    def run(self, code):
        lines = [
            line.strip()
            for line in code.split("\n")
            if line.strip()
        ]

        i = 0

        while i < len(lines):
            line = lines[i]

            # function
            if line.startswith("function"):
                func_name = (
                    line.split()[1]
                )

                func_name = (
                    func_name[
                        :func_name.find("(")
                    ]
                )

                params = line[
                    line.find("(")+1:
                    line.find(")")
                ].split(",")

                params = [
                    p.strip()
                    for p in params
                    if p.strip()
                ]

                body = []

                i += 1
                brace_count = 1

                while i < len(lines):
                    current_line = lines[i]

                    if "{" in current_line:
                        brace_count += 1

                    if "}" in current_line:
                        brace_count -= 1

                        if brace_count == 0:
                            break

                    body.append(
                        current_line
                    )
                    i += 1

                self.functions[
                    func_name
                ] = (
                    params,
                    body
                )

            # console.log
            elif "console.log" in line:
                self.execute_console_log(
                    line
                )

            i += 1