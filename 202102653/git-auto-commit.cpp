/*
-- Destination Location  --

~/git-repository/2023-Spring-Hamgorithm/202102653


-- CPP File Location  --

/home/bitwise/codingTest/cppProject/src/


-- JAVA File Location --

/home/bitwise/codingTest/javaProject/src/main/java/baekjoon

-- PYTHON File Location --

/home/bitwise/codingTest/pythonProject/


-- OCAML File Location --

/home/bitwise/codingTest/ocamlProject/

*/


#include <iostream>
#include <fstream>
#include <filesystem>
#include <cstdlib>
#include <ctime>
#include <string>

const std::string DESTINATION_LOC = "/home/bitwise/git-repository/2023-Spring-Hamgorithm/202102653/";
const std::string CPP_CODES_LOC = "/home/bitwise/codingTest/cppProject/src/";
const std::string JAVA_CODES_LOC = "/home/bitwise/codingTest/javaProject/src/main/java/baekjoon/bj_";
const std::string PYTHON_CODES_LOC = "/home/bitwise/codingTest/pythonProject/";
const std::string OCAML_CODES_LOC = "/home/bitwise/codingTest/ocamlProject/";

void copyFile(const std::string& src, const std::string& dest) {
    std::ifstream srcFile(src, std::ios::binary);
    std::ofstream destFile(dest, std::ios::binary);
    
    destFile << srcFile.rdbuf();
    
    srcFile.close();
    destFile.close();
}

std::string getCurrentDateTime() {
    time_t now = time(0);
    struct tm tstruct;
    char buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%B %d, %Y", &tstruct);
    return buf;
}

void exec_menu1() {
    std::string format;
    std::string problem_number;
    std::string file_name;
    std::string file_location;

    std::cout << "Extension options: cpp / java / py / ml" << std::endl;
    std::cout << "Please enter the extension of the source file: ";
    std::cin >> format;
    
    while (true) {
        if (format == "cpp") {
            file_location = CPP_CODES_LOC;
            break;
        } else if (format == "java") {
            file_location = JAVA_CODES_LOC;
            break;
        } else if (format == "py") {
            file_location = PYTHON_CODES_LOC;
            break;
        } else if (format == "ml") {
            file_location = OCAML_CODES_LOC;
            break;
        } else {
            std::cout << "Invalid input! Please enter it again: " << std::endl;
            std::cin >> format;
        }   
    }   
    
    while (true) {
        std::cout << "Please enter the number of the problem: ";
        std::cin >> problem_number;

        file_name = problem_number + "." + format;
        std::string temp_location = file_location + file_name;
        std::cout << temp_location << std::endl;
        std::string destination_file = DESTINATION_LOC + file_name;

        if (std::filesystem::exists(temp_location)) {
            copyFile(temp_location, destination_file);
            std::cout << "File copied successfully!" << std::endl;
            break;
        } else {
            std::cout << "Source file does not exist!" << std::endl;
        }
    }

    std::string commitMessage = "Solved" + problem_number + " - " + getCurrentDateTime();

    system("git add .");
    system(("git commit -m \"" + commitMessage + "\"").c_str());
    system("git push");

}

void exec_menu2() {
    std::string commitMessage;
    std::cout << "Please enter your own commit message: ";
    std::cin >> commitMessage;

    system("git add .");
    system(("git commit -m \"" + commitMessage + "\"").c_str());
    system("git push");

}

int main(void) {
    int menu_number;
    
    Select_menu:
    
    std::cout << "menu list : menu 1 - copy file & commit & push //  menu 2 - only commit & push";
    std::cout << "Please enter menu number: ";
    std::cin >> menu_number;

    if(menu_number != 1 && menu_number != 2) {
        goto Select_menu;
    } else if(menu_number == 1) {
        exec_menu1();
    } else {
        exec_menu2();
    }
    

    std::cout << "task complete!!" << std::endl;
    
    return 0;
}
