#include <iostream>
#include <set>
#include <stdexcept>
#include <vector>

typedef struct Compare {
    bool operator()(const char& a, const char& b) const { return a < b; }
} Compare;

bool IsVowel(char ch) {
    char vowels[] = {'a', 'e', 'i', 'o', 'u'};
    for (char vowel : vowels) {
        if (vowel == ch) return true;
    }
    return false;
}

std::set<std::set<char, Compare>> ChoiceNChars(std::set<char, Compare> chars,
                                               int n) {
    if (n == 0) throw std::runtime_error("n should be > 0");

    std::set<std::set<char, Compare>> result;
    std::set<char, Compare> temp;

    if (n == 1) {
        for (char ch : chars) {
            temp.insert(ch);
            result.insert(temp);
            temp.clear();
        }
        return result;
    }

    for (std::set<char, Compare> prev_set : ChoiceNChars(chars, n - 1)) {
        for (char ch : chars) {
            if (prev_set.find(ch) == prev_set.end()) {
                std::set<char, Compare> temp(prev_set);
                temp.insert(ch);
                result.insert(temp);
                continue;
            }
        }
    }

    return result;
}

bool IsValid(std::set<char, Compare> set) {
    int consonants = 0, vowels = 0;
    for (char ch : set) {
        if (IsVowel(ch)) vowels++;
        else consonants++;
    }
    return vowels >= 1 && consonants >= 2;
}

int main() {
    int L, C;
    std::set<char, Compare> consonants, vowels, inputs;
    std::set<char, Compare> sorted;

    std::cin >> L >> C;

    char temp;
    for (int i = 0; i < C; ++i) {
        std::cin >> temp;
        inputs.insert(temp);

        if (IsVowel(temp))
            vowels.insert(temp);
        else
            consonants.insert(temp);
    }

    for (std::set<char, Compare> set : ChoiceNChars(inputs, L)) {
        if (!IsValid(set)) continue;
        
        for (char ch : set) {
            std::cout << ch;
        }
        std::cout << std::endl;
    }

    return 0;
}