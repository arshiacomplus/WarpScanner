
#!/bin/bash
command -v python3 &>/dev/null || {
    echo "Python 3 نصب نیست. در حال نصب..."

    pkg install python-pip 
    pkg install git python
}
    # این دستور بستگی به سیستم عامل شما دارد. مثال
# دانلود اسکریپت پایتون
curl -fsSL -o script.py https://github.com/arshiacomplus/Test/blob/main/FixResult.py

# اجرای اسکریپت پایتون
python3 script.py
