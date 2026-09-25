class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:

        def parse(i):
            result = set()
            product = {""}

            while i < len(expression) and expression[i] != '}':
                if expression[i] == '{':
                    group, i = parse(i + 1)

                    product = {
                        a + b
                        for a in product
                        for b in group
                    }

                elif expression[i] == ',':
                    result |= product
                    product = {""}

                else:
                    product = {
                        x + expression[i]
                        for x in product
                    }

                i += 1

            result |= product
            return result, i

        ans, _ = parse(0)
        return sorted(ans)