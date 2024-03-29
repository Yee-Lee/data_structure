#include <iostream>
#include <stack>
#include <string>

struct Bracket {
    Bracket(char type, int position):
        type(type),
        position(position)
    {}

    bool Matchc(char c) {
        if (type == '[' && c == ']')
            return true;
        if (type == '{' && c == '}')
            return true;
        if (type == '(' && c == ')')
            return true;
        return false;
    }

    char type;
    int position;
};

int main() {
    std::string text;
    getline(std::cin, text);

    bool ret = true;
    int ret_num = 0;
    std::stack <Bracket> opening_brackets_stack;
    for (int position = 0; position <(int) text.length(); ++position) {
        char next = text[position];

        if (next == '(' || next == '[' || next == '{') {
            // Process opening bracket, write your code here
            opening_brackets_stack.push(Bracket(next, position));
        }

        if (next == ')' || next == ']' || next == '}') {
            // Process closing bracket, write your code here
            Bracket b = opening_brackets_stack.top();
            opening_brackets_stack.pop();
            if(!b.Matchc(next)){
                ret_num = position;
                ret = false;
                break;
            }
        }
    }
    if(ret)
        std::cout<<"Success"<<std::endl;
        
    else
        std::cout<<ret_num<<std::endl;
    // Printing answer, write your code here

    return 0;
}
