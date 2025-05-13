from textnode import TextNode, TextType

def main():
    node = TextNode("hello there", TextType.BOLD, "https://printhelloworldinpython.com")
    print(node)

main()