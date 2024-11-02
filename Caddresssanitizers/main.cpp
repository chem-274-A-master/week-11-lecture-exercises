/*
Compile this code with the following flag:
    -fsanitize=address

This flag will help in finding and fixing memory leaks. 

Your goal is to identify all memory leaks and then correct them. 

Hint: Pay close attention to dynamically allocated memory and how it's managed.
*/

#include <iostream>
#include <vector>

class Student {
public:
    Student(const std::string &name, int age)
        : name_(name), age_(age) {}

    void printInfo() const {
        std::cout << "Name: " << name_ << ", Age: " << age_ << std::endl;
    }

private:
    std::string name_;
    int age_;
};

class Classroom {
public:
    Classroom() {}

    ~Classroom() {
    }

    void addStudent(const std::string &name, int age) {
        students_.push_back(new Student(name, age));
    }

    void displayStudents() const {
        for (const auto &student : students_) {
            student->printInfo();
        }
    }

private:
    std::vector<Student*> students_;
};

int main() {
    Classroom *class1 = new Classroom();

    class1->addStudent("John", 20);
    class1->addStudent("Jane", 21);

    int *dynamicArray = new int[100];  

    for (int i = 0; i < 100; i++) {
        dynamicArray[i] = i;
    }

    class1->displayStudents();
 
    Student* loneStudent = new Student("Lucas", 23);

    return 0;
}
