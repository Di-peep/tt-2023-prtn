import pytest

from algorithm import get_unique_char


text_example_1 = (
    '''
    The Tao gave birth to machine language.  Machine language gave birth
    to the assembler.
    The assembler gave birth to the compiler.  Now there are ten thousand
    languages.
    Each language has its purpose, however humble.  Each language
    expresses the Yin and Yang of software.  Each language has its place within
    the Tao.
    But do not program in COBOL if you can avoid it.
            -- Geoffrey James, "The Tao of Programming"
    ''', 
    'm'
)

text_example_2 = (
    '''
    C makes it easy for you to shoot yourself in the foot. 
    C++ makes that harder, but when you do, it blows away your whole leg. (c) Bjarne Stroustrup
    ''',
    'e'
)

text_example_3 = (
    '''
      CCCC ccc   c c c c c. \n\n\n\t\t
    SsSsSsSs    (SsS)  (sSs)

    ''', 
    ''
)


def test_get_unique_char():  
    assert get_unique_char(text_example_1[0]) == text_example_1[1]
    assert get_unique_char(text_example_2[0]) == text_example_2[1]
    assert get_unique_char(text_example_3[0]) == text_example_3[1]


def test_get_unique_char_with_bad_argument():  
    with pytest.raises(TypeError):
        get_unique_char(123)
        get_unique_char([123, 123, 123])
        get_unique_char(None)  
