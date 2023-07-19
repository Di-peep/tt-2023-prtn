def get_unique_char(string: str) -> str:

    if string.count(' ') > 0:
        first_uniq_chars = ''.join([get_unique_char(word) for word in string.split()])
        return get_unique_char(first_uniq_chars)

    for char in string:
        if string.count(char) == 1:
            return char
    
    return ''


txt1 = """
The Tao gave birth to machine language.  Machine language gave birth
to the assembler.
The assembler gave birth to the compiler.  Now there are ten thousand
languages.
Each language has its purpose, however humble.  Each language
expresses the Yin and Yang of software.  Each language has its place within
the Tao.
But do not program in COBOL if you can avoid it.
        -- Geoffrey James, "The Tao of Programming"
"""

txt2 = """
C makes it easy for you to shoot yourself in the foot. C++ makes that harder, but when you do, it blows away your whole leg. (c) Bjarne Stroustrup
"""


if __name__ == '__main__':
    print(get_unique_char(txt2))
