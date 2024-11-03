/*
Compile this code with the following flag:
    -fsanitize=address

This flag will help in finding and fixing memory leaks. 

Your goal is to identify all memory leaks and errors, and then correct them. 
*/

#include <iostream>
#include <vector>

class Student {
private:
    std::string name_;
    int age_;

public:
    Student(const std::string &name, int age)
        : name_(name), age_(age) {}

    void printInfo() const {
        std::cout << "Name: " << name_ << ", Age: " << age_ << std::endl;
    }

};

class Classroom {
private:
    std::vector<const Student*> students_;

public:
    Classroom() {}

    ~Classroom() {
    }

    void addStudent(const Student & s) {
        students_.push_back(&s);
    }

    void displayStudents() const {
        for (const auto &student : students_) {
            student->printInfo();
        }
    }

    const Student & get_student(int i)
    {
        return *students_[i];
    }

};

int main() {
    Classroom *class1 = new Classroom();

    Student * s1 = new Student("John", 20);
    Student * s2 = new Student("Jane", 21);
    class1->addStudent(*s1);
    class1->addStudent(*s2);

    class1->displayStudents();

    // print the second student
    class1->get_student(2).printInfo();

    return 0;

}
