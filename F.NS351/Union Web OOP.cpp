/**  
 *  Writer : Byambadalai Sumiya
 *  Date   : 02-14-2019
 *  For educational only if cyrilics your platform doesn't support cyrillics then 
 *  you can change and edit it's open source. 
 *  This source is not sanitizing user input so it will crash so easily hope you 
 *  update them and use it carefully. 
 *  Have fun
**/
// I avoid include <bits/stdc++.h> 
#include <iostream>
#include <vector>
#include <utility>
#include <string>
#include <map>
#include <algorithm>
#define writeLine           cout << "============================================================\n"
#define localLine           cout << "<==========================================================>\n"
#define successLine         cout << "************************************************************\n"
#define endLine             cout << "############################################################\n"
#define teacherLine         cout << "<------------------------Багшийн веб----------------------->\n"
#define teacherLineRegister cout << "<-------------------Багшийн веб бүртгүүлэх----------------->\n"
#define teacherLineLogin    cout << "<---------------------Багшийн веб нэвтрэх------------------>\n"
#define studentLine         cout << "<------------------------Оюутны веб------------------------>\n"
#define studentLineRegister cout << "<-------------------Оюутны веб бүртгүүлэх------------------>\n"
#define studentLineLogin    cout << "<---------------------Оюутны веб нэвтрэх------------------->\n"
#define adminLine           cout << "[************************Админ веб*************************]\n"
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

// For some reason using 
using namespace std;

typedef unsigned int ui;
typedef long long i64;

// Teacher database

struct dataBaseTeacher {
  string code;
  string name;
  string password;
  vector <pair<string, pair <string, int> > > teacherStudents;
  struct lessons {
    string name;
    string code;
    float payment;
  } teacherLessons[10];
};

// Student database
struct dataBaseStudent {
  string code;
  string name;
  string password;
  int course;
  int totalCredit;
  string teacherName;
  struct lessons {
    string name;
    int credit;
  } studentLessons[30];
};
// Some global variable
vector <dataBaseTeacher> teachers;
vector <dataBaseStudent> students;
class Student {
  public:
    string sessionStudentName = "";
    string sessionStudentPassword = "";
    string sessionStudentCode = "";
    int sessionStudentIndex;
    int sessionStudentCredit;
  
    int tmp;
    Student () {
      start();
    }
    inline void start() {
      studentLine;
      cout << "1) Нэвтрэх \n2) Бүртгүүлэх\n3) Үндсэн веб\nТаны сонголт : ";
      cin >> tmp;
      switch (tmp) { case 1: {Login(); break;} case 2: {Register(); break;}}
    }
    
  private:
    inline void authorized() {
      cout << "\n\t\tТавтай морил # " << sessionStudentName << '\n';
      successLine;
      int tmpReq;
      Start:
        cout << "1) Хичээл сонгох\n2) Сонгосон хичээлээ харах\n";
        cout << "3) Хувийн мэдээлэл\n";
        cout << "4) Сонгосон багшаа харах\n5) Гарах\n";
        cout << "Таны сонголт : ";
        cin >> tmpReq;
        switch (tmpReq) {
          case 1: { localLine; planSchelude(); break; }
          case 2: { localLine; seeSchelude(); break; }
          case 3: { localLine; seeOwnInformation(); break; }
          case 4: { localLine; seeScheludesTeacher(); break; }
          case 5: { 
            this->sessionStudentName = "";
            this->sessionStudentPassword = "";
            this->sessionStudentCode = "";
            this->sessionStudentIndex = 0;
            this->sessionStudentCredit = 0;
            Student* stuObject = new Student();
            delete stuObject;
          }
          default: { 
            cout << "Таны сонгосон үйлдэл одоогоор боломжгүй байна.!\n";
            localLine;
            goto Start;
          }
        }
    }
    inline void planSchelude() {
      cout << "Test [*] planSchelude \n";
      authorized();
    }
    inline void seeSchelude() {
      cout << "Test [*] See schelude\n";
      authorized();
    }
    inline void seeOwnInformation() {
      cout << "Test [*] See own information\n";
      authorized();
    }
    inline void seeScheludesTeacher() {
      cout << "Test [*] See scheludes teacher\n";
      authorized();
    }
    inline void Login () {
      string studentCode, studentPassword;
      int tryAgain = 1;
      // Start:
        while (true) {
          studentLineLogin;
          cout << "1) Буцах\n";
          cout << "Оюутны кодоо хийнэ үү : ";
          cin >> studentCode;
          if (studentCode == "1") { Student* stuObject = new Student();
            delete stuObject; }
          if (isValidStudentCode(studentCode)) break;
          cout << "Оюутны код формат буруу байна (B170970065)\n";
        }
        cout << "Нууц үгээ хийнэ үү : ";
        cin >> studentPassword;
        int status = checkAvailableStudent(studentCode, studentPassword);
        switch(status) {
          case 1: { 
            cout << "Нууц үг буруу байна.!\n";
            if (5 - tryAgain < 1) {
              cout << "Уучлаарай 5 удаа нууц үг буруу байсан тул таныг системээс гаргалаа.\n";
              endLine;
              exit(0);
            }
            cout << 5 - tryAgain << " боломж үлдлээ.!\n";
            tryAgain++;
            // goto Start;
          }
          case 2: { 
            cout << "Оюутны код системд бүртгэгдээгүй байна.\n";
            // goto Start;
          }
          case 3: {
            authorized();
            break;
          }
        }
      authorized();
    }
    inline void Register() {
      string localName, localPassword, localCode, tmp; 
      int localCredit, localCourse;
      // Start:  
        studentLineRegister;
        cout << "1) Буцах\n";
        cout << "Нэрээ хийнэ үү : ";
        cin >> localName;
        if (localName == "1") {
          Student* stuObject = new Student();
            delete stuObject;
            }
        else if (localName.length() > 100 || localName.length() < 4) {
          cout << "Нэрний урт заавал 4 өөс их 100 аас бага байх ёстой.\n";
          // goto Start;
        }
        cout << "Оюутны кодоо хийнэ үү : ";
        cin >> localCode;
        if (!isValidStudentCode(localCode)) {
          cout << "Оюутны код формат буруу байна (B170970065)\n";
          // goto Start;
        }
        if (isInDatabaseStudent(localCode)) {
          cout << "Дараах оюутны код манай системд бүртгэлтэй байна.!\n";
          // goto Start;
        }
        localCourse = 19 - stoi(localCode.substr(1, 3));
        if (localCourse > 0) {
          cout << "Суралцаж буй курс алдаатай байна.!\n";
          // goto Start;
        }
        cout << "Суралцсан нийт кредит : ";
        cin >> localCredit;
        if (localCredit > 200 || localCredit < 0) {
          cout << "Суралцсан кредит алдаатай байна.!\n";
          // goto Start;
        }
        cout << "Бүртгүүлэх нууц үг : ";
        cin >> localPassword;
        cout << "Бүртгүүлэх нууц үг (баталгаажуулах) : ";
        cin >> tmp;
        if (localPassword != tmp) {
          cout << "Нууц үг таарахгүй байна.!\n";
          // goto Start;
        }
        dataBaseStudent tmpStruct;
        tmpStruct.name = localName;
        tmpStruct.code = localCode;
        tmpStruct.password = localPassword;
        tmpStruct.totalCredit = localCredit;
        students.push_back(tmpStruct);
        successLine;
        cout << "Бүртгэл амжилттай боллоо.!\n\n";
        Student* stuObject = new Student();
            delete stuObject;
    }
    inline int checkAvailableStudent(string studentCode, string studentPassword) {
      for (ui it = 0; it < students.size(); ++it) {
        if (students[it].code == studentCode && students[it].password == studentPassword) {
          this->sessionStudentName = students[it].name;
          this->sessionStudentPassword = students[it].password;
          this->sessionStudentCode = students[it].code;
          this->sessionStudentIndex = it;
          this->sessionStudentCredit = students[it].totalCredit;
          return 3;
        }
        else if (students[it].code == studentCode && students[it].password != studentPassword) {
          return 1;
        }
      }
      return 2;
    }
    inline bool isInDatabaseStudent (string outCode) {
      for (ui it = 0; it < students.size(); ++it) 
        if (students[it].code == outCode)
          return true;
      return false;
    }
    inline bool isValidStudentCode(string outValue) {
      if (outValue[0] != 'B' || outValue.length() != 10)
        return false;
      return true;
    }
};
class Teacher {
  public:
    string sessionTeacherName = "";
    string sessionTeacherPassword = "";
    string sessionTeacherCode = "";
    int sessionTeacherIndex;
    int sessionTeacherCredit;
    Student studentObject;
    Teacher () {
      start();
    }
    inline void start() {
      Start:
        teacherLine;
        cout << "1) Нэвтрэх \n2) Бүртгүүлэх\n3) Буцах\nТаны сонголт : ";
        int tmp; cin >> tmp;
        switch (tmp) {
          case 1: { Login(); break; } case 2: { Register(); break; }
        }
    } 
  private:
    inline void authorized() {
      successLine;
      cout << "\n\t\tТавтай морил # " << sessionTeacherName << '\n';
      int tmpReq;
      Start:
        teacherLine;
        cout << "1) Ангидаа шинэ хүүхэд нэмэх\n2) Ангийн сурагчдаа харах\n";
        cout << "3) Ангийн дарга томилох\n";
        cout << "4) Хувийн мэдээлэл харах\n5) Хичээл нэмэх\n6) Гарах\n";
        cout << "Таны сонголт : ";
        cin >> tmpReq;
        switch (tmpReq) {
          case 1: { localLine; addNewStudent(); break; }
          case 2: { localLine; showOwnStudents(); break; }
          case 3: { localLine; makeClassLeader(); break; }
          case 4: { localLine; showOwnInformation(); break; }
          case 5: { localLine; }
          case 6: { 
            this->sessionTeacherName = "";
            this->sessionTeacherPassword = "";
            this->sessionTeacherCode = "";
            this->sessionTeacherIndex = 0;
            start();
          }
          default: { 
            cout << "Таны сонгосон үйлдэл одоогоор боломжгүй байна.!\n";
            localLine;
            goto Start;
          }
        }
    }
    inline void addNewStudent() {
      Start:
        int tmpCount = 0; string tmpStudentName; bool fine = false;
        cout << "Ямар нэгэн ангид бүртгэлгүй байгаа оюутнууд : \n";
        for (ui i = 0; i < students.size(); ++i) if (students[i].teacherName == "") {
          cout << '\t' << i + 1 << ") " << students[i].code << " " << students[i].name << '\n'; tmpCount++;
        } 
        if (tmpCount == 0) { cout << "Бүх оюутан багштай эсвэл системд ямар нэгэн оюутан бүртгэгдээгүй байна.!\n"; authorized(); }
        cout << "1) Буцах\nАнгидаа нэмэх оюутны нэр эсвэл оюутны код : "; cin >> tmpStudentName; if (tmpStudentName == "1") authorized();
        for (ui i = 0; i < students.size(); i++) if (students[i].name == tmpStudentName || students[i].code == tmpStudentName) {
          teachers[sessionTeacherIndex].teacherStudents.push_back(make_pair(students[i].code, make_pair(students[i].name, 0)));
          cout << "Тус оюутныг өөрийн ангидаа амжилттай нэмлээ.!\n";
          fine = true;
        }
        if (!false) cout << "Оюутанг олсонгүй.!\n";
        goto Start;
    }
    inline void showOwnStudents() {
      Start:
        if (teachers[sessionTeacherIndex].teacherStudents.size() == 0) {
          cout << "Тухайн багш дээр бүртгэлтэй оюутан олдсонгүй.!\n";
          authorized();
        }
        sort(teachers[sessionTeacherIndex].teacherStudents.begin(), teachers[sessionTeacherIndex].teacherStudents.end());
        cout << sessionTeacherName << " багш дээр бүртгэлтэй оюутнууд : \n";
        for (unsigned int it = 0; it < teachers[sessionTeacherIndex].teacherStudents.size(); ++it) {
          if (teachers[sessionTeacherIndex].teacherStudents[it].second.second == 1) 
            cout << "\t\t" << teachers[sessionTeacherIndex].teacherStudents[it].first << " " << teachers[sessionTeacherIndex].teacherStudents[it].second.first << " (ангийн дарга)\n";
          else
            cout << "\t\t" << teachers[sessionTeacherIndex].teacherStudents[it].first << " " << teachers[sessionTeacherIndex].teacherStudents[it].second.first << '\n'; 
        }
        authorized();
    }
    inline void makeClassLeader() {
      Start:
        unsigned int tmpIndex, count = 0; string tmpStudentName;
        vector <pair <string, int > > tmpVector;
        if (teachers[sessionTeacherIndex].teacherStudents.size() == 0) {
          cout << "Тухайн багш дээр бүртгэлтэй оюутан олдсонгүй.!\n";
          authorized();
        }
        sort(teachers[sessionTeacherIndex].teacherStudents.begin(), teachers[sessionTeacherIndex].teacherStudents.end());
        cout << sessionTeacherName << " багш дээр бүртгэлтэй оюутнууд : \n";
        for (ui it = 0; it < teachers[sessionTeacherIndex].teacherStudents.size(); ++it) {
          if (teachers[sessionTeacherIndex].teacherStudents[it].second.second == 1) {   
            cout << "\t\t" << teachers[sessionTeacherIndex].teacherStudents[it].second.first << " (ангийн дарга)\n";
            count++;
          }
          else 
            cout << "\t\t" << teachers[sessionTeacherIndex].teacherStudents[it].second.first << '\n';
          tmpVector.push_back(make_pair(teachers[sessionTeacherIndex].teacherStudents[it].second.first, it));
         }
        cout << (count > 0 ? "Нэмж ангийн дарга болгох оюутны нэр : " : "Ангийн дарга болгох оюутны нэр : ");
        cin >> tmpStudentName;
        for (ui i = 0; i < tmpVector.size(); ++i) if (tmpVector[i].first == tmpStudentName) {
          tmpIndex = i; break;
        }
        if (tmpIndex != 0) { cout << "Оюутан олдсонгүй\n"; authorized(); }
        teachers[sessionTeacherIndex].teacherStudents[tmpIndex].second.second = 1;
        cout << "Амжилттай ангийн дарга томиллоо.!\n";
        authorized();
    }
    inline void showOwnInformation() {

    }
    inline void Login() {
      string teacherCode, teacherPassword;
      int tryAgain = 1;
      Start:
        while (true) {
          teacherLineLogin;
          cout << "1) Буцах\n";
          cout << "Багшийн кодоо хийнэ үү : ";
          cin >> teacherCode;
          if (teacherCode == "1") { start(); }
          if (isValidTeacherCode(teacherCode)) break;
          cout << "Багшийн код формат буруу байна (D.XY12)\n";
        }
        cout << "Нууц үгээ хийнэ үү : ";
        cin >> teacherPassword;
        int status = checkAvailableTeacher(teacherCode, teacherPassword);
        switch (status) {
          case 1: { 
            cout << "Нууц үг буруу байна.!\n";
            if (5 - tryAgain < 1) {
              cout << "Уучлаарай 5 удаа нууц үг буруу байсан тул таныг системээс гаргалаа.\n";
              endLine;
              exit(0);
            }
            cout << 5 - tryAgain << " боломж үлдлээ.!\n";
            tryAgain++;
            goto Start;
          }
          case 2: { 
            cout << "Багшийн код системд бүртгэгдээгүй байна.\n";
            goto Start;
          }
          case 3: {
            authorized();
            break;
          }
        }
      authorized();
    }
    inline void Register() {
      string localName, localPassword, localCode, tmp; 
      int localCredit, localCourse;
      Start:  
        teacherLineRegister;
        cout << "1) Буцах\n";
        cout << "Нэрээ хийнэ үү : ";
        cin >> localName;
        if (localName == "1")
          start();
        else if (localName.length() > 100 || localName.length() < 4) {
          cout << "Нэрний урт заавал 4 өөс их 100 аас бага байх ёстой.\n";
          goto Start;
        }
        cout << "Багшийн кодоо хийнэ үү : ";
        cin >> localCode;
        if (!isValidTeacherCode(localCode)) {
          cout << "Багшийн код формат буруу байна (D.XY12)\n";
          goto Start;
        }
        if (isInDatabaseTeacher(localCode)) {
          cout << "Дараах багшийн код манай системд бүртгэлтэй байна.!\n";
          goto Start;
        }
        cout << "Бүртгүүлэх нууц үг : ";
        cin >> localPassword;
        cout << "Бүртгүүлэх нууц үг (баталгаажуулах) : ";
        cin >> tmp;
        if (localPassword != tmp) {
          cout << "Нууц үг таарахгүй байна.!\n";
          goto Start;
        }
        dataBaseTeacher tmpStruct;
        tmpStruct.name = localName;
        tmpStruct.code = localCode;
        tmpStruct.password = localPassword;
        teachers.push_back(tmpStruct);
        successLine;
        cout << "Бүртгэл амжилттай боллоо.!\n\n";
        start();
    }
    inline int checkAvailableTeacher(string teacherCode, string teacherPassword) {
      for (ui it = 0; it < teachers.size(); ++it) {
        if (teachers[it].code == teacherCode && teachers[it].password == teacherPassword) {
          this->sessionTeacherName = teachers[it].name;
          this->sessionTeacherPassword = teachers[it].password;
          this->sessionTeacherCode = teachers[it].code;
          this->sessionTeacherIndex = it;
          return 3;
        }
        else if (teachers[it].code == teacherCode && teachers[it].password != teacherPassword) {
          return 1;
        }
      }
      return 2;
    }
    inline bool isInDatabaseTeacher (string outCode) {
      for (ui it = 0; it < teachers.size(); ++it) 
        if (teachers[it].code == outCode)
          return true;
      return false;
    }
    inline bool isValidTeacherCode(string outValue) {
      if (outValue.length() != 6)
        return false;
      return true;
    }
};
class Admin {
  public:
    Admin() {
      
    }
    inline void start() {
      adminLine;
      return;
    }
  private:

};
namespace GlobalMainFunction {
  inline void start() {
    Start:
    cout << "\t\tШУТИС-МХТС вебд тавтай морил\n";
    cout << "1) Оюутны веб\n2) Багшийн веб\n3) Админ\n4) Гарах\n";
    cout << "Таны сонголт : "; 
    int choise;
    cin >> choise;
    if (choise != 4 && choise != 3 && choise != 2 && choise != 1) {
      cout << "Таны оруулсан утгатай комманд олдсонгүй.!\n";
      writeLine;
      goto Start;
    }
    if (choise == 4) {
      cout << "Манай үйлчилгээг ашигласанд баярлалаа.!\n";
      endLine;
      exit(0);
    }
    switch (choise) {
      case 1: { Student* stuObject = new Student(); delete stuObject; break; }
      case 2: { Teacher* teachObject = new Teacher(); delete teachObject; break; }
      case 3: { Admin* adminObject = new Admin(); delete adminObject; break; }
    }
  return;
  }
}
int main (int args, char* argc[]) {
  GlobalMainFunction::start();
  return 0;
}
