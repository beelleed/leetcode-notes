class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.",
            "....", "..", ".---", "-.-", ".-..", "--", "-.",
            "---", ".--.", "--.-", ".-.", "...", "-", "..-",
            "...-", ".--", "-..-", "-.--", "--.."
        ]

        seen = set()

        for word in words:
            code = ""
            for ch in word:
                code += morse[ord(ch) - ord('a')]
            seen.add(code)

        return len(seen)
