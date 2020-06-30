// Author: Byambadalai Sumiya
#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair
#define ff first
#define ss second
#define sz(x) (int)(x).size()
#define all(x) (x).begin(),(x).end()
#define PI 3.14159265

using namespace std;

vector <char> box;
int done = 0;

inline int isDoneForWithoutBracket (string expression) {
  // cout << "Checking : " << expression << '\n';
  int leftBracket = 0, rightBracket = 0, operat = 0;
  for (int i = 0; i < expression.length(); i++) {
    leftBracket += (expression[i] == '(');
    rightBracket += (expression[i] == ')');
    if (expression[i] == '+' || expression[i] == '-' || expression[i] == '*' || expression[i] == '/')
      operat++;
  }
  if (operat == 1 && leftBracket == 1 && rightBracket == 1)
    return 3;
  if (expression[0] == '-') {
    bool can = true;
    for (int i = 1; i < expression.length(); i++) {
      if ((expression[i] >= 48 && expression[i] <= 57) || expression[i] == '.')
        continue;
      else { can = false; break; }
    }
    if (can) return 0;
  }
  for (int i = 0; i < expression.length(); i++)
    if (expression[i] == '*' || expression[i] == '/')
      return 1;
  for (int i = 0; i < expression.length(); i++)
    if (expression[i] == '+' || expression[i] == '-')
      return 2;
  return 0;
}
template <typename T>
std::string to_string(T const& value) {
  stringstream sstr;
  sstr << value;
  return sstr.str();
}
inline string calcWithoutBracket (string expression) {
  int status = isDoneForWithoutBracket(expression);
  cout << "Status " << status << " " << expression << '\n';
  switch (status) {
    case 1: {
      for (int i = 0; i < expression.length(); i++) {
        if ((expression[i] == '*' || expression[i] == '/') && i != 0) {
          string left = "", right = "";
          int startIndex, endIndex;
          bool ok = false;
          // Start right side;
          if (expression[i + 1] == '(') {
            ok = true;
            for (int j = i + 2; j < expression.length(); j++) {
              if (expression[j] == ')') { endIndex = j + 1; break; }
              else right += expression[j];
            }
          }
          if (!ok) {
            for (int j = i + 1; j < expression.length(); j++) {
              if ((expression[j] >= 48 && expression[j] <= 57) || expression[j] == '.') {
                if (j == expression.length() - 1)
                  endIndex = j;
                right += expression[j];
              }
              else { endIndex = j; break; }
            }
          }
          cout << "RIGHT : " << right << '\n';
          // Done right side;
          // Start left side;
          ok = false;
          cout << "EXrpession  " << expression << '\n';
          if (expression[i - 1] == ')') {
            ok = true;
            for (int j = i - 2; j >= 0; j--) {
              if (expression[j] == '(') { startIndex = j - 1; break; }
              else if (j == 0) { left += expression[j]; startIndex = 0; break; }
              else left += expression[j];
            }
          }
          cout << "LEFT : " << left << '\n';
          if (!ok) {
            for (int j = i - 1; j >= 0; j--) {
              if (j == 0 && expression[j] == '-') {
                startIndex = 0;
                left += expression[j];
                break;
              }
              if ((expression[j] >= 48 && expression[j] <= 57) || expression[j] == '.') {
                if (j == 0) {
                  startIndex = 0;
                  left += expression[j];
                  break;
                }
                left += expression[j];
              }
              else if (j == 0) { startIndex = 0; break; }
              else { startIndex = j; break; }
            }
          }
          // cout << "LEFT : " << left << '\n';
          // Done left side;
          reverse (left.begin(), left.end());
          cout << left << " " << right << '\n';
          // cout << startIndex << " " << endIndex << "\n";
          double num1 = stod(left), num2 = stod(right), ans;
          // cout << expression[i] << '\n';
          ans = (expression[i] == '*' ? num1 * num2 : num1 / num2);
          string tmp = to_string(ans);
          // cout << tmp << '\n';
          if (startIndex != 0)
            if (ans < 0)
              tmp = '(' + tmp + ')';
          if (startIndex != 0)
          for (int j = 0; j <= startIndex; j++) box.push_back(expression[j]);
          for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
          for (int j = endIndex; j < expression.length(); j++) box.push_back(expression[j]);
          expression = "";
          for (int j = 0; j < box.size(); j++) expression += box[j];
          // cout << "Now -> " << expression << '\n';
          box.clear();
          return calcWithoutBracket(expression);
        }
      }
      break;
    }
    case 2: {
      for (int i = 0; i < expression.length(); i++) {
        if ((expression[i] == '+' || expression[i] == '-') && i != 0 ) {
          string left = "", right = "";
          int startIndex, endIndex;
          bool ok = false;
          // Start right side;
          if (expression[i + 1] == '(') {
            ok = true;
            for (int j = i + 2; j < expression.length(); j++) {
              if (expression[j] == ')') { endIndex = j + 1; break; }
              else right += expression[j];
            }
          }
          if (!ok) {
            for (int j = i + 1; j < expression.length(); j++) {
              if ((expression[j] >= 48 && expression[j] <= 57) || expression[j] == '.') {
                if (j == expression.length() - 1)
                  endIndex = j;
                right += expression[j];
              }
              else { endIndex = j; break; }
            }
          }
          cout << "RIGHT : " << right << '\n';
          // Done right side;
          // Start left side;
          ok = false;
          cout << "EXrpession  " << expression << '\n';
          if (expression[i - 1] == ')') {
            ok = true;
            for (int j = i - 2; j >= 0; j--) {
              if (expression[j] == '(') { startIndex = j - 1; break; }
              else if (j == 0) { left += expression[j]; startIndex = 0; break; }
              else left += expression[j];
            }
          }
          cout << "LEFT : " << left << '\n';
          if (!ok) {
            for (int j = i - 1; j >= 0; j--) {
              if (j == 0 && expression[j] == '-') {
                startIndex = 0;
                left += expression[j];
                break;
              }
              if ((expression[j] >= 48 && expression[j] <= 57) || expression[j] == '.') {
                if (j == 0) {
                  startIndex = 0;
                  left += expression[j];
                  break;
                }
                left += expression[j];
              }
              else if (j == 0) { startIndex = 0; break; }
              else { startIndex = j; break; }
            }
          }
          // cout << "LEFT : " << left << '\n';
          // Done left side;
          reverse (left.begin(), left.end());
          cout << left << " " << right << '\n';
          // cout << startIndex << " " << endIndex << "\n";
          double num1 = stod(left), num2 = stod(right), ans;
          // cout << expression[i] << '\n';
          ans = (expression[i] == '+' ? num1 + num2 : num1 - num2);
          string tmp = to_string(ans);
          // cout << tmp << '\n';
          if (startIndex != 0)
            if (ans < 0)
              tmp = '(' + tmp + ')';
          if (startIndex != 0)
          for (int j = 0; j <= startIndex; j++) box.push_back(expression[j]);
          for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
          for (int j = endIndex; j < expression.length(); j++) box.push_back(expression[j]);
          expression = "";
          for (int j = 0; j < box.size(); j++) expression += box[j];
          // cout << "Now -> " << expression << '\n';
          box.clear();
          return calcWithoutBracket(expression);
        }
      }
      break;
    }
    case 3: {
      return expression.substr(1, expression.length() - 2);
      break;
    }
    case 0: {
      if (expression[0] == '-')
        return '(' + expression + ')';
      return expression;
      break;
    }
  }
  return "Crash";
}
inline string sanitizeUserInput (string expression) {
  // sin(x), cos(x), tan(x), sqrt(x)
  for (int i = 0; i < expression.length(); i++) {
    if (expression[i] == 's' && expression[i + 1] == 'i' && expression[i + 2] == 'n') {
      string tmp = "";
      int endInd;
      for (int j = i + 4; j < expression.length(); j++) {
        if (expression[j] == ')') { endInd = j; break; }
        tmp += expression[j];
      }
      cout << tmp << '\n';
      double tmpNumber = stod(tmp);
      tmpNumber = sin(tmpNumber);
      cout << tmpNumber << '\n';
      tmp = to_string(tmpNumber);
      if (i != 0)
        if (tmpNumber < 0)
          tmp = '(' + tmp + ')';
      cout << "last tmp : " << tmp << '\n';
      for (int j = 0; j < i; j++) box.push_back(expression[j]);
      for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
      for (int j = endInd + 1; j < expression.length(); j++) box.push_back(expression[j]);
      expression = "";
      for (int j = 0; j < box.size(); j++)
        expression += box[j];
      box.clear();
      return expression;
    }
    else if (expression[i] == 'c' && expression[i + 1] == 'o' && expression[i + 2] == 's') {
      string tmp = "";
      int endInd;
      for (int j = i + 4; j < expression.length(); j++) {
        if (expression[j] == ')') { endInd = j; break; }
        tmp += expression[j];
      }
      cout << tmp << '\n';
      double tmpNumber = stod(tmp);
      tmpNumber = cos(tmpNumber);
      cout << tmpNumber << '\n';
      tmp = to_string(tmpNumber);
      if (i != 0)
        if (tmpNumber < 0)
          tmp = '(' + tmp + ')';
      cout << "last tmp : " << tmp << '\n';
      for (int j = 0; j < i; j++) box.push_back(expression[j]);
      for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
      for (int j = endInd + 1; j < expression.length(); j++) box.push_back(expression[j]);
      expression = "";
      for (int j = 0; j < box.size(); j++)
        expression += box[j];
      box.clear();
      return expression;
    }
    else if (expression[i] == 't' && expression[i + 1] == 'a' && expression[i + 2] == 'n') {
      string tmp = "";
      int endInd;
      for (int j = i + 4; j < expression.length(); j++) {
        if (expression[j] == ')') { endInd = j; break; }
        tmp += expression[j];
      }
      cout << tmp << '\n';
      double tmpNumber = stod(tmp);
      tmpNumber = tan(tmpNumber);
      cout << tmpNumber << '\n';
      tmp = to_string(tmpNumber);
      if (i != 0)
        if (tmpNumber < 0)
          tmp = '(' + tmp + ')';
      cout << "last tmp : " << tmp << '\n';
      for (int j = 0; j < i; j++) box.push_back(expression[j]);
      for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
      for (int j = endInd + 1; j < expression.length(); j++) box.push_back(expression[j]);
      expression = "";
      for (int j = 0; j < box.size(); j++)
        expression += box[j];
      box.clear();
      return expression;
    }
    else if (expression[i] == 's' && expression[i + 1] == 'q' && expression[i + 2] == 'r' && expression[i + 3] == 't') {
      string tmp = "";
      int endInd;
      for (int j = i + 5; j < expression.length(); j++) {
        if (expression[j] == ')') { endInd = j; break; }
        tmp += expression[j];
      }
      // cout << tmp << '\n';
      double tmpNumber = stod(tmp);
      tmpNumber = sqrt(tmpNumber);
      // cout << tmpNumber << '\n';
      tmp = to_string(tmpNumber);
      if (tmpNumber < 0)
        tmp = '(' + tmp + ')';
      // cout << "last tmp : " << tmp << '\n';
      for (int j = 0; j < i; j++) box.push_back(expression[j]);
      for (int j = 0; j < tmp.length(); j++) box.push_back(tmp[j]);
      for (int j = endInd + 1; j < expression.length(); j++) box.push_back(expression[j]);
      expression = "";
      for (int j = 0; j < box.size(); j++)
        expression += box[j];
      box.clear();
      return expression;
    }
  }
  done = 1;
  return expression;
}
inline bool isDoneBracket (string expression) {
  return true;
}
inline string powerOfRecursive (string value) {
  string newValue = "";
  bool ok = false;
  for (int i = 0; i < value.length(); i++) {
    if (value[i] == '(') {
      ok = true;
      int endInd, startInd = i;
      string tmp = "";
      for (int j = i + 1; j < value.length(); j++) {
        if (value[j] == ')') {
          endInd = j;
          break;
        }
        tmp += value[j];
      }
      tmp = calcWithoutBracket(tmp);
      for (int j = 0; j < startInd; j++)
        newValue += value[j];
      for (int j = 0; j < tmp.length(); j++)
        newValue += tmp[j];
      for (int j = endInd + 1; j < value.length(); j++)
        newValue += value[j];
      cout << "New value : " << newValue << '\n';
      if (isDoneBracket(newValue)) {
        cout << "returning : " << newValue << '\n';
        return newValue;
      }
      newValue = powerOfRecursive(newValue);
    }
  }
  if (!ok) newValue = value;
  cout << "Returning : " << newValue << '\n';
  return newValue;
}
int main() {
  cout << "Enter your expression : ";
  string first;
  cin >> first;
  while (true) {
    cout << first << '\n';
    first = sanitizeUserInput(first);
    if (done == 1)
      break;
  }
  // sqrt(36)+567-sin(23)*572/cos(34)
  // (12313*23/123)+(42342-123+123-sin(23)+32)
  // 123*sin(223)+2323/231*sqrt(36)-(123+323-123/23+213)
  // 1234+sin(123)-(sin(32)+123*123/23-123)/(323*23-sqrt(64))
  // (123123*23123123/1123*123-12313)-123123*9213+923-12.3128/tan(23)
  // sin(23)*(2131/23)*3-(2323-sin(34))*sqrt(63)+23*123-123/34*1-234/123
  cout << first << '\n';
  cout << "Power of recursive starting \n";
  string last = powerOfRecursive(first);
  cout << "Calculator starting\n";
  string finals = calcWithoutBracket(last);
  // string last = powerOfRecursive(first);
  cout << "Answer : " << finals << '\n';
}
