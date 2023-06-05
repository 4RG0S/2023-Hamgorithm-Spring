#include <iostream>
#include <cstdlib>
#include <ctime>
#include <string>

std::string getCurrentDateTime() {
    time_t now = time(0);
    struct tm tstruct;
    char buf[80];
    tstruct = *localtime(&now);
    strftime(buf, sizeof(buf), "%Y-%m-%d %X", &tstruct);
    return buf;
}

int main() {
    std::string commitMessage = "New commit in " + getCurrentDateTime();
    
    system("git add .");
    system(("git commit -m \"" + commitMessage + "\"").c_str());
    system("git push");
    
    return 0;
}

